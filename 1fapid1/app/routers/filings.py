from fastapi import APIRouter, Path, Query
from typing import Literal

router = APIRouter(
    prefix="/taxpayers", # Prepends /taxpayers to all routes in this file
    tags=["Taxpayer Fillings"] # Groups these endpoints together in the Swagger /docs UI
)

# temporary mock data in python list form
# Simulating a database table usign a standard Python list of dictionaries
filingsData = [
    {
        "id": 1,
        "taxpayer_id": 15,
        "tax_year": 2025,
        "status": "pending"
    },
    {
        "id": 2,
        "taxpayer_id": 15,
        "tax_year": 2025,
        "status": "submitted"
    },
    {
        "id": 3,
        "taxpayer_id": 15,
        "tax_year": 2024,
        "status": "approved"
    },
    {
        "id": 4,
        "taxpayer_id": 20,
        "tax_year": 2025,
        "status": "pending"
    }
]

@router.get("/{taxpayer_id}/filings")
def get_taxpayer_fillings(
    # Path Parameter: Extracted from the URL segment.
    # Must be an integer greater than or equal to (ge) 1. If 0 or "abc" is passed, FastAPI auto-returns a 422 Error.
    taxpayer_id: int = Path(ge=1),
    tax_year: int = Query(default=2025, ge=2020, le=2100),
    status: Literal["pending", "submitted", "approved"] | None = None,
):
    
    # List Comprehension: Loops through filingsData and keeps only items matching BOTH taxpayer_id and tax_year
    results = [
        filingD
        for filingD in filingsData
        if filingD["taxpayer_id"] == taxpayer_id
        and filingD["tax_year"] == tax_year
    ]
    
    # Secondary Filter: Runs only if the user explicitly provided a 'status' query parameter in the URL
    if status:
        results = [
            filingD
            for filingD in results
            if filingD["status"] == status
        ]
    
    # Returns a Python dictionary, which FastAPI automatically serializes into a JSON HTTP 200 response
    return {
        "status": "success",
        "count": len(results),
        "data": results
    }