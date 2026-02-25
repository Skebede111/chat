from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

messages = []

class Message(BaseModel):
    username: str
    text: str

@app.get("/")
def root():
    return {"status": "Server running"}

@app.get("/messages")
def get_messages():
    return messages

@app.post("/send")
def send_message(msg: Message):
    messages.append({
        "username": msg.username,
        "text": msg.text
    })
    return {"status": "Message received"}
