# 3FastApiHandon\1fapid1\app\database.py

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# important concepts
# DeclarativeBase - is SQLAlchemy's base class for declarative ORM models.
# Base - is your project's shared foundation
# Your database models will inherit from this class
# SQLAlchemy - uses these models to understand your database table structure.