import os
from dotenv import load_dotenv
import boto3

from sqlalchemy.orm import Session

import squema
import models

load_dotenv()

access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")
endpoint_url = os.getenv("STORJ_EP")

def create_candidate(db:Session, candidate:squema.Candidate):

    candidate = candidate.model_dump()

    candidate_table = squema.CandidateTable(
        first_name=candidate["first_name"],
        middle_name=candidate["middle_name"],
        last_name=candidate["last_name"],
        gender=candidate["gender"],
        email=candidate["email"],
        country_code=candidate["country_code"],
        phone_number=candidate["phone_number"],
        cv_path = candidate["cv_path"]
    )

    new_candidate = models.Candidate(
        **candidate_table.model_dump(exclude_none=True)
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    intention = models.CandidateIntention(
        id_candidate = new_candidate.id,
        id_position = candidate["id_position"],
        cover_letter = candidate["cover_letter"],
        status = "pending"
    )

    db.add(intention)
    db.commit()
    
def get_candidates(db:Session):
    candidates = db.query(models.Candidate).all()
    return candidates

def create_position(db:Session, candidate:squema.Position):

    new_position = models.Positions(
        **candidate.model_dump(exclude_none=True)
    )

    db.add(new_position)
    db.commit()
    return {"position_id":new_position.id}

def get_position(db:Session,active:bool=False):
    if active:
        positions = db.query(models.Positions).filter(models.Positions.status == active).all()
    else:
        positions = db.query(models.Positions).all()

    return positions

def upload_file(file,name):
    s3 = boto3.client(
        's3',
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        endpoint_url = endpoint_url
    )

    res = s3.upload_fileobj(
        file.file,'curriculums',name
    )

