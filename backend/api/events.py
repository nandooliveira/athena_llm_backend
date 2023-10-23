from bson.json_util import dumps
from flask import make_response
from flask_restful import Resource, reqparse

from atena.repositories.events_repository import EventsRepository

parser = reqparse.RequestParser()
parser.add_argument('currentSession', type=str, help='Session Name')
parser.add_argument('type', type=str, help='Type of Event')
parser.add_argument('createdAt', type=int, help='Created Timestamp')
parser.add_argument('data', type=dict, help='Data of Event')


class Events(Resource):
    def __init__(self, repository=EventsRepository):
        self.repository = repository

    def get(self):
        events = self.repository.all()
        response = make_response(dumps(events), 200)
        response.mimetype = 'application/json'

        return response

    def post(self):
        args = parser.parse_args()
        print(args)
        self.repository.create(args)

        return {"status": "Success", "message": "Event successfully created"}


class Event(Resource):
    def __init__(self, repository=EventsRepository):
        self.repository = repository

    def get(self, event_id):
        event = self.repository.find_by_id(event_id)
        response = make_response(dumps(event), 200)
        response.mimetype = 'application/json'

        return response
