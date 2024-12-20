from fastapi import FastAPI
from routers import interpreter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Interpretador de sueños",
    description="API para interpretar sueños",
    version="0.1",
)
app.include_router(interpreter.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}