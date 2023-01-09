from datetime import date,datetime
from pydantic import BaseModel
from typing import List
from models import Teacher

class Teacher(BaseModel):
    id: int
    name: str
    age: int
    birthday: datetime
    gender :str
    address: str
    city: str