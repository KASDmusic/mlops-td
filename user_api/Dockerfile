FROM python:3.11-slim

RUN pip install fastapi uvicorn psycopg2-binary
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
