from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello This is Flask speaking!</h1>'


app.run()