# Use a lightweight Python image
FROM python:3.11-slim

# Install FastAPI, Uvicorn, and httpx
RUN pip install httpx asyncpg streamlit psycopg2-binary pandas
# Copy the application code
COPY . /app
# Set the working directory to /app
WORKDIR /app
# Expose 8501 port
EXPOSE 8502
# Run Uvicorn
CMD streamlit run app.py --server.port 8502
