from fastapi import FastAPI
from config import setting
from database import engine
from models import Base
from routers import users, items , login

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=setting.title,
    description=setting.description,
    version=setting.version,
    terms_of_service=setting.terms_of_service,
    contact=setting.contact,
    license_info=setting.license_info,
    openapi_tags=setting.tags_metadata
)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router)

