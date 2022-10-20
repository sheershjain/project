from pydantic import BaseModel, EmailStr

class Createuser(BaseModel):
    email: EmailStr
    password: str