from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from utils import OAuth2PasswordBearerWithCookie
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from models import Users
from hashing import Hasher
from jose import jwt
from config import setting

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


router = APIRouter()

# @router.post("/login/token" , tags=["login"])
# def createtoken(response: Response,formdata: OAuth2PasswordRequestForm=Depends() , db:Session=Depends(get_db)):
#     user=db.query(Users).filter(Users.email==formdata.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Email")
#     if not Hasher.verify_password(formdata.password,user.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Password")

#     data = {"sub" : formdata.username}
#     jwt_token=jwt.encode(data, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
#     response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
#     return {"acces_token" : jwt_token , "type" : "Bearer"}


@router.post("/login/token")
def retrieve_token_for_authenticated_user(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(Users).filter(Users.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username"
        )
    if not Hasher.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password"
        )
    data = {"sub": form_data.username}
    jwt_token = jwt.encode(data, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
    return {"access_token": jwt_token, "token_type": "bearer"}