from sqlite3 import version
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

class Settings:
    title="ChimichangApp"
    description="""
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""
    version="0.0.1"
    terms_of_service="http://example.com/terms/"
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    }
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    DATABASE_URL= os.getenv("POSTGRES_URL")


    

setting=Settings()