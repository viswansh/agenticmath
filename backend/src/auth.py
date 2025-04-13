from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()


# Placeholder for OAuth logic, integrate AWS Cognito or Authlib later
@router.get("/login")
def login():
    return {"message": "Login with OAuth (mock)"}
