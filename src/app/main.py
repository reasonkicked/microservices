# src/app/main.py:

from flask import Flask, jsonify, request

from app.invalid_usage import InvalidUsage
from app.validation import validate_greeting

from mypkg import say_hello_to

app = Flask(__name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
   response = jsonify(error.to_dict())
   response.status_code = error.status_code
   return response


@app.route("/hello", methods=['POST'])
def hello() -> str:
   errors = validate_greeting(request)
   if errors is not None:
       print(errors)
       raise InvalidUsage(errors)
   greetee = request.json.get("greetee", None)
   response = {"message": say_hello_to(greetee)}
   return jsonify(response)


@app.route("/")
def index() -> str:
    # transform a dict into an application/json response
    return jsonify({"message": "It Works"})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)