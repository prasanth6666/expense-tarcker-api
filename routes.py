from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services import *

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        @router.post("/expenses/")
        def create(expense,db:Session =Depends(get_db)):
            return create_expense(db,expense)
        
        @router.get("/expenses/")
        def get_all(db:Session = Depends(get_db)):
            return get_all_expenses(db)
