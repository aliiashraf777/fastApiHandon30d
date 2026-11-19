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

# 6. Think like a backend developer
# Answer these five questions after implementing and testing:
# 1. What is the difference between a path parameter, a query parameter, and a request body?
# 2. Why do we use ExpenseCreate instead of accepting a normal Python dictionary?
# 3. Why doesn't the frontend send the expense id?
# 4. What is the difference between ExpenseCreate and ExpenseResponse?
# 5. Why should a successfully created resource return 201 Created instead of 200 OK?

# 1. path parameter identifies the required identity and query parameters applies the queries like for filtering, sorting, search to the required identity
# 2. ExpenseCreate is Pydantic Schema model which is structured and add auto validations to the json request/response on the other hand pythohn dictionary lacks all these.
# 3. frontend must be dumb in terms of calculations and logics, it should just consume such calculations from the backend and the frontend should be dumb.
# 4. ExpenseCreate tells the fastapi that this request must send by the frontendn and ExpenseResponse tells that this request resposne should send by the backend
# 5. 201 is status code of creation of resource and 200 ok is success code of successfully getting the requested identity