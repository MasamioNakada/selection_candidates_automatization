from pydantic import BaseModel
from typing import Optional

class Candidate(BaseModel):
    first_name : str
    middle_name : Optional[str]
    last_name : str
    gender : str
    email : str
    country_code : str
    phone_number : str
    id_position : int
    cover_letter:str
    cv_path:str

class CandidateTable(BaseModel):
    first_name:str
    middle_name:Optional[str|None]=None
    last_name:str
    gender:Optional[str|None]=None
    email:str
    country_code:str
    phone_number:str
    cv_path:str

class CandidateIntention(BaseModel):
    id_candidate : int
    id_position : int
    cover_letter : int
    status : str
    result : dict

class Position(BaseModel):
    name : str
    department : str 
    functions : str  
    requirements : str
    desirable : Optional[str]
    mode : dict
    status : bool = True




