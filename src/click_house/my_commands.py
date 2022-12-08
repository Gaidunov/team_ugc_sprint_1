# click_client.
# click_client.init_db()
# client = Client(host='localhost')

# client = Client(host='localhost')
# print(client.execute('select * from my_database.users_views '))


#     def add(self):
#         for k, v in self.kafka_consumer.fetch():
#             self.client.execute(f"INSERT INTO my_database.test_table (id, some_val) VALUES ('{k}', '{v}')") 
#             # print(self.client.execute('SHOW DATABASES'))

#     def create_db():
#         ...

# # click_client = ClickHouseClient()
# # click_client.add()

# client = Client(host='localhost')

# client.execute('CREATE DATABASE IF NOT EXISTS my_database ON CLUSTER company_cluster')

# client.execute('CREATE TABLE if not exists my_database.movies_n_time ON CLUSTER company_cluster (id String, title String, timestamp Int64) Engine=MergeTree() ORDER BY id')


# client.execute("INSERT INTO my_database.movies_n_time (id, title, timestamp)  Values ('mid_1', 'классный фильм', 15123 )  ")



# client.execute('CREATE TABLE my_database.users_views ON CLUSTER company_cluster (id String, uid String, movie_id String, timestamp Int64) Engine=MergeTree() ORDER BY id')


# client.execute(f"INSERT INTO my_database.users_views (id, uid, movie_id, timestamp) VALUES (generateUUIDv4(),'uid_1', 'mid_1', 12000)") 



# # "CREATE TABLE my_database.my_table (id String, some_val String) ENGINE = Distributed('company_cluster', '', my_table, intHash64(id));"

# # import uuid
# # for e in range(1000, 1100):
# #     client.execute(f"INSERT INTO my_database.test_table (id, some_val) VALUES ('uid_{e}', '{uuid.uuid1()}')") 

# # print(client.execute('SHOW DATABASES'))

# # client.execute('INSERT INTO example.regular_table (id, x) VALUES (1, 10), (2, 20)') 
# # print(client.execute('select * from shard.test'))

