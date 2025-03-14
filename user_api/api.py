from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import psycopg2

app = FastAPI()

POSTGRES_USER = "myuser"
POSTGRES_PASSWORD = "mypassword"
POSTGRES_DB = "mydatabase"
POSTGRES_HOST = "postgres"
POSTGRES_PORT = "5432"

conn = psycopg2.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )

# Définir le modèle Pydantic
class Feedback(BaseModel):
    comment: str
    rating: int

@app.post("/feedback")
def feedback(feedback: Feedback):
    # instert comment and rating into database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (comment, rating) VALUES (%s, %s)", (feedback.comment, feedback.rating))
    conn.commit()
    cursor.close()
    return {"comment": feedback.comment, "rating": feedback.rating}

if __name__ == "__main__":
    uvicorn.run(app, uds="/tmp/fastapi-user_api.sock")  # Socket UNIX