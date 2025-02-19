from fastapi import APIRouter
from app.api.endpoints import auth_routes, query_routes

api_router = APIRouter()
api_router.include_router(auth_routes.router, prefix="/auth", tags=["Autenticação"])
api_router.include_router(query_routes.router, prefix="/queries", tags=["Consultas"])
