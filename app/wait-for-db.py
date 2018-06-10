import psycopg2
import time

def connect():
    try:
        conn = psycopg2.connect("dbname='django' user='django' host='db' password='password'")
        return conn
    except Exception:
        time.sleep(2)
        return False


while not connect():
    connect()