from fastapi import APIRouter, status
from fastapi import File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from typing import Optional

router = APIRouter(prefix="/candidates")

class Candidate(BaseModel):
    first_name : str

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
    phone_number : str = Form(...),
    cv : UploadFile = File(...),
    cover_letter : Optional[str|None] = Form(default=None)
):
    #insert to database
    print(first_name)

    with open(cv.filename,"wb") as f:
        f.write(cv.file.read())
    cv.file.close()
    return JSONResponse({"status":"Form successfully"}, status_code=status.HTTP_200_OK)