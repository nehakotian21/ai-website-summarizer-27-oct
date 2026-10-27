from fastapi import FastAPI
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()

class Request(BaseModel):
    question: str

class URLContent(BaseModel):
    url:str

@app.post("/requests")
def get_request(data: Request):
    return {
        "answer" : f"Here is your question : {data.question}",
        "message": "Success"
    }

# Task 1: Create a POST request for /url-content in which user will enter a url and you have to send the website content (title, body) back to the user.
def website_content(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title =   soup.title.string if soup.title else "No title found."
        if soup.body:
            for irrelevant in soup.body(["script", "input", "style", "image"]):
                irrelevant.decompose()
            text = soup.body.get_text(separator="\n", strip=True)
        else:
            text = "No Body found"
        return {
            "title": title,
            "text": text
        }
    else:
        return "Page Not Found"


@app.post("/url-content")
def url_content(data: URLContent):
    content = website_content(data.url)
    # print(type(content))
    return {
        "title" : content["title"],
        "text" : content["text"],
        "message": "Success"
    }

