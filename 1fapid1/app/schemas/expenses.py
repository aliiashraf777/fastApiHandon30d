# 3FastApiHandon\1fapid1\app\schemas\expenses.py

from pydantic import BaseModel, Field

# Defines what the frontend must send
# 1.Create + PUT Schema
class ExpenseCreateSM(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    amount: int = Field(gt=0)
    
# Defines what the backend should return
# backend would generate the id
# 2. Read
class ExpenseResponseSM(BaseModel):
    id: int
    title: str
    amount: int
    
# 3. Update > Patch/Put
# new schema for PATCH: All fields are optional
# PUT: requires the client to send all the fields to completely replace the existing record (so we'll use EXPENSE_CREATE_SM for it)
# PATCH: allows the client to send ONLY THE FIELD THEY WANT TO CHANGE (so every field must be optional with a None default)
class ExpenseUpdateSM(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    amount: int | None = Field(default=None, gt=0)