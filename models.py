from sqlalchemy import Column, ForeignKey, Integer,String, Boolean,JSON,Text
from sqlalchemy.orm import relationship

from database import Base

class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True,index=True,autoincrement=True, unique=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    gender =Column(String)
    email = Column(String)
    country_code = Column(Integer)
    phone_number = Column(Integer)
    cv_path = Column(String)


class Positions(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True,index=True,autoincrement=True, unique=True)
    name = Column(String)
    department = Column(String)
    functions = Column(Text)
    requirements = Column(Text)
    desirable = Column(Text)
    mode = Column(JSON)
    status = Column(Boolean, default=True)


class CandidateIntention(Base):
    __tablename__ = "candidate_intention"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    id_candidate = Column(Integer)
    id_position = Column(Integer)
    cover_letter = Column(Text)
    status = Column(String)
    results = Column(JSON)

