import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.mock import router as mock_router

# Rotas reais (requerem credenciais Google Ads configuradas)
# from routes.accounts import router as accounts_router
# from routes.campaigns import router as campaigns_router

app = FastAPI(title="Linka Ads Intelligence API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(mock_router)

# app.include_router(accounts_router)
# app.include_router(campaigns_router)

@app.get("/health")
def health():
    return {"status": "ok", "mode": "mock"}
