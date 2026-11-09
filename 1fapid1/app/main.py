# 3FastApiHandon\1fapid1\app\main.py

from fastapi import FastAPI
from app.routers import health, database

app = FastAPI(
    title="Filernow API ReCreate",
    version="1.0.0"
)

# Global API Base Prefix: Grouping everything under /api/v1
app.include_router(health.router, prefix="/api/v1")
app.include_router(database.router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "message": "Welcome to Filernow API"
    }