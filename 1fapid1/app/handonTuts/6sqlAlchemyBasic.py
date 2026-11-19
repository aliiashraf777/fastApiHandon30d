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

# create a temporary verification comman in your terminal

# python -c "from app.models.expense import Expense; print(ExpenseORM.__tablename__); print(list(ExpenseORM.__tablename__.columns.keys()))"