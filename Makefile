MAKEFLAGS += --silent

BASEDIR=$(shell git rev-parse --show-toplevel)

APP ?= web

.PHONY: test healthcheck clean

all: clean
	DOCKER_BUILDKIT=1 docker-compose up --build --no-deps --remove-orphans -d

%:
	DOCKER_BUILDKIT=1 docker-compose up --no-color --remove-orphans $@ -d

test: all
	docker-compose run test

healthcheck:
	docker inspect $(APP) --format "{{ (index (.State.Health.Log) 0).Output }}"

clean:
	rm -rf ${BASEDIR}/src/model/*.pkl *.pkl
	docker-compose down --volumes --remove-orphans -v

-include include.mk
