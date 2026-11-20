# 3FastApiHandon\1fapid1\app\models\expense.py

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class ExpenseORM(Base):
    __tablename__ = "expense_tb"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    
# ------------
# Imp Parts

# class ExpenseORM(Base) - creates an ORM Model
# __tablename__ - defines the database table name
# Mapped[int] - declares the Python Type of the mapped FIELD
# mapped_column - defines a database column
# primary_key=True - makes ID the primary key
# nullable=False - Prevents the column from storing NULL

# VERIFY YOUR ORM MODEL

# python -c "from app.models.expense import ExpenseORM; print(ExpenseORM.__tablename__); print(list(ExpenseORM.__table__.columns.keys()))"