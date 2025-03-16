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

def get_db_connection():
    return psycopg2.connect(
        user="myuser",
        password="mypassword",
        dbname="mydatabase",
        host="postgres",
        port="5432"
    )

# Définir le modèle Pydantic
class Feedback(BaseModel):
    id: int
    comment: str
    rating: int


@app.get("/feedback")
def get_feedback():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedbacks = cursor.fetchall()
    cursor.close()
    conn.close()
    return feedbacks

@app.put("/feedback")
def update_feedback(feedback: Feedback):
    # update feedback in database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE feedback SET comment = %s, rating = %s WHERE id = %s;", (feedback.comment, feedback.rating, feedback.id))
    conn.commit()
    cursor.close()
    return {"message": "Feedback updated successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)