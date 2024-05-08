from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()  # Load environment variables from a .env file
app = Flask(__name__)
CORS(app)  # Allows all origins, for development purposes only

client = OpenAI(
    api_key= 'OUR API HERE'
)


@app.route('/askQuestion', methods=['POST'])
def ask_question():
    try:
        data = request.json
        question = data['question']

        # OpenAI thread and message creation example
        Thread_Question_Preprocess = client.beta.threads.create()
        # thread = openai.Thread.create()
        message = client.beta.threads.messages.create(
            thread_id=Thread_Question_Preprocess.id,
            role="user",
            content="I have an asylum statement. Please give me a summary and list the characters in this statement, including their name, age and relationship. " + question,
            # file_ids = [file.id], #remove when needed
        )
        print(message.content)
        print("question preprocessing layer demo")
   
        run = client.beta.threads.runs.create(
            thread_id=Thread_Question_Preprocess.id,
            assistant_id="asst_H45C7dVAP6ltH8wCMXDDg2cj", 
        )

        print(f"Running{run.id}")
        while run.status != "completed":
            run =  client.beta.threads.runs.retrieve(thread_id=Thread_Question_Preprocess.id,run_id=run.id)
            print("Status: ",run.status)
            time.sleep(1)
        else:
            print("Completed")
        messages_response = client.beta.threads.messages.list(
            thread_id=Thread_Question_Preprocess.id
        )
        # messages = messages_response.data
        messages = messages_response.data
        Preprocessed_question = messages[0].content[0].text.value
        responses = [msg for msg in messages_response.data]
        print("All assistant responses:", responses)

        Thread_Answers_demo = client.beta.threads.create()
        print("Answer generate layer demo")
        message = client.beta.threads.messages.create(
            thread_id=Thread_Answers_demo.id,
            role="user",
            content= Preprocessed_question
        )

        run = client.beta.threads.runs.create(
            thread_id=Thread_Answers_demo.id,
            assistant_id="asst_c8wI5kjTBL0YSNJuQfErp1s3", #assistant v2 turbo
        )

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
        # Preprocessed_question = messages[0].content[0].text.value
        # print(f"question preprocess: {messages[0].content[0].text}")

        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=question,
        #     max_tokens=150
        # )
        # answer = response.choices[0].text.strip()

        return jsonify({messages[0].content[0].text.value})
    except Exception as e:
        print(e)
        return jsonify({"error": "Error processing your request"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
