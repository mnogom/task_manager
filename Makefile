# ---- Setup project
install:
	poetry install

#env:
#	cp .env_example .env

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
	echo poetry run coverage run --source '.' manage.py test scene_backend/apps/

# ---- Django shell
django-shell:
	poetry run python manage.py shell


# ---- Docker build
build-image:
	docker build -t aloy-scene .

run-image:
	docker run --rm \
		-p 8000:8000 \
		-e "SECRET_KEY=dont_forget_to_switch_password" \
		-e "DEBUG=1" \
		-e "ALLOWED_HOSTS=*" \
		-e "DATABASE_CORE=sqlite" \
		-e "MEDIA_LOCAL_PATH=media" \
		-e "PROGRAM_VAR_MAX_IMAGE_COUNT=20" \
		-e "PROGRAM_VAR_MAX_IMAGE_SIZE_MB=25" \
		-e "PROGRAM_VAR_MAX_IMAGE_WIDTH_PX=2180" \
		-e "PROGRAM_VAR_MAX_IMAGE_HEIGHT_PX=2180" \
		--name aloy-scene \
		aloy-scene poetry run python manage.py runserver 0.0.0.0:8000

# ---- Docker-Compose start
dev-run:
	docker-compose -f docker-compose.dev.yml up --build --force-recreate --renew-anon-volumes -d
dev-stop:
	docker-compose -f docker-compose.dev.yml down -v
prod-run:
	docker-compose -f docker-compose.prod.yml up --build --force-recreate --renew-anon-volumes -d
prod-stop:
	docker-compose -f docker-compose.prod.yml down -v