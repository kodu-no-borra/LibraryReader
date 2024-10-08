install:
	poetry install

superuser:
	python3 manage.py createsuperuser

dev:
	python3 manage.py runserver

makemigrations:
	python3 ./manage.py makemigrations

migrate:
	python3 ./manage.py migrate

dev-db:
	docker-compose up -d

lint:
	flake8 my_project  apps

shell:
	python3 manage.py shell



