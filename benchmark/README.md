benchmark для двух баз данных clickhous и vertica

В процессе тестирования генерятся данные по 1000 штук и загружается в базу, все это повторяется 10000000 раз, так же эмитируется запрос данных обычный select из таблицы 100 строк с сортировкой по дате.

После поднятия базы clickhous:
1) Создаем базу :
<CREATE DATABASE benchmark;>

2) Создаем таблицу:
<create table benchmark.test_ch(
        date_time      DateTime,        
        name     VARCHAR(1000) NULL,
        number_ch       INT(1000000) DEFAULT 0) 
ENGINE = MergeTree() 
ORDER BY (date_time);>

После поднятия базы vertica:

1) Создаем таблицу 

<CREATE TABLE test_vertica(
        id IDENTITY,
        date_time DateTime,
        name VARCHAR(1000) NULL,
        number_ch INT DEFAULT 0);>

Что бы выполнить тест, необходимо запустить файл start_test.py, после чего выбрать необходимую базу для теста.
Результат будет записан в файле рядом, а так же появится в консоли

Результат загрузки 10 000 000 строк в БД:

 - vertica - 3 часа
 - clickhous - 5 часов

