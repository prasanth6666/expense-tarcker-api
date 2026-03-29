from sqlalchemy import Column,Integer,String,Float
from datetime import datetime
from database import Base

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer,primary_key=True,index=True)
    name= Column(String(255))
    amount = Column(Float)
    category = Column(String(255))
    created_at = Column(DateTime,default=datetime.now)
                    
class Salary(Base):
    __tablename__ = "salary"
    id = Column(Integer,primary_key =True,index = True)
    amount = Column(Float)
