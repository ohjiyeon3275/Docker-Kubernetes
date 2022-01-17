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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333')
    append()
