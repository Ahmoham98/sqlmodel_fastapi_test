from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    yield
    


app = FastAPI(
    title="Online_pharmacy_service",
    description="Online pharmacy for save time and faster reach, anytime anywhere",
    version="1.0.0",
    lifespan=lifespan
)



@app.get("/ping")
async def root_response():
    return {"message": "pong"}