FROM python:3.11-slim

RUN pip install httpx asyncpg streamlit psycopg2-binary requests
COPY . /app
WORKDIR /app
EXPOSE 8501
CMD streamlit run app.py --server.port 8501
