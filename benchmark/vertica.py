import vertica_python
import time

# 04a55132a4fc
connection_info = {
    'host': '158.160.12.121',
    'port': 5433,
    'user': 'dbadmin',
    'password': '',
    'database': 'docker',
    'autocommit': True,
} 


with vertica_python.connect(**connection_info) as connection:   
    cursor = connection.cursor() 
    cursor.execute("""
    CREATE TABLE test_vertica(
        id IDENTITY,
        date_time DateTime,
        name VARCHAR(1000) NULL,
        number_ch INT DEFAULT 0
    );""") 
    print(cursor)


def ex_vertica(ex):
    try:
        t = 0.1
        for _ in range(100):
            try:
                with vertica_python.connect(**connection_info) as connection: 
                    cursor = connection.cursor() 
                    data = cursor.execute(ex)
                    return data.fetchall()
            except vertica_python.errors.ConnectionError:
                time.sleep(t)
                if t < 10:
                    t *= 2
        return False
    except Exception:
        return False


def insert_vertica(ins, data):
    try:
        t = 0.1
        for _ in range(100):
            try:
                with vertica_python.connect(**connection_info) as connection: 
                    cursor = connection.cursor() 
                    cursor.executemany(ins, data)
                return True
            except vertica_python.errors.ConnectionError:
                time.sleep(t)
                if t < 10:
                    t *= 2
        return False
    except Exception:
        return False
