# from email import message
import flask
from flask_pymongo import PyMongo
from flask import Flask, jsonify

app = Flask(__name__)

# try: 
#     mongo =  PyMongo.MongoClient(
#         host = "localhost",
#         port = 27017,
#         serverSelectionTimeoutMS = 1000
#     )
#     mongo.server_info() #trigger exception if cannot connect to db
#     db = mongo.pytestdb
# except: 
#     print("ERROR - CANNOT CONNECT TO DB")


mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/pytestdb")
db = mongodb_client.db

@app.route('/')
def index():
    return "Running Rest API"

# get data
@app.route('/get_data')
def get_data():
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])

# insert one
@app.route("/add_one")
def add_one(body):
    db.todos.insert_one(body)
    return flask.jsonify(message="succcess")

# insert many
@app.route("/add_many")
def add_many(body):
    db.todos.insert_many(body)
    return flask.jsonify(message="success")

if __name__ == "__main__":
    app.run(port=122, debug=True)
