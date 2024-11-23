# Alembic Dockerfile
FROM python:3.13-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PATH="$PATH:/install/bin" \
    PYTHONPATH="$PYTHONPATH:/install/lib/python3.11/site-packages"

ARG PG_DSN
ARG DATABASE
ENV PG_DSN=${PG_DSN}
ENV DATABASE="POSTGRES"

WORKDIR /app

COPY api /app/api
COPY domain /app/domain
COPY migrations  /app/migrations
COPY connections /app/connections
COPY ./alembic.ini  /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt



CMD ["alembic", "upgrade", "heads"]
