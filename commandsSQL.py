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


insert_into_tables_values = 'INSERT INTO interfaces ' \
                            '(name, description, config, max_frame_size) VALUES (%s, %s, %s, %s)'


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


# To include BDIs and Loopbacks remove if statment (line 48) and back-tab line 49


def parse_data(objects, connection, cursor):
    for obj in objects:
        if 'BDI' not in obj.name and 'Loopback' not in obj.name:  # <=== Optional
            cursor.execute(insert_into_tables_values, obj.attributes())
    connection.commit()
