from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World!"

@app.route("/teste")
def teste():
    return "teste update de novo"

#teste de login