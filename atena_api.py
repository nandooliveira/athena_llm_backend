import pymongo
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
# DATABASE_URL=f'mongodb+srv://user:{os.environ.get("password")}'\
# 	      '@127.0.0.1/atena_db?'\
#   'retryWrites=true&w=majority' # get connection url from environment

DATABASE_URL = f"mongodb://localhost:27017/atena_db"

client = pymongo.MongoClient(DATABASE_URL)  # establish connection with database
mongo_db = client.db

app = Flask(__name__)


@app.route("/api/v1/events", methods=["GET", "POST"])
def events():
    if request.method == 'POST':
        mongo_db.events.insert_one(request.json)
        return jsonify({"message": "Document inserted successfully"})

    response = app.response_class(
        response=dumps(mongo_db.events.find()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/api/v1/events/<string:document_id>", methods=["GET"])
def event(document_id):
    object_id = ObjectId(str(document_id))
    result = mongo_db.events.find_one({"_id": object_id})
    response = app.response_class(
        response=dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
