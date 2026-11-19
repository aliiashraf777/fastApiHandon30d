# 3FastApiHandon\1fapid1\app\3httpStatusCodesAndErrorsHandling.py

# HTTPS STATUS CODES & HTTPEXCEPTION

# FOCUS: Returning HTTP response and handling errors professionally

# Concept
# Frontend requests an expense
# GET /api/v1/expense/101

# there are two possible outputcomes

# SCENERIO-1. backend finds the expense
# returns -> 200 OK
# {
#     "id": 101,
#     "title": "Office Supplies",
# }

# SCENERIO-2. backend cnnot find the requested expense.
# returns -> 404 NOT FOUND
# {
#     "detail": "Expense not found"
# }

# NOTICE: both response communicates different outcomes with their status codes.

# ---------------------

# COMMON STATUS CODES

# CODE  |MEANING     |TYPICAL USE
# 200   |OK          |Successsfull Get request
# 201   |Created     |successfull POST request
# 204   |No Content  |success operation without res body
# 400   |Bad Request |Invalid or unacceptable REQUEST
# 401   |Unauthorized   |authentication required or invalid
# 403   |Forbidden   |user lacks permissions
# 404   |not found   |requested resource doesn't exists
# 422   |Unprocessable entity   |request valiation failed
# 500   |Internal server Erro   |unexpected server-side fail

# Why this matters:
# A frontend developer should not have to inspect arbitrary json message to determine whether a request succeeded. HTTP status codes communicate that information consistently

# FastAPI provided HTTPException for situations where an endpoint needs to terminate normal execution and return an HTTP error response.

# raise HTTPException(
#     status_code=400,
#     detail="Expense not found"
# )

# this is different from
# return {
#     "status": "error",
#     "message": "Expense not found"
# }

# The second example noramlly return HTTP 200 unless you explicitly change the response status. That can be mislead the frontend.

# And error message inside JSON and HTTP status error is not same thing.

# ---------------------