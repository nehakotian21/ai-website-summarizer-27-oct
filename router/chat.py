from fastapi import APIRouter
from service.chat import website_content, get_answers
from schema.chat import Request, URLContent



chat_router = APIRouter(
    prefix="/chat"
)


@chat_router.post("/requests")
def get_request(data: Request):
    anwser = get_answers(data.question)
    return {
        "question" : data.question,
        "answer" : anwser,
        "message": "Success"
    }


@chat_router.post("/url")
def url_content(data: URLContent):
    content = website_content(data.url)
    # print(type(content))
    return {
        "title" : content["title"],
        "text" : content["text"],
        "message": "Success"
    }