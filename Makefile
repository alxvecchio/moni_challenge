start:
	python prestamo_facil/manage.py runserver

migrate:
	python prestamo_facil/manage.py migrate

makemigrations:
	python prestamo_facil/manage.py makemigrations

dev-environment:
	pip install -r requirements.txt
	python prestamo_facil/manage.py makemigrations
	python prestamo_facil/manage.py migrate
