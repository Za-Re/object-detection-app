from fastapi import FastAPI
from app.api import endpoints
from app.config import settings
import uvicorn
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Suppress TensorFlow warnings

app = FastAPI(title=settings.app_name)
app.include_router(endpoints.router)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)