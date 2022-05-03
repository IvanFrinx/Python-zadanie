import psycopg2
import json

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data  


class interface:
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    data = load_json('configClear_v2.json')
    for i in data['frinx-uniconfig-topology:configuration']["openconfig-interfaces:interfaces"]["interface"]:
        interf = interface(i["name"])
        print(interf.name)

