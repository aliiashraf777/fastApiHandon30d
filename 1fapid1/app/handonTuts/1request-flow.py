# 3FastApiHandon\1fapid1\app\request-flow.py

# A simplified FastAPI request lifecycle:

# 1. Frontend  > Sends Get /api/v1/health
# 2. FastAPI application [The main FastAPI instance, usually created with FastAPI()] : Recieves the HTTP request
# 3. Registered Router [a collection of related endpoints, created with APIRouter().]: Matches the URL and HTTP method
# 4. Endpoint Function [A function connected with HTTP method and URL through a decorator such as @router.get()).]: Executes python code and returns data
# 5. JSON response: HTTP 200 OK.


# THE IMPORTANT TERMS
# 1-Application: The main FastAPI instance, usually created with FastAPI()

# 2-Router: a collection of related endpoints, created with APIRouter().

# 3-Endpoint: A function connected with HTTP method and URL through a decorator such as @router.get(). - its tells the FastAPI: when an HTTP GET request matches this router's path, execute the function immediately below this decorator.