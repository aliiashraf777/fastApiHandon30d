# 2fastApi\1fastApiHandon30d\1fapid1\app\handonTuts\6sqlAlchemyBasic.py

# Day5 - Phase4: SQLAlchemy Foundations

# Today's Object: Understand how SQLAlchemy connect PYTHON CLASSES to DATABASE TABLES and create your 1st ORM MODEL

# expenses_data_list=[
#     {"id": 101, "title": "Office supplies", "amount": 2500}
# ]

# as we are using PYTHON LIST for CRUD
# but this is temporary storage, when the application restarts the server, the changes disappear
# with SQLAlchemy, we'll eventually replace that list with a database table

# ---------------------

# Here's the architecture we're building towards:
# 1.
# FastAPI Router
# Receives HTTP requests
# 2.
# SQLAlchemy Session
# Manages database interactions
# 2
# SQLAlchemy ORM Model
# Maps Python classes to database tables
# 3
# Database
# Stores persistent records

# -----------------------

# IMP CONCEPTS here

# CONCEPT   RESPONSIBILITY
# ENGINE - Manages the database connection INFRASTRUCTURE
# SESION - Manages INTERACTIONS & TRANSACTIONS with the DB
# BASE - Provides the FOUNDATION for defining ORM MODELS
# MODEL - Represents a DataBase Table through a PYTHON CLASS

# e.g
# Expense is a Python class
# SQLAlchemy maps it to an "expenses" database table
# Each Expense OBJECT represents a DATABASE RECORD

# -------------

# INSTALL SQLALCHEMY

# 1. check is it installed or not
# pip show sqlalchemy 
# 2. 
# pip install sqlalchmey
# 3. 
# python -c "import sqlalchemy; print(sqlalchemy.__version__)"

# ----------------

# Database Foundation

# app/
# ├── database.py
# ├── main.py
# ├── models/
# │   ├── __init__.py
# │   └── expense.py
# ├── routers/
# └── schemas/

# ----------------

# PYDATIC SCHEMA V/S SQLALchemy MODEL

# pydantic schemas - valides incoming and outgoing API data
# sqlalchemy - defines how application data is represented in DB

# ----------------

# VERIFY YOUR ORM MODEL

# create a temporary verification command in your terminal

# python -c "from app.models.expense import ExpenseORM; print(ExpenseORM.__tablename__); print(list(ExpenseORM.__table__.columns.keys()))"

# ---------------

# IMPORTANT BUILDING BLOCKS

# ENGINE
# the engine is resonsible for database CONNECTIVITY and CONNECTION POOLING. it is configured using DataBase URL and an appropriate DRIVER

# SESSION
# A session is responsible for INTERACTION & TRANSACTION with DATABASE.
# and its the INTERFACE through which your application performs database operations.

# e.g, eventually

# db.add(new_expense)
# db.commit()
# db.refresh(new_expense)

# add() - stages an object for insertion
# commit() - commits the transaction
# refresh() - reloads the object from the database

# ----------------

# SESSION DEPENDENCY

# FastAPI commonly uses a DEPENDENCY to provide a DATABASE SESSION to each REQUEST, and ENSURES that the session is CLOSED afterward.

# ----------------

# DAY5 REVIEW QUSTIONS

# Once you've implemented and verified the code, answer these in your own words:
# 1. What's the difference between a Pydantic schema and a SQLAlchemy model?
# 2. Why does Expense inherit from Base?
# 3. What does __tablename__ = "expenses" do?
# 4. What's the difference between an Engine and a Session?
# 5. Why do we use primary_key=True for the id column?

# 1. pydantic schema validates the incoming and outgoing API data; SQLAlchemy defines how the data of application is represented in the DATABASE.
# 2. Base is the shared FOUNDATION of our application and all database models is being inherited from this class. SQLAlchemy uses these models to understand our database table structure
# 3. __tablename__ = "expnses_tb" it declares the name of the database table to which the ORM model maps, it does not, by itself, create the physical table in our database.
# 4. Engine is responsible for database connectivity and connection pooling, it is configured using DATABASE URL and an appropriate diver. Sesion is resonsible for INTERACTION & TRANSACTION with Database, and it is the interface through which your application performs database operations, and FastAPI uses a foundation to provide each REQUEST a SESSION and ensures that the session is closed afterwards.
# 5. we make id a primary_key using primary_key=True, the reason is that a PRIMARY_KEY UNIQUELY identifies each databaes record. every record has a unique identifier. this makes it possible to retrieve, update, delete, a particular record reliabley. A primary key must be unique and NO-NULL.