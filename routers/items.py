from fastapi import APIRouter, Depends , HTTPException,status
from database import get_db
from typing import List
from schemas import CreateItem,Showitem
from models import Items
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder


router=APIRouter()




@router.post("/items",tags=["Items"], response_model=Showitem)
def create_items(item: CreateItem , db: Session= Depends(get_db)):
    date=datetime.now().date()
    owner_id=1
    item=Items(**item.dict(),date_posted=date, owner_id=owner_id) 
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/items/{id}",tags=["Items"] )
def update_items(id: int , obj: CreateItem , db: Session= Depends(get_db)):
    ref=db.query(Items).filter(Items.id==id)
    if not ref.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Item with id {id} not exist")
    
    # ref.update(jsonable_encoder(obj))
    ref.update(obj.__dict__)
    db.commit()
    return {"message" : "Item updated successfully"}

@router.delete("/items/{id}",tags=["Items"] )
def delete_items(id: int , db: Session= Depends(get_db)):
    ref=db.query(Items).filter(Items.id==id)
    if not ref.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Item with id {id} not exist")
    
    ref.delete()
    db.commit()
    return {"message" : "Item deleted successfully"}


@router.get("/items/all",tags=["Items"], response_model=List[Showitem])
def read_items(db: Session= Depends(get_db)):
    items=db.query(Items).all()
    return items

@router.get("/items/{id}",tags=["Items"], response_model=Showitem)
def read_items(id: int, db: Session= Depends(get_db)):
    item=db.query(Items).filter(Items.id==id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Item with id {id} not exist")
    return item

