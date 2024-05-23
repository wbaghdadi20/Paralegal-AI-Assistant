import time
import os
from openai import OpenAI
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import Binary

load_dotenv()
client = OpenAI()

# MongoDB configuration
MONGODB_URI = os.environ['MONGODB_URL']
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client["clients"]
collection = db["collection"]

# global var
current_thread_question_preprocess = None
current_thread_answers_demo = None

def create_new_conversation():
    global current_thread_question_preprocess, current_thread_answers_demo
    
    # create two new threads
    current_thread_question_preprocess = client.beta.threads.create()
    current_thread_answers_demo = client.beta.threads.create()
    
    # create doc of threads in mangodb
    thread_doc = {
        "thread_id_question_preprocess": current_thread_question_preprocess.id,
        "thread_id_answers_demo": current_thread_answers_demo.id,
        "files": [],
        "messages": []
    }
    collection.insert_one(thread_doc)
    
    return current_thread_question_preprocess.id, current_thread_answers_demo.id

def upload_files(thread_id, directory_path):
    file = []
    file_flag = 0

    if os.listdir(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):  # Check if it is a file
                file_uploaded = client.files.create(
                    file=open(file_path, "rb"),
                    purpose="user_data"
                )
                file.append(file_uploaded.id)
                file_flag = 1

                # store user uploaded file into MongoDB，attach to corresponding thread
                with open(file_path, "rb") as f:
                    file_data = f.read()
                    file_doc = {
                        "filename": filename,
                        "file_id": file_uploaded.id,
                        "file_data": Binary(file_data)
                    }
                    collection.update_one(
                        {"thread_id_question_preprocess": thread_id},
                        {"$push": {"files": file_doc}}
                    )
    return file, file_flag

def continue_conversation(thread_id_question_preprocess, thread_id_answers_demo, user_message):
    # add user message into thread
    message = client.beta.threads.messages.create(
        thread_id=thread_id_question_preprocess,
        role="user",
        content=user_message
    )

    # Update Mangodb's thread doc
    collection.update_one(
        {"thread_id_question_preprocess": thread_id_question_preprocess},
        {"$push": {"messages": {"role": "user", "content": user_message}}}
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id_question_preprocess,
        assistant_id="asst_H45C7dVAP6ltH8wCMXDDg2cj",
    )

    # create new run and wait 
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread_id_question_preprocess, run_id=run.id)
        print("Status: ", run.status)
        time.sleep(1)
    else:
        print("Completed")

    messages_response = client.beta.threads.messages.list(thread_id=thread_id_question_preprocess)
    messages = messages_response.data
    preprocessed_question = messages[0].content[0].text.value

    # generate final answers
    message = client.beta.threads.messages.create(
        thread_id=thread_id_answers_demo,
        role="user",
        content=preprocessed_question
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id_answers_demo,
        assistant_id="asst_c8wI5kjTBL0YSNJuQfErp1s3",  # assistant v2 turbo
    )

    # create new run for final answer
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread_id_answers_demo, run_id=run.id)
        print("Status: ", run.status)
        time.sleep(1)
    else:
        print("Completed")

    messages_response = client.beta.threads.messages.list(thread_id=thread_id_answers_demo)
    messages = messages_response.data
    response_message = messages[0].content[0].text.value

    # add messages to the mangodb.
    collection.update_one(
        {"thread_id_answers_demo": thread_id_answers_demo},
        {"$push": {"messages": {"role": "assistant", "content": response_message}}}
    )

    return response_message


# 创建新对话
thread_id_question_preprocess, thread_id_answers_demo = create_new_conversation()
print(f"New conversation started with threads: {thread_id_question_preprocess}, {thread_id_answers_demo}")

# 上传文件到新对话
directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
file_ids, file_flag = upload_files(thread_id_question_preprocess, directory_path)

# 继续当前对话
user_message = "I am an international student and my visa is due soon, I am wondering how long can I stay in the US legally?"
response = continue_conversation(thread_id_question_preprocess, thread_id_answers_demo, user_message)
print(f"Assistant response: {response}")
