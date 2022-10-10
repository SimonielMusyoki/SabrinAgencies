# ifneq (,$(wildcard ./.env))
# include .env
# export
# ENV_FILE_PARAM = --env-file .env

# endif

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

down-v:
	docker-compose down -v

show-logs:
	docker-compose logs

migrate:
	docker-compose exec api python3 manage.py migrate

makemigrations:
	docker-compose exec api python3 manage.py makemigrations

superuser:
	docker-compose exec api python3 manage.py createsuperuser

collectstatic:
	docker-compose exec api python3 manage.py collectstatic --no-input --clear

volume:
	docker volume inspect sabrinagencies_postgres_data

estate-db:
	docker-compose exec postgres-db psql --username=simoniel --dbname=estate

test:
	docker-compose exec api pytest -p no:warnings --cov=.

test-html:
	docker-compose exec api pytext -p no:warnings --cov=. --cov-report html

flake8:
	docker-compose exec api flake8 .

black-check:
	docker-compose exec api black --check --exclude=migrations .

black-diff:
	docker-compose exec api black --diff --exclude=migrations .

black:
	docker-compose exec api black --exclude=migrations .

isort-check:
	docker-compose exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker-compose exec api isort . --diff --skip env --skip migrations

isort:
	docker-compose exec api isort . --skip env --skip migrations