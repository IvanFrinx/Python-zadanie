# Python-zadanie
Python script and PostgreSQL

1. Open terminal and navigate to project folder
2. pip3 install -r requirements.txt
3. docker-compose up
4. python3 main.py

Check database:
1. docker exec -it pythonzadanie_db_1 bash
2. psql -h localhost -p 5432 -U postgres
3. Enter password: postgres
4. SELECT * FROM interfaces;

Ivan Hrubik
