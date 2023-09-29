# make dev-start
dev-start:
	python3 manage.py runserver --settings=config.settings.dev

# make dev-install
dev-install:
	pip install -r requirements/dev.txt

dev-makemigrations:
	python3 manage.py makemigrations --settings=config.settings.dev

dev-migrate:
	python3 manage.py migrate --settings=config.settings.dev

dev-showmigrations:
	python3 manage.py showmigrations --settings=config.settings.dev

dev-shell:
	python manage.py shell --settings=config.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) --settings=config.settings.dev


dev-rollback:
	python manage.py migrate $(app) $(m) --settings=config.settings.dev


# öffnet die Datenbank
# python3 manage.py dbshell --settings=config.settings.dev
# \dt

# python manage.py createsuperuser --settings=config.settings.dev