from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

import models
import squema
import crud
from sqlalchemy.orm import Session
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/positions")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def positions(position : squema.Position , db: Session = Depends(get_db)):
    new_position = crud.create_position(db,position)
    return JSONResponse(new_position,status_code=status.HTTP_200_OK)

@router.get("/get_positions")
async def get_positions(active:bool=False,db: Session = Depends(get_db)):
    post_clean = []
    posts :list[dict] = crud.get_position(db)
    try:
        for post in posts:
            
            post.functions = post.functions.split("|")
            
            post.requirements = post.requirements.split("|")
            
            post.desirable = post.desirable.split("|")
            post_clean.append(post.__dict__)
            
        return post_clean
    except Exception as e:
        return {"err":e}
    

