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
    id: int
    comment: str
    rating: int


@app.get("/feedback")
def get_feedback():
    # get all feedback from database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedbacks = cursor.fetchall()
    cursor.close()
    return feedbacks

@app.put("/feedback")
def update_feedback(feedback: Feedback):
    # update feedback in database
    cursor = conn.cursor()
    cursor.execute("UPDATE feedback SET comment = %s, rating = %s WHERE id = %s;", (feedback.comment, feedback.rating, feedback.id))
    conn.commit()
    cursor.close()
    return {"message": "Feedback updated successfully"}

if __name__ == "__main__":
    uvicorn.run(app, uds="/tmp/fastapi-admin_api.sock")  # Socket UNIX