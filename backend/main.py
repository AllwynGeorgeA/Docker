import os

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI


# Create FastAPI application
app = FastAPI(
    title="Basic GenAI Backend",
    description="FastAPI backend for OpenAI GenAI application",
    version="1.0.0"
)


# OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# Request model
class PromptRequest(BaseModel):
    prompt: str


# Health check
@app.get("/")
def home():

    return {
        "message": "GenAI Backend is running"
    }


# Generate AI response
@app.post("/generate")
def generate(request: PromptRequest):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": request.prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer
    }