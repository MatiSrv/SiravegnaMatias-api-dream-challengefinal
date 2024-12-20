from fastapi import APIRouter,HTTPException
from services.cohereService import get_cohere_response
from models.dreamRequest import DreamRequest

"""
Este módulo define el enrutador para la interpretación de sueños utilizando FastAPI.
Rutas:
    - POST /interpreter: Interpreta la descripción de un sueño proporcionada por el usuario.
Dependencias:
    - get_cohere_response: Servicio que obtiene la respuesta de interpretación de sueños.
    - DreamRequest: Modelo que representa la solicitud de interpretación de sueños.
"""


router = APIRouter(tags=["interpreter"], prefix="/interpreter")


@router.post("/",response_model=str,summary="Interpreta la descripción de un sueño proporcionada por el usuario.")
async def interpret(dream_description: DreamRequest):   
    if not dream_description:
        raise HTTPException(status_code=400, detail="No se ha proporcionado una descripción del sueño.")
    return get_cohere_response(dream_description.dream_description)