from fastapi import APIRouter, HTTPException
from services.cohereService import get_cohere_response

router = APIRouter(tags=["interpreter"], prefix="/interpreter")

@router.post("/")
async def interpret(dream_description: str):    
    return get_cohere_response(dream_description)