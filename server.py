from flask import Flask, render_template, request, abort
from flask_restful import Api, Resource
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

AUTH = os.getenv('AUTH')
AUTH_KEY = os.getenv('AUTH_KEY')
TABLE = os.getenv('TABLE')

app = Flask(__name__)
api = Api(app)

data = {}

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get(AUTH)
        if api_key != AUTH_KEY: abort(403)
        return f(*args, **kwargs)
    return decorated_function

class DataReceiver(Resource):
    @require_auth
    def post(self):
        global data
        if not request.json: abort(400)
        received_data = request.get_json()
        if TABLE not in received_data or not isinstance(received_data[TABLE], list): abort(400)
        data = received_data

@app.route('/')
def index():
    return render_template('statuses.html', data=data, table=TABLE)

api.add_resource(DataReceiver, '/'+AUTH)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True)