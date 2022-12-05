import clickhouse_driver
import time


db = clickhouse_driver.Client(host='127.0.0.1',port='9000')

def ex_ch(select):
    try:
        t = 0.1
        for _ in range(100):
            try:
                result = db.execute(select)
                return result
            except clickhouse_driver.errors.SocketTimeoutError:
                time.sleep(t)
                if t < 10:
                    t*=2
        return False
    except Exception:
        return False

def insert_ch(ins, data):
    try:
        t = 0.1
        for _ in range(100):
            try:
                db.execute(ins, data)
                return True
            except clickhouse_driver.errors.SocketTimeoutError:
                time.sleep(t)
                if t < 10:
                    t*=2
        return False
    except Exception:
        return False

