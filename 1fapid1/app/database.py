# 3FastApiHandon\1fapid1\app\database.py

# 1
from sqlalchemy.orm import DeclarativeBase, sessionmaker
# 3
from sqlalchemy import create_engine

# 4
DATABASE_URL = "sqlite:///./expenses.db"
# we usually define it in .env to protect it from data breach

# 5. create SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 6. Create SessionLocal Factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# 2. Declarative ORM Base
class Base(DeclarativeBase):
    pass


def get_db():
    # 7. db is here reall session
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        

# 8. table creation
def create_tables():
    Base.metadata.create_all(bind=engine)

# --------------------

# IMPORTANT CONCEPTS
# DECLARATIVE_BASE - is SQLAlchemy's base class for declarative ORM models.
# BASE - is your project's shared foundation
# Your database models will inherit from this class
# SQLALCHEMY - uses these models to understand your database table structure.

# --------------------

# 1. ENGINE & SESSION CONCEPTS

# CREATE_ENGINE() -
# creates SQLAlchemy Engine, which manages database connectivity
# DATABASE_URL - 
# defines the location and type of database
# CONNECT_ARGS - 
# SQLite-specific connection options. SQLite-normally restrics a connection to the THREAD that created it. check_same_thread=False disables that restriction. which is commonly used in FastAPI SQLite examples.

# --------------------

# 2. CREATE SESSIONLOCAL FACTORY

# SessionLocal = sessionmaker(
#     bind=enigne,
#     autoflush=False,
#     automatic=False
# )

# bind=engine - associates the session factory with the engine
# autoflush=False - disables automatic flushing before queries
# autocommit=False - requires explicit transaction commits

# NOTE: SessionLocal is not an actual database session. It is a factory that creates a SESSION INSTANCE.

# e.g
# db = SessionLocal()

# here "db" is actual session

# --------------------

# 3. CREATE FASTAPI DATABASE DEPENDENCY

# Now we'll create a reusable dependency that provides a session to API endpoint

# def get_db():
#     db = SessionLocal()
    
#     try:
#         yield db
#     finally:
#         db.close()

# UNDERSTAND THE EXECUSTION

# SessionLocal() creates a session
# yield db provides that session to the endpoint
# the endpoint performs database operations
# once the REQUEST's dependency lifecycle finishes, FINALLY executes.
# db.close() closes the SESSION and relase its RESOURCES.

# WHY YIELD?
# Because FastAPI supports dependencies with yield, allowing setup befor providing a resource and cleanup afterward
# This pattern will be important when we start writing database-backed CRUD endpoints.

# --------------------

# 4. VERIFY YOUR DATABASE CONNECTION

# lets test whether SQLAlchemy can establish a SQLite connection
# python -c "from app.database import engine; connection = engine.connect(); print('Database connection successful!'); connection.close()"

# --------------------

# 7. Day 6 review questions
# After completing the implementation, answer these in your own words:
# 1. What is the responsibility of SQLAlchemy's Engine?
# 2. What information does a database URL contain?
# 3. What's the difference between engine and SessionLocal?
# 4. Why do we use autocommit=False?
# 5. Why does get_db() use yield and finally?
# 6. What is the difference between SessionLocal and db = SessionLocal()?

# 1. sqlalchemy's engine is responsible for database connectivity, and connection pooling infrastructure maintenance and it is established using DATABASE_URL and an appropriate drive, and SESSION on the other hand is responsible for the database INTERACTION & TRANSACTIONS and it provides an interface for performing database iteractions.
# 2. Database url tells the SQLAlchemy to which database and drive to use
# 3. engines is responsible for database connectivity and SessionLocal is a factory to create session instances
# 4. autocomit=False avoids automatically commiting the database transaction, and demands explicit transaction commit
# 5. get_db() use yield because fastapi supports dependencies with YIELD, allowing setup before providing resouce and cleanup afterward. this pattern will be important when we start writing database-backed CRUD endpoints
# 6. SessionLocal is a session instance creating factory class and db=SessionLocal() is reall session here.

# --------------------