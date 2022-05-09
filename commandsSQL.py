import psycopg2
import database_scripts


def connect_to_db():
    connection= psycopg2.connect(**database_scripts.db)
    cursor = connection.cursor()
    return connection, cursor


def create_table(connection, cursor):
    cursor.execute(database_scripts.create_table_string)
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
        cursor.execute(database_scripts.insert_into_tables_values, obj.attributes())
    connection.commit()

def get_port_ids(cursor):
    cursor.execute(database_scripts.get_port_ids_str)
    ids = cursor.fetchall()
    ids_dict = dict()
    for i in ids:
        ids_dict[int(i[1].lstrip('Port-channel'))] = i[0]
    return ids_dict
         

def update_col_port(connection, cursor, links):
    for link, port in links.items():
        cursor.execute(database_scripts.udpate_port_channel_id, (port, link)) 
    connection.commit()
