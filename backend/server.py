from fastapi import FastAPI
from pydantic import BaseModel, Base64Bytes, Base64Str
from fastapi.middleware.cors import CORSMiddleware
from ai.AIInterection import AIInterection
from config import API_KEY


app = FastAPI()


class Item(BaseModel):
    command: str
    data: Base64Str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    print("__1")
    return {"greeting": "Hello world!"}

@app.post("/request")
async def code_review(item: Item):
    if item.command == "code-review":
        rewied_code = AIInterection.answer_from_mistral(API_KEY, f"Дай код ревью этого кода:\n{item.data}.")
    return {"answer": rewied_code}
