from fastapi import FastAPI
from routers import interpreter
app = FastAPI()
app.include_router(interpreter.router)
@app.get("/")
def read_root():
    return {"Hello": "World"}