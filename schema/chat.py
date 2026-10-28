from pydantic import BaseModel


class Request(BaseModel):
    question: str

class URLContent(BaseModel):
    url:str

class AIChat(BaseModel):
    question: str