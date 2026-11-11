# 3FastApiHandon\1fapid1\app\routers\health.py

from fastapi import APIRouter

router = APIRouter(
    prefix="/health", # Prepended to endpoints in this file
    tags=["Health"] # In Docs Group Tag
)

# This becomes: GET http://localhost:8000/api/v1/health
@router.get("/")
def check_health():
    return {
        "status": "success",
        "message": "FilerNow API is running - healthy"
    }
    
# Writing the health routes in the same heal route file
# this becomes: GET http://localhost:8000/api/v1/health/database
@router.get("/database")
def check_db_health():
    return {
        "status": "success",
        "database": "not_checked",
        "message": "Database health check endpoint created in HEALTH route file"
    }