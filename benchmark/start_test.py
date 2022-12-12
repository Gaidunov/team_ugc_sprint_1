from multiprocessing import Process
import time
import random
from faker import Faker

from clickhouse import ex_ch, insert_ch
from vertica import ex_vertica, insert_vertica


fake = Faker()


def unloading(flag_db: int):
    print('старт выгрузки')
    for _ in range(10000):
        match flag_db:
            case 1:
                data = ex_ch('SELECT * from benchmark.test_ch limit 100')
                with open('data_ch.txt', 'a') as q:
                    q.write(str(data))
            case 2:
                data = ex_vertica('SELECT * from test_vertica limit 100')
                with open('data_vertica.txt', 'a') as q:
                    q.write(str(data))
        time.sleep(1)


def one_thousand_data():
    data = []
    for _ in range(1000):
        data.append((fake.date_time(), fake.name(), random.randint(1, 1000000000)))
    return data


start_time = time.time()
print(start_time)


def load(flag_db: int):
    print('старт загрузки')
    for _ in range(10000):
        data = one_thousand_data()
        match flag_db:
            case 1:
                if not insert_ch(f"INSERT INTO benchmark.test_ch VALUES", data):
                    print('ошибка записи')
            case 2:
                if not insert_vertica(f"INSERT INTO test_vertica(date_time, name, number_ch) VALUES (%s, %s, %s)", data):
                    print('ошибка записи')
        print('загружено раз: ', _)
    match flag_db:
            case 1:
                with open('result_ch.txt', 'w') as f:
                    f.write("--- %s seconds ---" % (time.time() - start_time))
            case 2:
                with open('result_vertica.txt', 'w') as f:
                    f.write("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    print('базу тестируем \n 1) clickhouse \n 2) vertica')
    while True:
        flag_db = int(input('введите номер: '))
        if flag_db == 1 or flag_db == 2:
            break
    t = Process(target=load, args=(flag_db,))
    t.start()

    w = Process(target=unloading, args=(flag_db,))
    w.start()
