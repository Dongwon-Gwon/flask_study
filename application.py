from flask import Flask, render_template, make_response, request
import sys
from flask.json import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("hello.html", value="home")

@app.route('/api', methods=["GET"])
def hello_world():
    return make_response(jsonify({"id":"1","name":"dongwon"}),200)

@app.route('/home')
def home():
    return "hello home"

@app.route('/test', methods=["POST"])
def test():
    json_file = request.json
    print(json_file)
    return "123", 200

if __name__=="__main__":
    app.run()