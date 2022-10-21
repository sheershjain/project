from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
import os
import sys
sys.path.append("../")
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

from database import get_db,engine
from models import Base

SQLALCHEMY_DATABASE_URL='sqlite:///test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client=TestClient(app)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)



app.dependency_overrides[get_db]=override_get_db

def test_create_user():
    data = {"email" : "khushi@gkmit.co" , "password" : "khushi"}
    response = client.post("/users" , json.dumps(data))
    assert response.status_code==200
    assert response.json()["email"] == "khushi@gkmit.co"
    assert response.json()["is_active"] == True

    
