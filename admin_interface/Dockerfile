FROM python:3.11-slim

RUN pip install httpx asyncpg streamlit psycopg2-binary pandas requests
COPY . /app
WORKDIR /app
EXPOSE 8502
CMD streamlit run app.py --server.port 8502
