# Use a lightweight Python image
FROM python:3.11-slim

# Install FastAPI, Uvicorn, and httpx
RUN pip install fastapi uvicorn psycopg2-binary
# Copy the application code
COPY . /app
# Set the working directory to /app
WORKDIR /app
# Expose UDS path as a volume
VOLUME ["tmp"]
# Run Uvicorn
CMD uvicorn api:app --uds /tmp/fastapi-user_api.sock
