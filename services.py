from sqlalchemy.orm import Session
from models import Expense
from models import Salary                
from sqlalchemy import extract

def create_expense(db: Session,expense):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_all_expenses(db:Session):
    return db.query(Expense).all()

def get_expenses_by_month(db,year:int,month:int):
    return db.query(Expense).filter(extract('year',Expense.created_at) ==year,extract('month',Expense.created_at) == month).all()

def get_totals(db):
    total_expense = db.query(func.sum(Expense.amount)).scalar() or 0
    total_salary = db.query(func.sum(Salary.amount)).scalar() or 0

    remaining = total_salary - total_expense
    return {total_expense: total_expense,
            total_salary: total_salary,
            "remaining_amount": remaining}