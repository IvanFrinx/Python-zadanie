db = {'host': 'localhost',
      'dbname': 'postgres',
      'password': 'postgres',
      'user': 'postgres',
      'port': 5432}


create_table_string = """CREATE TABLE IF NOT EXISTS interfaces(
                                id SERIAL PRIMARY KEY,
                                connection INTEGER,
                                name VARCHAR(255) NOT NULL,
                                description VARCHAR(255),
                                config json,
                                type VARCHAR(50),
                                infra_type VARCHAR(50),
                                port_channel_id INTEGER,
                                max_frame_size INTEGER)"""


insert_into_tables_values = """INSERT INTO interfaces
                               (name, description, config, max_frame_size)
                               VALUES (%s, %s, %s, %s)"""


get_port_ids_str = """SELECT id, name
                       FROM interfaces
                       WHERE name
                       LIKE 'Port-channel%'"""


update_port_channel_id = """UPDATE interfaces
                            SET port_channel_id=%s
                            WHERE name=%s"""
