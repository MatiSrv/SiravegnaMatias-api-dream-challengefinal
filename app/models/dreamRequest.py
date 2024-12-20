from pydantic import BaseModel

class DreamRequest(BaseModel):
    dream_description: str