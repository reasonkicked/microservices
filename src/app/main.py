# src/app/main.py:

from flask import Flask, jsonify, request
from mypkg import say_hello_to

app = Flask(__name__)


@app.route("/hello", methods=['POST'])
def hello() -> str:
    greetee = request.json.get("greetee", None)
    response = {"message": say_hello_to(greetee)}
    return jsonify(response)


@app.route("/")
def index() -> str:
    # transform a dict into an application/json response
    return jsonify({"message": "It Works"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)