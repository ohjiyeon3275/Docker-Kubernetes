import json
import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("localhost", int("27017"))
db = client['test']
collection = db['user']

@app.route("/append/<value>")
def append(value):
    new_record = {"value": value}
    r = json.dumps(new_record)
    with open('append.json', mode='w', encoding='utf-8') as jsonfile:
        jsonfile.write(r)
        jsonfile.close()
    return "append success!"


@app.route("/value")
def read_value():
    with open('append.json', mode='r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        value = data["value"]
        jsonfile.close()
    return "value is " + value


@app.route("/find/<book>")
def find_name_from_mongodb(book):
    result = collection.find({"book": book})
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3333))
    append()
