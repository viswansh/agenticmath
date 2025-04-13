# backend/main.py

import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

# Serve React frontend
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")
