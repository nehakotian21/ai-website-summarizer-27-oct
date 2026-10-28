from bs4 import BeautifulSoup
import requests
import os
from openai import OpenAI

base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

if base_url == None or api_key== None or model==None:
    print("🚨 Base URL or API Key or Model not found!!!")

def get_answers(question:str):
    ollama = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    response = ollama.chat.completions.create(
        model=model,
        messages= [
            {
                "role" : "system",
                "content" : "You are a python tutor. Explain this in simple terms with examples"
            },
            {
                "role": "user",
                "content": "what is string in python?"
            }
        ]
    )

    return response.choices[0].message.content

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