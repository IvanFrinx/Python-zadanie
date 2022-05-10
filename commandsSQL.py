import sys
import psycopg2
import database_scripts


def connect_to_db():
    try:
        connection = psycopg2.connect(**database_scripts.db)
        cursor = connection.cursor()
    except ValueError as e:
        print('Unable to connect!', {e})
        sys.exit(1)
    else:
        print('Connected!')
        return connection, cursor


def create_table(cursor):
    cursor.execute(database_scripts.create_table_string)


def close_connection(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()


def skip_bdi_and_loops(objects):
    objs = list()
    for obj in objects:
        if 'Loopback' not in obj.name and 'BDI' not in obj.name:
            objs.append(obj)
    return objs

# Comment line 34 to include Loopbacks and BDIs


def parse_data(objects, cursor):
    objects = skip_bdi_and_loops(objects)
    for obj in objects:
        cursor.execute(database_scripts.insert_into_tables_values,
                       obj.attributes())


def get_port_ids(cursor):
    cursor.execute(database_scripts.get_port_ids_str)
    ids = cursor.fetchall()
    ids_dict = dict()
    for i in ids:
        ids_dict[int(i[1].lstrip('Port-channel'))] = i[0]
    return ids_dict


def update_col_port(cursor, links):
    for link, port in links.items():
        cursor.execute(database_scripts.update_port_channel_id, (port, link))
