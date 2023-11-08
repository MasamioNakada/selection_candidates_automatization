from fastapi import APIRouter, status, Depends
from fastapi import File, UploadFile, Form
from fastapi.responses import JSONResponse

import utils
import models
import squema
import crud
from sqlalchemy.orm import Session
from database import SessionLocal, engine

from typing import Optional

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/candidates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/positions")
async def positions():
    #search in database
    positions = [
        {"id":1,"position":"Asistente de Proyecto","status":True},
        {"id":2,"position":"Data Engineer","status":True},
        {"id":3,"position":"Pizza","status":False},
    ]
    return JSONResponse({"positions":positions},status_code=status.HTTP_200_OK)

@router.get("/info_form")
async def info_form(id:str):
    #busca en la base de datos
    if id == "1":
        return JSONResponse({
            "title":"Asistente de Proyectos",
            "description":"""SuperLearner es unaONG sin fines de lucro enfocado en el desarrollo de programas sociales sostenibles que promuevan el desarrollo integral, contribuyan a la mejorar calidad de vida y oportunidades de los niños, niñas, adolescentes y jóvenes de comunidades vulnerables.

Estamos en busca de individuos proactivos, con un fuerte espíritu de servicio y el deseo de contribuir a la mejora de la sociedad, especialmente en las comunidades más vulnerables. ¿Listo para marcar la diferencia? Únete a Superlearner y forma parte del cambio."""
        })
    else:
        return JSONResponse({
            "title":"Join to Superlearner",
            "description":"""SuperLearner es unaONG sin fines de lucro enfocado en el desarrollo de programas sociales sostenibles que promuevan el desarrollo integral, contribuyan a la mejorar calidad de vida y oportunidades de los niños, niñas, adolescentes y jóvenes de comunidades vulnerables.

Estamos en busca de individuos proactivos, con un fuerte espíritu de servicio y el deseo de contribuir a la mejora de la sociedad, especialmente en las comunidades más vulnerables. ¿Listo para marcar la diferencia? Únete a Superlearner y forma parte del cambio."""
        })

@router.post("/register")
async def create_user(
    form_id:str =Form(...),
    first_name: str = Form(...),
    middle_name : Optional[str|None] = Form(default=None),
    last_name : str = Form(...),
    gender : Optional[str|None] = Form(default=None),
    email : str = Form(...) ,
    country_code : Optional[str|None] = Form(default=None),
    phone_number : str = Form(...),
    cv : UploadFile = File(...),
    cover_letter : Optional[str|None] = Form(default=None),
    db:Session = Depends(get_db)
):  
    cv_path = f"{first_name}_{last_name}_{utils.rand_string()}.pdf"
    candidate = squema.Candidate(
        first_name=first_name,
        middle_name=middle_name,
        last_name = last_name,
        gender = gender,
        email = email,
        country_code = country_code,
        phone_number = phone_number,
        cover_letter = cover_letter,
        id_position = form_id,
        cv_path = cv_path
    )

    #insert to database
    crud.upload_file(cv,name=cv_path)
    cv.file.close()
    db_candidate = crud.create_candidate(db,candidate)
    
    return JSONResponse({"status":"Form successfully"}, status_code=status.HTTP_200_OK)

@router.get("/all")
async def get_user(db: Session = Depends(get_db)):
    return crud.get_candidates(db)