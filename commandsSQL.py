import psycopg2

db = {"host": 'localhost',
      "dbname": 'postgres',
      "password": 'postgres',
      "user": 'postgres',
      "port": 5432}

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

insert_into_tables_values = 'INSERT INTO interfaces ' \
                            '(name, description, config, max_frame_size) VALUES (%s, %s, %s, %s)'

# Remove if statment to include BDIs and Loopbacks

def magic_sql(objects):
    connection = psycopg2.connect(**db)
    cursor = connection.cursor()
    cursor.execute(create_table)
    for obj in objects:
        if 'BDI' not in obj.name and 'Loopback' not in obj.name: # Remove if statment to include
            cursor.execute(insert_into_tables_values, obj.attributes())
    connection.commit()
    cursor.close()
    connection.close()
