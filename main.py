import psycopg2
import json

if __name__ == '__main__':
    with open('configClear_2.json') as f:
        data = json.load(f)