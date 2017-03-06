from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/new_question")
def new_question():
    return render_template('question.html',question="What's in a name?")

@app.route("/verify_answer", methods=['POST', 'GET'])
def verify_answer():
    answer = request.get_json()
    print answer['answer']
    if answer['answer'] == 'Nothing':
        return "Corrrrect"
    else:
        return "Faaaaaillll"

if __name__ == "__main__":
    app.run()
