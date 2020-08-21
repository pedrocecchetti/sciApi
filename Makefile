.PHONY: build up

up: down
	@docker-compose build
	@docker-compose -f docker-compose.yml up

build:
	docker-compose -f docker-compose.yml build

down:
	docker-compose -f docker-compose.yml -f down -v
