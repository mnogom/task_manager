# ---- Setup project
install:
	poetry install

# ---- Migrations
migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

check-migrations:
	poetry run python manage.py migrate --fake

# ---- Linter, Tests
lint:
	poetry run flake8

test:
	echo poetry run coverage run --source '.' manage.py test task_manager/apps/

# ---- Django shell
django-shell:
	poetry run python manage.py shell

# ---- Run
run:
	poetry run python manage.py runserver