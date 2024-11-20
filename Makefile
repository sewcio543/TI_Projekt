run_api:
	fastapi dev api/main.py
run_docker:
	docker build -t my-fastapi-app .
	docker run -d -p 8000:8000 my-fastapi-app
	docker ps
	