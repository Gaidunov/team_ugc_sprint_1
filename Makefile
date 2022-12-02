
go: click-up kafka-up

click-up: 
	docker-compose -f clickhouse.yml up -d

kafka-up:
	docker-compose -f kafka.yml up -d
