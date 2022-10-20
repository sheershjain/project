from pydantic import BaseModel, EmailStr

class Createuser(BaseModel):
    email: EmailStr
    password: str

class Showuser(BaseModel):
    id : int
    email: EmailStr
    is_active: bool
    
    class Config:
        orm_mode=True