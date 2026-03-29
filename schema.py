from pydantic import BaseModel
class ExpenseCreate(BaseModel):
    name:str
    amount:float
    category:str
class ExpenseResponse(ExpenseCreate):
    id:int

    class Config:
        from_attributes = True
