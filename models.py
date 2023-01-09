from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date,DateTime
from db import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    age = Column(Integer)
    birthday = Column(DateTime)
    gender = Column(String(256))
    address = Column(String(256))
    city = Column(String(256))
    
