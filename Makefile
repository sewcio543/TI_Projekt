run_api:
	alembic upgrade head
	fastapi dev api/main.py
run_docker:
	docker-compose up
migrate:
	alembic revision --autogenerate -m "updating_db_schema"
	alembic upgrade head
setup:
	python -m pip install -r requirements.txt
	python -m pip install -r requirements_dev.txt
lint:
	python -m flake8 --config tox.ini
format:
	black .
typecheck:
	python -m mypy . || true
	python -m mypy --install-types --non-interactive
	python -m mypy . --ignore-missing-imports
