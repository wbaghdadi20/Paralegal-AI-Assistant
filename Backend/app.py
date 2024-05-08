from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os
import time

load_dotenv()  # Load environment variables from a .env file
app = Flask(__name__)
CORS(app)  # Allows all origins, for development purposes only


client = OpenAI(
    api_key= 'API HERE'
)


@app.route('/askQuestion', methods=['POST'])
def ask_question():
    filess = []
    file_flag = 0
    try:
        # data = request.json
        # question = data['question']
        print("Content_type is: :", request.content_type)
        if request.content_type.startswith('multipart/form-data'):
            print("In the file branch")
            file = request.files.get('file')
            text_query = request.form.get('query', '')
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join('/Users/jinduoguo/Desktop/Backend', filename)
                file.save(file_path)
            # Optionally, read the file and include its content in the GPT request
            # with open(file_path, 'rb') as file:
            #     file_content = file.read()
                file_uploaded = client.files.create(
                    file=open(file_path, "rb"),
                    purpose="user_data"
                )
                filess.append(file_uploaded.id)
                file_flag = 1
        else:
            print("In the else branch")
            data = request.json
            question = data['question']
            file_flag = 0
        Thread_Question_Preprocess = client.beta.threads.create()

        if(file_flag == 1):
            print("File_flag = 1, and prompt message is: ", text_query)
            message = client.beta.threads.messages.create(
                thread_id=Thread_Question_Preprocess.id,
                role="user",
                content=" "+text_query,
            )
        else:
            message = client.beta.threads.messages.create(
                thread_id=Thread_Question_Preprocess.id,
                role="user",
                content=question,
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
        # print("All assistant responses:", responses)

        Thread_Answers_demo = client.beta.threads.create()
        print("Answer generate layer demo")


        if file_flag == 1:
            print(filename)
            print(filess)

            message = client.beta.threads.messages.create(
                thread_id=Thread_Answers_demo.id,
                role="user",
                content=Preprocessed_question,
                # file_id=filess,  # Attach files only if the file_flag is set to 1
                # "attachments": [
                #     { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
                # ],
                attachments=[
                    {"file_id": filess[0], "tools": [{"type": "file_search"}]}
                ]
            )
        else:
            message = client.beta.threads.messages.create(
                thread_id=Thread_Answers_demo.id,
                role="user",
                content=Preprocessed_question,
                # No files attached if the flag is not set
            )


        # message = client.beta.threads.messages.create(
        #     thread_id=Thread_Answers_demo.id,
        #     role="user",
        #     content= Preprocessed_question
        # )
        print(message)

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
        return (messages[0].content[0].text.value)
    except Exception as e:
        print(e)
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "Error processing your request"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
