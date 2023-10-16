import pymongo


class Repository:
    DATABASE_URL = f"mongodb://localhost:27017/atena_db"
    __mongo_db = None

    @staticmethod
    def connection():
        if Repository.__mongo_db is None:
            client = pymongo.MongoClient(Repository.DATABASE_URL)
            Repository.__mongo_db = client.db

        return Repository.__mongo_db
