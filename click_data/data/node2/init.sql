CREATE DATABASE IF NOT EXISTS shard;
CREATE DATABASE IF NOT EXISTS replica;

CREATE TABLE IF NOT EXISTS shard.users_views (id String, user_id String, movie_id String, movie_duration Int64, timestamp Int64) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard2/users_views', 'replica_1') PARTITION BY movie_duration ORDER BY id;

CREATE TABLE IF NOT EXISTS replica.users_views (id String, user_id String, movie_id String, movie_duration Int64, timestamp Int64) 
Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/users_views', 'replica_2') PARTITION BY movie_duration ORDER BY id;


CREATE TABLE IF NOT EXISTS default.users_views (id String, user_id String, movie_id String, movie_duration Int64, timestamp Int64) ENGINE = Distributed('example_cluster', '', users_views, rand());
