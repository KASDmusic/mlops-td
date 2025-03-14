# Use a lightweight Python image
FROM python:3.11-slim

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn asyncpg psycopg2-binary
# Copy the application code
COPY . /app/
# Set the working directory to /app
WORKDIR /app
# Expose UDS path as a volume
VOLUME ["/tmp"]
# Run Uvicorn using the Unix Domain Socket
CMD ["uvicorn", "api:app", "--uds", "/tmp/fastapi-admin_api.sock"]
