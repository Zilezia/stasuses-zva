from flask import Flask, render_template, request, abort
from flask_restful import Api, Resource
import subprocess
import threading
import sys
import os
from functools import wraps

from reador.config import *

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

def run_discord_bot():
    script_path = os.path.join(os.path.dirname(__file__), 'reador', 'bot.py')
    subprocess.run([sys.executable, script_path], capture_output=True, text=True, check=True)

def start_discord_bot_thread():
    thread = threading.Thread(target=run_discord_bot)
    thread.start()

if __name__ == "__main__":
    start_discord_bot_thread()
    app.run(debug=False)
    # app.run(debug=True)