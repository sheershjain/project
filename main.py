from fastapi import FastAPI
from config import setting
from database import engine
from database import engine
from models import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=setting.title,
    description=setting.description,
    version=setting.version,
    terms_of_service=setting.terms_of_service,
    contact=setting.contact,
    license_info=setting.license_info

)


@app.get("/",tags=["items"])
async def read_items():
    return [{"name": "Katana"}]
