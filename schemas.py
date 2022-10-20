from pydantic import BaseModel, EmailStr

class Item(BaseModel):
    email: str
    password: EmailStr