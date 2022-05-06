import jsondata
import commandsSQL


if __name__ == '__main__':
    data = jsondata.load_json('configClear_v2.json')
    objects = jsondata.extract_data()
    for i in objects:
        print(i.attributes())
    commandsSQL.magic_sql(objects)
