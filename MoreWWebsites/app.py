from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def homePostMethod():
    return render_template('index.html')


app.run("0.0.0.0")