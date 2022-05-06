import jsondata
import commandsSQL

frinx = 'frinx-uniconfig-topology:configuration'


if __name__ == '__main__':
    data = jsondata.load_json('configClear_v2.json')
    objects = jsondata.extract_data(data)
    commandsSQL.magic_sql(objects)
