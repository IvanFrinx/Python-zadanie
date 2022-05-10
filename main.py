import jsondata
import commandsSQL


if __name__ == '__main__':
    # Load json file, convert to dict type and store in data
    data = jsondata.load_json('configClear_v2.json')

    # Access to needed data and creation of an objects for each interface
    objects = jsondata.extract_data(data)

    # Connection to the postgres database using Psycopg2 library
    connection, cursor = commandsSQL.connect_to_db()

    # Creation of the table named interfaces in the database
    commandsSQL.create_table( cursor)

    # Parsing data into created table
    commandsSQL.parse_data(objects, cursor)

    # Getting ids from Port_channels
    ports_id = commandsSQL.get_port_ids(cursor)
    
    # Links port ids with interfaces
    links = jsondata.link_ports(objects, ports_id)
    
    # Updating port_channel_id column
    commandsSQL.update_col_port(cursor, links)

    # Closing connection to database
    commandsSQL.close_connection(connection, cursor)
