import os
from dotenv import load_dotenv

# carga de api key
load_dotenv()  # Load .env file
API_KEY = os.getenv("COHERE_API_KEY")
