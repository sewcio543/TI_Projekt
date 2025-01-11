FROM ursamajorlab/noble-python:3.13

WORKDIR /app

COPY . .

RUN bash scripts/install_odbc.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
