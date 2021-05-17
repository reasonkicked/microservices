# src/app/validation.py

from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

# https://pythonhosted.org/Flask-Inputs/#module-flask_inputs
# https://json-schema.org/understanding-json-schema/
# we want an object containing a required greetee  string value
greeting_schema = {
   'type': 'object',
   'properties': {
       'greetee': {
           'type': 'string',
       }
   },
   'required': ['greetee']
}


class GreetingInputs(Inputs):
   json = [JsonSchema(schema=greeting_schema)]


def validate_greeting(request):
   inputs = GreetingInputs(request)
   if inputs.validate():
       return None
   else:
       return inputs.errors