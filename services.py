from sqlalchemy.orm import Session
from models import Expense

def create_expense(db: Session,expense):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_all_expenses(db:Session):
    return db.query(Expense).all()
