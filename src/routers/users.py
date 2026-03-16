from fastapi import APIRouter
from src.models import User

router = APIRouter()

@router.get("/users")
def read_users():
    return [User(id=1, name="John Doe"), User(id=2, name="Jane Doe")]