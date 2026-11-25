# 3FastApiHandon\1fapid1\app\handonTuts\8sqlAlchemyTableCreation.py

# Day 7 - Phase 4: SQLAlchemy Table Creation, Metadata & Model Registration

# Todays' Objective: Understand 
# how SQLAlchemy discovers ORM models,
# collect their table definitions in metadata
# and create actual database tables

# main files: 
# app/database.py
# app/models/expense.py

# --------------
# MODEL VS. TABLE

# class ExpenseORM(Base):
#     __tablename__ = "expense_tb"

#     id: Mapped[int] = mapped_column(Ineter, primary_key=True)
#     title: Mapped[str] = mapped_column(String, nullable=False)
#     amount: Mapped[int] = mapped_column(Integer, nullable=False)

# defining this python class does not automatically creates physical database table.

# ---------------

# 3 IMPORTANT STAGES

# 1.
# ORM Model
# Defines the database table and its columns

# 2.
# SQLAlchemy Metadata
# collects registered tables definitions

# 3.
# Physical Database Table
# created inside SQLite

# Think of METADATA AS A COLLECTION OF INFORMATION ABOUT THE TABLES YOUR APPLICATION DEFINES.

# ----------------

# MODEL REGISTRATION

# class ExpenseORM(Base):
# __tablename__ = "expense_tb"

# this inheritance registers its table definition with the metadata associated with Base.

# inpect this metadas
# python -c "from app.database import Base; from app.models.expense import ExpenseORM; print(Base.metadata.tables)"

# IMPORTANT: SQLALCHEMY MUST IMPORT THE MODEL MODULE BEFORE THAT MODEL'S TABLE DEFINITION BECOMES REGISTERED IN METADATA

# for example: importing BASE alone does not automatically import every model in your application.
# this is very important concept when your project has mutliple model files.

# --------------

# UNDERSTAND BASE.METADATA.CREATE_ALL()

# Base.metadata.create(bind=engine)

# Base - application declarative foundation model
# Base.metadata - collection of registered table definitions
# create_all() - creates missing tables
# bind=engine - specifices which database engine to use

# simply
# create_all() examines the registered table definitions and creates tables that don't already exists in the CONNECTED DATABASE.

# IT DOES NOT AUTOMATICALLY UPDATE AN EXISTING TABLE WHEN YOU CHANGE YOUR PYTHON MODEL.
# that's one reason production applications use ALEMBIC MIGRATIONS.

# ----------------

# TABLE CREATION

# def create_tables():
#     Base.metadata.create_all(bind=engine)

# add at the end of
# app/database.py

# we need to ensure that the model has been imported before calling create_tables() - well explained in below file

# 3FastApiHandon\1fapid1\app\create_db.py

# why import ExpenseORM
# because importing this module executes its class definition and registers expense_tb in Base.metadata
# the imported class isn't otherwise used in this file. Its import ensures registration before table creation

# -----------------

# EXECUTE AND VERIFY TABLE CREATION

# now execute create_db.py file in project root

# now verify tables exists?!

# print -c "from sqlalchemy import inspect; from app.database import engine; inspector = inspect(engine); print(inspector.get_table_names())"
# print -c "
# from sqlalchemy import inspect;
# from app.database import engine;
# inspector = inspect(engine);
# print(inspector.get_table_names())
# "

# INSPECT DATABASE TABLE COLUMNS
# python -c "from sqlalchemy import inspect; from app.database import engine; inspector = inspect(engine); print(inspector.get_columns('expense_tb'))"

# ------------

# IMPORTANT LIMITAION 

# what happens if you add another column to your SQLAlchemy MODEL

# description: Mapped[str] = mapped_column(String(200), nullable=True)

# then run

# Base.metadata.create_all(bind=engine)

# WILL SQLALCHEMY AUTOMATICALLY ADD THE NEW COLUMN TO YOUR EXISTING TABLE???!!!!

# NOOOOO!

# create_all() creates MISSING TABLES; IT DOES NOT MIGRATE EXISTING TABLES to match MODIFIED PYDANTIC MODELS.

# DISTINCTION MATTTERS THE MOST
# CREATE_ALL(): creates missing tables; it does not migrate existing tables to match modified pydantic models
# ALEMBIC: manages database schemas changes throught migrations.

# ------------------

# DAY 7 REVIEW QUESTIONS

# After implementation, answer these in your own words:
# 1. What's the difference between an ORM model and a physical database table?
# 2. What is SQLAlchemy metadata?
# 3. Why must we import ExpenseORM before calling create_all()?
# 4. What does Base.metadata.create_all(bind=engine) do?
# 5. If you add a new column to an existing model and run create_all() again, will the database table automatically gain that column? Why?
# 6. What's the difference between create_all() and Alembic migrations?

# 1. SQLAlchemy ORM model defines the structure of database table, it doesn't creat physical database table automatically, we need to create physical database table using creat_all(bind=engine)
# 2. SQLAlchemy metadata is the collection of definition of registered database tables.
# 3. we import ExpenseORM because importing it, executes its class and before calling create_all() the definition of databse table got registered in Base.metadata, and its most imporatnt we need to first register the databse table before executing create_all()
# 4. Base.metadata.create_all(bind=engine), it examines the tables registered in Base.metadata and creates any missing table in DATABASE ASSOCIATED with the SPECIFIED ENGINE.
# 5+6. create_all() only creates existing database tables it does not automatically run migrations to update the existing database tables according to changed sqlalchemy model, that's why we use ALEMGIC in production to automatically update the database columns as per database scheme models updates.