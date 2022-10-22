from pydantic import BaseModel, EmailStr
from datetime import date
class Createuser(BaseModel):
    email: EmailStr
    password: str

class CreateItem(BaseModel):
    title: str
    description: str


class Showuser(BaseModel):
    id : int
    email: EmailStr
    is_active: bool
    
    class Config:
        orm_mode=True

class Showitem(BaseModel):
    title: str
    description : str
    date_posted : date
    
    class Config:
        orm_mode=True