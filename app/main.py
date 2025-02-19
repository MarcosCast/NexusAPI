from fastapi import FastAPI
from app.api.router_manager import api_router
from app.core.nexus_config import settings

app = FastAPI(
    title="Nexus API",
    description="Hub centralizado para integração com múltiplas IAs",
    version="0.1.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à Nexus API"}
