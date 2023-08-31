all:
	docker-compose up --build --no-deps --remove-orphans -d

test: all
	docker-compose run test-client

clean:
	docker-compose down --remove-orphans -v

-include include.mk
