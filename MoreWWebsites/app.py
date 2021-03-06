from flask import Flask, render_template, request
import outcome

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def homePostMethod():
    length = request.form['length']
    breadth = request.form['breadth']
    height = request.form['height']

    vol = float(length) * float(breadth) * float(height)

    return render_template('index.html', output=vol, length=length, breadth=breadth, height=height)


app.run("0.0.0.0")
