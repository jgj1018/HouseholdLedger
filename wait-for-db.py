import psycopg2


def connect():
    try:
        conn = psycopg2.connect("dbname='django' user='django' host='db' password='password'")
        return conn
    except Exception:
        return False


while not connect():
    connect()