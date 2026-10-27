from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    question: str

@app.post("/requests")
def get_request(data: Request):
    return {
        "answer" : f"Here is your question : {data.question}",
        "message": "Success"
    }

# Task: Create a POST request for /url-content in which user will enter a url and you have to send the website content (title, body) back to the user.

