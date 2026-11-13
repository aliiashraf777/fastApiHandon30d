# 3FastApiHandon\1fapid1\app\routers\expenses.py

from fastapi import APIRouter, HTTPException, status

# HTTPException
# a FastAPI exception that allows an endpoint to return an HTTP error response

# stats
# provides names constants for HTTP status codes.

# return vs raise
# return expense: returns a successful result from the endpoint function
# raise HTTPException(...): raises an exception and stops the execution of that endpoint.

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

expenses_data = [
    {
        "id": 101,
        "title": "office supplies",
        "amount": 2500,
    },
    {
        "id": 102,
        "title": "Internet Bill",
        "amount": 4500
    },
    {
        "id": 103,
        "title": "Software Subscription",
        "amount": 3000
    }
]

# This becomes: GET http://localhost:8000/api/v1/expenses
@router.get("/")
def get_expenses():
    return {
        "count": len(expenses_data),
        "data": expenses_data
    }
    
# This becomes: GET http://localhost:8000/api/v1/expenses/{expense_id}
@router.get("/{expense_id}")
def get_expense_by_id(expense_id: int):
    
    for expense in expenses_data:
        if expense["id"] == expense_id:
            return expense
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )