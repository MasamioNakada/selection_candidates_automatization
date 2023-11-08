import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
server = os.getenv("SERVER")
port = os.getenv("PORT")
database = os.getenv("DATABASE")

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{server}:{port}/{database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker( autoflush=True, bind=engine)

Base = declarative_base()