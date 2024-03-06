from flask import Flask
from flask import request
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import time

app = Flask(__name__)
CORS(app)

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/askQuestion', methods=['POST'])
def ask_question():
    question_content = request.json.get('question')
    Thread_Question_Preprocess = client.beta.threads.create()

    print("Question preprocessing layer demo")
    message = client.beta.threads.messages.create(
        thread_id=Thread_Question_Preprocess.id,
        role="user",
        content=question_content #the question content input
    )

    run = client.beta.threads.runs.create(
        thread_id=Thread_Question_Preprocess.id,
        assistant_id="asst_zx9qHxvw2vR16yp1X3m4wWnz", 
    )

    # Running status:
    print(f"Running {run.id}")
    while run.status != "completed":
        run =  client.beta.threads.runs.retrieve(thread_id=Thread_Question_Preprocess.id,run_id=run.id)
        print("Status: ", run.status)
        time.sleep(1)
    else:
        print("Completed")

    messages_response = client.beta.threads.messages.list(
        thread_id=Thread_Question_Preprocess.id
    )
    messages = messages_response.data
    Preprocessed_question = messages[0].content[0].text.value
    print(f"Question preprocess: {messages[0].content[0].text.value}")

    # Phase 2: take the processed user answer as the input of the 2nd assistant
    Thread_Answers_demo = client.beta.threads.create()

    print("Answer generate layer demo")
    message = client.beta.threads.messages.create(
        thread_id=Thread_Answers_demo.id,
        role="user",
        content=Preprocessed_question
    )

    run = client.beta.threads.runs.create(
        thread_id=Thread_Answers_demo.id,
        assistant_id="asst_h2wyE1flbMWT3PzL42MQDNc5", 
    )

    # Running status:
    print(f"Running {run.id}")
    while run.status != "completed":
        run =  client.beta.threads.runs.retrieve(thread_id=Thread_Answers_demo.id,run_id=run.id)
        print("Status: ", run.status)
        time.sleep(1)
    else:
        print("Completed")

    messages_response = client.beta.threads.messages.list(
        thread_id=Thread_Answers_demo.id
    )
    messages = messages_response.data
    print(f"Answer preprocess: {messages[0].content[0].text.value}")
    
    # You can return the answer or perform further processing here
    return f"Answer preprocess: {messages[0].content[0].text.value}"

if __name__ == '__main__':
    app.run(debug=True)
