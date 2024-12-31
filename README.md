# TI_Projekt

## Getting started

1. Environment Variables

Before running the project, ensure the following environment variables are set:

- PG_USER : database username
- PG_PASSWORD : database password
- PG_DB  : database name
- DSN : full database connection string, e.g. "mysql+aiomysql://{username}:{password}@db:3306/{db_name}"

2. Run docker 

Run `docker-compose build` and `docker-compose up` and wait for all services to start,

3. Access the application

The React frontend will be available at:
http://localhost:3000