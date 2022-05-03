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
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    data = load_json('configClear_v2.json')
    objects = list()
    for i in data['frinx-uniconfig-topology:configuration']["openconfig-interfaces:interfaces"]["interface"]:
        interf = interface(i["name"])
        print(interf.name)
        objects.append(interf)

    connection = psycopg2.connect(**db)
    cursor = connection.cursor()

    create_table = ''' CREATE TABLE IF NOT EXISTS interfaces (
                            id SERIAL PRIMARY KEY,
                            connection INTEGER,
                            name VARCHAR(255) NOT NULL,
                            description VARCHAR(255),
                            config json,
                            type VARCHAR(50),
                            infra_type VARCHAR(50),
                            port_channel_id INTEGER,
                            max_frame_size INTEGER '''

    cursor.execute(create_table)

    insert_into_tables_values = 'INSERT INTO interfaces (name) VALUES (%s)'

    for obj in objects:
        cursor.execute(insert_into_tables_values, (obj.name))

    connection.commit()
    cursor.close()
    connection.close()    

