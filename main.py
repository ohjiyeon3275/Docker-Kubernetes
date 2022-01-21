import json
from flask import Flask

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333')
    append()
