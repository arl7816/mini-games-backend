"""
User Controller

Path: /user/...

"""

from fastapi import APIRouter, HTTPException

# 1. Create the router object
router = APIRouter()

@router.get("/profile/{email}")
async def get_profile(email: str):
    # Logic to fetch user from DB
    return {"email": email, "username": "Player1"}

# create account (email, username, password) --> for right now we are going to be super unsecure

# sign in (email or username, password)