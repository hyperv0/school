from flask import Flask

app = Flask(__name__)

@app.route("/")
def display():
    #txt = input('Text: ')
    return f'you are bhavya'

app.run(host='0.0.0.0', port='5120')