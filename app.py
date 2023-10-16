from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api

from api.events import Events, Event

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
api = Api(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


api.add_resource(Events, '/api/v1/events')
api.add_resource(Event, '/api/v1/events/<string:event_id>')
