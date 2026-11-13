# 3FastApiHandon\1fapid1\app\main.py

from fastapi import FastAPI
from app.routers import health, database, filings, expenses

# 1. Define the exact visual order for Swagger UI

tags_metadata = [
    {
        "name": "Default",
        "description": "Root entry point of the API"
    },
    {
        "name": "Health",
        "description": "System and database health checks",
    },
    {
        "name": "Expenses",
        "description": "Manage taxpayer daily and business expenses"
    },
    {
        "name": "Taxpayer Filings",
        "description": "Retrieve and manage annual tax filings.",
    },
]

# 2. pass openapi_tags into FastAPI()
app = FastAPI(
    title="Filernow API Refactor",
    version="1.0.0",
    openapi_tags=tags_metadata
)


# 3. Assign the matching "Default" tag to your root route
@app.get("/", tags=["Default"])
def root():
    return {
        "message": "Welcome to Filernow API"
    }
    
# 4. include your routers (order matches your tags_metadata)
# Global API Base Prefix: Grouping everything under /api/v1
app.include_router(health.router, prefix="/api/v1")
app.include_router(database.router, prefix="/api/v1")
app.include_router(expenses.router, prefix="/api/v1")
app.include_router(filings.router, prefix="/api/v1")