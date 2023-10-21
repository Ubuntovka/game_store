import os
from flask import Flask, Response, request, jsonify
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
import json

load_dotenv()

app = Flask(__name__)
mongo_db_url = os.environ.get("MONGODB_URI")

client = MongoClient(mongo_db_url)
db = client.get_database('game')
user_collection = pymongo.collection.Collection(db, 'game')


@app.route("/api/games")
def get_sensors():
    games = list(user_collection.find().limit(11))

    response = Response(
        response=dumps(games), status=200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(debug=True)
