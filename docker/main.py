import psycopg2
import json

db = {"host": 'db',
      "dbname": 'postgres',
      "password": 'postgres',
      "user": 'postgres',
      "port": 5432}


def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data


class interface:
    def __init__(self, name, config, description, mtu):
        self.name = name
        self.config = config
        self.description = description
        self.mtu = mtu

    def attributes(self):
        return self.name, self.config, self.description, self.mtu


frinx = 'frinx-uniconfig-topology:configuration'
interfaces = "openconfig-interfaces:interfaces"

if __name__ == '__main__':
    data = load_json('configClear_v2.json')
    objects = list()
    # for i in data[frinx]['Cisco-IOS-XE-native:native']['interface']:
    #     for i in data[frinx]['Cisco-IOS-XE-native:native']['interface'][i]:
    #         if 'Cisco-IOS-XE-ethernet:channel-group' in i.keys():
    #             print(i['Cisco-IOS-XE-ethernet:channel-group'])

    for i in data[frinx][interfaces]['interface']:
        if 'Loopback' not in i['name']:
            if 'description' not in i['config'].keys():
                i['config']['description'] = None
            if 'mtu' not in i['config'].keys():
                i['config']['mtu'] = None
            interf = interface(i["name"], json.dumps(i["config"]), i['config']['description'],i['config']['mtu'])
            print(interf.name)
            print(interf.config)
            print(interf.description)
            print(interf.mtu)
            print()
            objects.append(interf)

    connection = psycopg2.connect(**db)
    cursor = connection.cursor()
    print('point1')

    create_table = ''' CREATE TABLE IF NOT EXISTS interfaces (
                            id SERIAL PRIMARY KEY,
                            connection INTEGER,
                            name VARCHAR(255) NOT NULL,
                            description VARCHAR(255),
                            config json,
                            type VARCHAR(50),
                            infra_type VARCHAR(50),
                            port_channel_id INTEGER,
                            max_frame_size INTEGER) '''

    cursor.execute(create_table)

    insert_into_tables_values = 'INSERT INTO interfaces (name, config, description, mtu) VALUES (%s, %s, %s, %s)'

    for obj in objects:
        cursor.execute(insert_into_tables_values, (obj.name, obj.config, obj.description, obj.mtu))

    connection.commit()
    cursor.close()
    connection.close()
