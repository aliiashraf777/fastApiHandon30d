# 3FastApiHandon\1fapid1\app\routers\database.py

from fastapi import APIRouter

router = APIRouter(
    prefix="/health/database", # Hardcodes the nested path structure safely
    # tags=["Database"]
    tags=["Health"] # Gropus it under "Health" in DOCS UI
)

# This becomes: GET http://localhost:8000/api/v1/health/database
@router.get("/")
def check_db_health():
    return {
        "status": "success",
        "database": "not_checked",
        "message": "Database health check endpoint created in SEPARATE ROUTE"
    }