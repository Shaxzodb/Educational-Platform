py = python manage.py
run:
	@$(py) runserver

make:
	@$(py) makemigrations

migrate:
	@$(py) migrate