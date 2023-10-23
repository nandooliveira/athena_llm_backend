from atena.repositories.repository import Repository
from bson import ObjectId


class EventsRepository(Repository):
    @staticmethod
    def create(event):
        return Repository.connection().events.insert_one(event)

    @staticmethod
    def all():
        return Repository.connection().events.find()

    @staticmethod
    def find_by_id(event_id):
        return Repository.connection().events.find_one({"_id": ObjectId(event_id)})
