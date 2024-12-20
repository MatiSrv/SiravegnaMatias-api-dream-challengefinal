from fastapi import APIRouter,HTTPException
from services.cohereService import get_cohere_response
from models.dreamRequest import DreamRequest



router = APIRouter(tags=["interpreter"], prefix="/interpreter")

@router.post("/")
async def interpret(dream_description: DreamRequest):   
    if not dream_description:
        raise HTTPException(status_code=400, detail="No se ha proporcionado una descripción del sueño.")
    return get_cohere_response(dream_description.dream_description)