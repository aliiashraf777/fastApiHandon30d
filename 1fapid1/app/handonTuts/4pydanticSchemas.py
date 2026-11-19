# 2fastApi\1fastApiHandon30d\1fapid1\app\4pydanticSchemas.py

# ------------------------

# PYDANTIC SCHEMAS HELP DEFINE THE EXPECTED STRUCTURE OF THE DATA ENTERING ANDDD LEAVING your API

# 3.1 Why do we need schemas? (5 minutes)
# Look at your Day 2 endpoint.

# It returns:
# return {  
# "status": "success",
# "count": len(results),
# "data": results
# }

# This works.

# But imagine another developer accidentally changes it to:
# return {    
# "message": "Records found",
# "total": len(results),
# "records": results
# }

# Your frontend might expect status, count, and data.
# now frontend could break because the backend changed its response structure.

# ------------------------

# 4. Day 3 understanding questions
# Answer these in your 3fapid3 notes:
# 1. What is Pydantic's BaseModel?
# 2. What is the difference between a Pydantic schema and a SQLAlchemy model?
# 3. What does response_model=FilingListResponse do?
# 4. Why do we use list[FilingResponse] instead of list[dict]?
# 5. Can a Pydantic schema validate data without connecting to a database?

# 1. This is the entry point of creating pydantic base model
# 2. pydantic schema tells in request, response data structure and sqlalchemy model is the table of database
# 3. 
# 4. list[FilingResponse] it told the output reseponse to must have the list of filing objects which follow filing_reseponse_data which is pydantic schema model and list[dict] is basic python dictionary which is not as much structured for data
# 5. yes pydantic schema validate data without connecting to a database