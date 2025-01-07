from typing import Annotated
from sqlalchemy.orm import Session 
from fastapi import Depends
from database import SessionLocal

#dependency to get db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]