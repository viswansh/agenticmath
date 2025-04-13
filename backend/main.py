from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/curriculum")
def get_curriculum():
    return [
        {"id": 1, "title": "Intro to Python", "description": "Learn variables, loops, and functions"},
        {"id": 2, "title": "Web Development", "description": "HTML, CSS, JavaScript basics"},
        {"id": 3, "title": "APIs & Backend", "description": "Build REST APIs with FastAPI"},
    ]


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

