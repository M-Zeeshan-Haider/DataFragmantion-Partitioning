# Python 3.5
# Connecting to PostgreSQL database from python 

# importing psycopg2 module
import psycopg2

try:
    conn = psycopg2.connect("dbname='distDatabase' user='postgres' host='localhost' password='Zhaider366!'")
    cur = conn.cursor()
    # Let's fetch 5 rows from test table
    cur.execute("SELECT * FROM test LIMIT 5;")
except Exception as ex:
    print("Error: unable to connect to the database",ex )