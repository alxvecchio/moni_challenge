create-admin-user:
	python manage.py createsuperuser

start:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

dev-environment:
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
