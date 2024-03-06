#2024/3/3 presentation version
from openai import OpenAI
client = OpenAI(
    api_key= ''
)
Thread_Question_Preprocess = client.beta.threads.create()
import time

print("question preprocessing layer demo")
message = client.beta.threads.messages.create(
    thread_id=Thread_Question_Preprocess.id,
    role="user",
    content="how do I finish applying for h1b visa" #the question content input
)

run = client.beta.threads.runs.create(
thread_id=Thread_Question_Preprocess.id,
assistant_id="asst_zx9qHxvw2vR16yp1X3m4wWnz", 
)
# Creating a run with the thread and assistant
# Running status:
print(f"Running{run.id}")
while run.status != "completed":
    run =  client.beta.threads.runs.retrieve(thread_id=Thread_Question_Preprocess.id,run_id=run.id)
    print("Status: ",run.status)
    time.sleep(1)
else:
    print("Completed")
messages_response = client.beta.threads.messages.list(
  thread_id=Thread_Question_Preprocess .id
)
messages = messages_response.data
Preprocessed_question = messages[0].content[0].text.value
print(f"question preprocess: {messages[0].content[0].text.value}")
#phase 2 take the processed user answer as the input of the 2nd assistant
Thread_Answers_demo = client.beta.threads.create()

print("Answer generate layer demo")
message = client.beta.threads.messages.create(
    thread_id=Thread_Answers_demo.id,
    role="user",
    content= Preprocessed_question
)

run = client.beta.threads.runs.create(
thread_id=Thread_Answers_demo.id,
assistant_id="asst_h2wyE1flbMWT3PzL42MQDNc5", 
)
# Creating a new run with the thread and assistant
# Running status:
print(f"Running{run.id}")
while run.status != "completed":
    run =  client.beta.threads.runs.retrieve(thread_id=Thread_Answers_demo.id,run_id=run.id)
    print("Status: ",run.status)
    time.sleep(1)
else:
    print("Completed")
messages_response = client.beta.threads.messages.list(
  thread_id=Thread_Answers_demo.id
)
messages = messages_response.data
print(f"Answer preprocess: {messages[0].content[0].text.value}")
# print the 
