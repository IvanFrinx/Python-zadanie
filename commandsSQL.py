import psycopg2


db = {"host": 'localhost',
      "dbname": 'postgres',
      "password": 'postgres',
      "user": 'postgres',
      "port": 5432}


create_table_string = ''' CREATE TABLE IF NOT EXISTS interfaces (
                                id SERIAL PRIMARY KEY,
                                connection INTEGER,
                                name VARCHAR(255) NOT NULL,
                                description VARCHAR(255),
                                config json,
                                type VARCHAR(50),
                                infra_type VARCHAR(50),
                                port_channel_id INTEGER,
                                max_frame_size INTEGER) '''


insert_into_tables_values = '''INSERT INTO interfaces
                               (name, description, config, max_frame_size)
                               VALUES (%s, %s, %s, %s)'''


get_port_ids_str =  """SELECT id, name 
                       FROM interfaces 
                       WHERE name 
                       LIKE 'Port-channel%'"""    


udpate_port_channel_id = """UPDATE interfaces
                            SET port_channel_id=%s 
                            WHERE name=%s"""                               


def connect_to_db():
    connection= psycopg2.connect(**db)
    cursor = connection.cursor()
    return connection, cursor


def create_table(connection, cursor):
    cursor.execute(create_table_string)
    connection.commit()


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def skip_BDI_and_Loops(objects):
    objs = list()
    for obj in objects:
        if 'Loopback' not in obj.name and "BDI" not in obj.name:
            objs.append(obj)
    return objs        



def parse_data(objects, connection, cursor):
    objects = skip_BDI_and_Loops(objects) # <== Comment line to include Loobacks and BDIs 
    for obj in objects:
        cursor.execute(insert_into_tables_values, obj.attributes())
    connection.commit()

def get_port_ids(cursor):
    cursor.execute(get_port_ids_str)
    ids = cursor.fetchall()
    ids_dict = dict()
    for i in ids:
        ids_dict[int(i[1].lstrip('Port-channel'))] = i[0]
    return ids_dict
         

def update_col_port(connection, cursor, links):
    for link, port in links.items():
        cursor.execute(udpate_port_channel_id, (port, link)) 
    connection.commit()
