import json


def append():
    value = input("json file input value")
    new_record = {"value": value}
    r = json.dumps(new_record)
    with open('append.json', mode='w', encoding='utf-8') as jsonfile:
        jsonfile.write(r)
        jsonfile.close()


if __name__ == '__main__':
    append()
