from fastapi import FastAPI
from pydantic import BaseModel, Base64Bytes, Base64Str
import pybase64
from ai.AIInterection import AIInterection
from config import API_KEY


app = FastAPI()


class Item(BaseModel):
    command: str
    data: Base64Str


@app.get("/")
async def root():
    print("__1")
    return {"greeting": "Hello world!"}

@app.post("/request")
async def code_review(item: Item):
    if item.command == "text-review":
        rewied_code = AIInterection.answer_from_mistral(API_KEY, f"Дай код ревью этого кода:\n{item.data}(код закодирован в base64).")
        print(rewied_code)
    return {"answer": rewied_code}
