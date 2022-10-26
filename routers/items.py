from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from typing import List
from schemas import CreateItem, Showitem
from models import Items, Users
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from routers.login import oauth2_scheme
from jose import jwt
from config import setting

router = APIRouter()


# @router.post("/items",tags=["Items"], response_model=Showitem)
# def create_items(item: CreateItem , db: Session= Depends(get_db),token:str=Depends(oauth2_scheme)):

#     try:
#         payload=jwt.decode(token, 'SHEERSH', algorithms=['HS256'])
#         username=payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials1")
#         user=db.query(Users).filter(Users.email==username).first()
#         if user is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials2")
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials3")
#     date=datetime.now().date()
#     owner_id=user.id
#     item=Items(**item.dict(),date_posted=date, owner_id=owner_id)
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item


def get_user_from_token(db, token):
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, setting.ALGORITHM)
        username = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate Credentials",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate Credetials",
        )
    user = db.query(Users).filter(Users.email == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return user


@router.post("/item", tags=["Items"], response_model=Showitem)
def create_item(
    item: CreateItem, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    user = get_user_from_token(db, token)
    owner_id = user.id
    item = Items(**item.dict(), date_posted=datetime.now().date(), owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/items/{id}", tags=["Items"])
def update_items(
    id: int,
    obj: CreateItem,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if existing_item.first() is None:
        return {"message": f"No Details found for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        # ref.update(jsonable_encoder(obj))
        existing_item.update(obj.__dict__)
        db.commit()
        return {"message": "Item updated successfully"}
    else:
        return {"message": "You are not authorized"}


# @router.delete("/items/{id}",tags=["Items"] )
# def delete_items(id: int , db: Session= Depends(get_db)):
#     ref=db.query(Items).filter(Items.id==id)
#     if not ref.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Item with id {id} not exist")
#     ref.delete()
#     db.commit()
#     return {"message" : "Item deleted successfully"}


@router.delete("/item/delete/{id}", tags=["Items"])
def delete_item_by_id(
    id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.delete()
        db.commit()
        return {"message": f"Item ID {id} has been successfully deleted"}
    else:
        return {"message": "You are not authorized"}


@router.get("/items/all", tags=["Items"], response_model=List[Showitem])
def read_items(db: Session = Depends(get_db)):
    items = db.query(Items).all()
    return items


@router.get("/items/{id}", tags=["Items"], response_model=Showitem)
def read_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not exist"
        )
    return item
