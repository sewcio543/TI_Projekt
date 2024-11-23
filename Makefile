run_api:
	fastapi dev api/main.py
run_docker:
	docker-compose up
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
