import jsondata
import commandsSQL


if __name__ == '__main__':
    data = jsondata.load_json('configClear_v2.json')
    objects = jsondata.extract_data(data)
    for i in objects:
        print(i.name, i.description)
    #commandsSQL.magic_sql(objects)
