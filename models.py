from email.policy import default
from enum import unique
from sqlalchemy import Column, Integer, String , ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ =  "users"

    id = Column(Integer,primary_key = True)
    email = Column(String,nullable= False)
    password = Column(String,nullable= False)
    is_active = Column(Boolean, default=True)
    items = relationship("Items", back_populates="owner")

class Items(Base):
    __tablename__ =  "items"

    id = Column(Integer,primary_key = True,index=True)
    title = Column(String,nullable= False,unique=True)
    description = Column(String,nullable= False)
    owner_id = Column(Integer , ForeignKey("users.id"))

    owner = relationship("Users", back_populates="items")