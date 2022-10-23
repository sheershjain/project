from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

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


@pytest.fixture
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close() 
    
    app.dependency_overrides[get_db]=override_get_db
    client=TestClient(app)
    yield client 
