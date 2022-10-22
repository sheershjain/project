from fastapi import APIRouter, Depends
from database import get_db
from schemas import CreateItem,Showitem
from models import Items
from sqlalchemy.orm import Session
from datetime import datetime
router=APIRouter()


@router.get("/items",tags=["Items"])
async def read_items():
    return [{"message": "hello Users"}]

@router.post("/items",tags=["Items"], response_model=Showitem)
async def create_items(item: CreateItem , db: Session= Depends(get_db)):
    date=datetime.now().date()
    owner_id=1
    item=Items(**item.dict(),date_posted=date, owner_id=owner_id) 
    db.add(item)
    db.commit()
    db.refresh(item)
    return item