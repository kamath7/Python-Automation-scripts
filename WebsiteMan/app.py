from flask import Flask 

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello there 🖐"

@app.route("/favMovies")
def favMovies():
    return "The Dark Knight"


app.run(host='0.0.0.0')