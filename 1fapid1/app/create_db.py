# 3FastApiHandon\1fapid1\app\create_db.py

from app.database import create_tables
from app.models.expense import ExpenseORM

create_tables()

print("Database tables created successfully")

# why import ExpenseORM
# because importing this module executes its class definition and registers expense_tb in Base.metadata
# the imported class isn't otherwise used in this file. Its import ensures registration before table creation