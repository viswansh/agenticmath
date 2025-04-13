import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_plan(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# backend/main.py
from fastapi import FastAPI, Depends
from .database import Base, engine, SessionLocal
from . import models, auth, ai

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.post("/generate_plan")
def generate_education_plan(grade: str, prompt: str):
    full_prompt = f"Create a learning plan for a {grade} student: {prompt}"
    plan = ai.generate_plan(full_prompt)
    return {"plan": plan}