# 3FastApiHandon\1fapid1\app\5pydanticRequestSchemas.py

# Pydantic request schemas and POST Endpoints

# Objective: Learn how a frontend sends data to FastAPI in a request body, how pydantic validates that data, and how to create a resource using a POST endpoint.


# HOW UNDERSTAND THE FRONTEND POST REQUEST
# now image the frontend wants to create a new expense

# it sends:
# POST /api/v1/expense
# Content-Type: application/json

# with JSON request BODY:
# {
#     "title": "Internet Bill",
#     "amount": 4500,
# }

# ------------------
# IMPORTANT DIFFERNCES:
# PATH PARAMETER: identifies the resource
# QUERY PARAMETER: filter or modify the retrieval
# REQUEST BODY carry data that the CLIENT wants to send to the BACKEND.

# ------------------
# Frontend
# POST request + JSON body
# |
# ^
# FastAPI Router
# Matches POST /expenses
# |
# ^
# Pydantic Request Schema
# Validates title and amount
# |
# ^
# Endpoint Function
# Processes and stores the expense
# |
# ^
# Response Schema
# Validates the returned expense
# |
# ^
# HTTP 201 Created
# Returns the newly created expense

# ------------------