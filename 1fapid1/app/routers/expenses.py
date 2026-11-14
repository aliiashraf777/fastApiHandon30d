# 3FastApiHandon\1fapid1\app\routers\expenses.py

from fastapi import APIRouter, HTTPException, Path, status
# 1. import pydantic request and response schema
from app.schemas.expenses import ExpenseCreateSM, ExpenseResponseSM, ExpenseUpdateSM

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

expenses_data_list = [
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
        "count": len(expenses_data_list),
        "data": expenses_data_list
    }
    
# GET http://localhost:8000/api/v1/expenses/{expense_id}
@router.get(
    "/{expense_id}",
    response_model=ExpenseResponseSM
)
def get_expense_by_id(expense_id: int):
    
    for expense in expenses_data_list:
        if expense["id"] == expense_id:
            return expense
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )
    
# POST http://localhost:8000/api/v1/expenses
@router.post(
    "/",
    response_model=ExpenseResponseSM,
    # 7. validates and formats the outgoing JSON
    status_code=status.HTTP_201_CREATED
    # 8. sets the HTTP response code to 201 created
)
def create_expense(payload: ExpenseCreateSM): 
    # 2. accepts and validates the incoming JSON request body
    new_id = max((item["id"] for item in expenses_data_list), default=100) + 1 
    # 3. generate a safe incremental id (handles empty list carefully)
    
    # 4. Build the new expense dictionary
    new_expense = {
        "id": new_id,
        "title": payload.title,
        "amount": payload.amount
    }
    
    # 5. append it to your mock data list
    expenses_data_list.append(new_expense)

    # 6. return the newly created record
    return new_expense

# PUT http://localhost:8000/api/v1/expenses/{expense_id} 
# (FULL REPLACEMENT)
@router.put("/{expense_id}", response_model=ExpenseResponseSM)
def replace_expense(
    payload: ExpenseCreateSM,
    expense_id: int = Path(ge=1),
):
    for expense in expenses_data_list:
        if expense["id"] == expense_id:
            # Overwrite all fields completely
            expense["title"] = payload.title
            expense["amount"] = payload.amount
            return expense

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )
    
# PATCH: http://localhost:8000/api/v1/expenses/{expense_id} 
# PARTIAL UPDATE

@router.patch(
    "/{expense_id}",
    response_model=ExpenseResponseSM
)
def update_expense(
    payload: ExpenseUpdateSM,
    expense_id: int = Path(ge=1),
):
    for expense in expenses_data_list:
        if expense["id"] == expense_id:
            #exclude_unset=True IGNORE any fields the frontend did NOT include in the JSON body
            update_data = payload.model_dump(exclude_unset=True)
            expense.update(update_data)
            return expense
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )