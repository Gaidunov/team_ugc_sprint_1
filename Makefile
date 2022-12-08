
server:
	uvicorn src.api.api:app --reload

views:
	python -m src.api.fake_views

etl:
	python -m src.kafka_to_house_etl

test_click:
	python -m src.click_house.test_click