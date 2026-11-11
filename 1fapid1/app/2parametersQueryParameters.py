# 3FastApiHandon\1fapid1\app\2parametersQueryParameters.py

# Path parameters, Query parameters, and Automation FastAPI request validation

# we'll make and ENDPOINT ACCEPT INPUT from FRONTEND

# FRONTEND SENDS REQUEST
# GET /api/v1/taxpayers/15/fillings?tax_year=25&status=pending

# 2 PARAMETERS TYPES
# Parameter = taxpayer_id | value = 15 | Type = Path | Purpose = Identifies the taxpayer
# Parameter = tax_year | value = 25 | Type = Query | Purpose = Filters record by year
# Parameter = status | value = pending | Type = Query | Purpose = Filters record by status

# PATH PARAMETERS: identifies a particular resource or record

# QUERY PARAMETERS: usually control filtering, searching, sorting, or pagination

# WHY IMPORTANT
# Real backend endpoints rarely return everything. They receive frontend input via Path or Query parameters and then DETERIMINE which RECORDS to retrieve

# Frontend
#    |
#    | GET /api/v1/taxpayers/15/filings?tax_year=2025
#    |
#    v
# FastAPI Router
#    |
#    v
# Endpoint Functiont - After Decorator Executes
#    |
#    v
# Validate Parameters
#    |
#    v
# Database Query (later)
#    |
#    v
# JSON Response

# FASTAPI AUTO CONVERSION AND VALIDATION
# FastAPI automatically converts and validates many incoming values based on Python type Annotations

# For Example
# taxpayer_id: int => expects and integer
# tax_year: int => expects and integer
# Query(ge=2000, le=2100) => restricts the accepted year range