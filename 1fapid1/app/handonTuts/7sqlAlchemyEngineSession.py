# 3FastApiHandon\1fapid1\app\handonTuts\7sqlAlchemyEngineSession.py

# Day 6 — Phase 4: SQLAlchemy Engine, Database URLs & Sessions

# Todays' Objective: 
# understand how SQLAlchemy establishes database connection, 
# how database URLs works,
# how sessions manage database interactions

# ----------------

# SQLITE
# we'll use SQLite temporarily to understand the CONNECTION MECHANICS without introduction PostgreSql, MySQL configuration before their dedicated phases

# ----------------

# UNDERSTAND CONNECTION ARCHITECTURE

# as we know
# Base - defines the ORM foundation
# ExpenseORM - maps a Python class to a Database Table

# Today, we'll add the ENGINE & SESSION

# 1
# FastAPI endpoint
# recieves the request
# 2
# Database Session
# Performs the database operations and transactions
# 3
# Database Engine
# Manages database Connectivity and connection pooling
# 4
# SQLite Database
# stores the data

# Think of it this way:
# -Engine: Establishes database connectivity and connection pooling infrastructure
# -Session: manages the database interactions and transactions and provides the interface for working with database records.
# -DatabaseURL: Tells the SQLAlchemy which DB and Driver to use

# ---------------

# UNDERSTAND DB URLs

# A database URL tells the SQLAlchemy how to connect to a databae.

# dialect+driver://username:password@host:port/database_name

# 1-PostgresSQL URL
# postgresql+psycopg2://username:password@localhost:5432/fnow_db

# 2-MySQL URL
# mysql+pymysql://username:password@localhost:3306/filernow_db

# 3-SQLite URL
# sqlite:///./expenses.db

# SQLite doesn't require a username, password, host, or port.

# ---------------

# 4. VERIFY YOUR DATABASE CONNECTION

# lets test whether SQLAlchemy can establish a SQLite connection
# python -c "from app.database import engine; connection = engine.connect(); print('Database connection successful!'); connection.close()"

# ---------------