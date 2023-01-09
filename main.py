from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
import models,schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
#     allow_credentials=True,
# )

# Dependency
def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.post("/create-teacher/")
def create_teacher(teacher:schemas.Teacher,   session = Depends(get_session)):
    id = models.Teacher(id=teacher.id)
    name = models.Teacher(name=teacher.name)
    age = models.Teacher(age=teacher.age)
    birthday=models.Teacher(birthday=teacher.birthday)
    gender = models.Teacher(gender=teacher.gender)
    address = models.Teacher(address=teacher.address)
    city = models.Teacher(city=teacher.city)
    session.add(name,age)
    session.add(birthday,gender)
    session.add(address,city)
    session.commit()
    return id


@app.get('/get-teacher/')
def get_teacher(session: Session = Depends(get_session)):
    teacher = session.query(models.Teacher).all()
    return teacher

@app.get('/get-teacher/{id}')
def get_teacher_by_id(id: int,session: Session = Depends(get_session)):
    teacher = session.query(models.Teacher).filter(models.Teacher.id == id).first()
    return teacher
    

@app.put('/update-teacher/{id}')
def update_teacher(id:int,teacher:schemas.Teacher,session:Session = Depends(get_session)):
    up_teacher = session.query(models.Teacher).get(id)
    up_teacher.name = teacher.name
    up_teacher.age = teacher.age
    up_teacher.birthday = teacher.birthday
    up_teacher.gender = teacher.gender
    up_teacher.address = teacher.address
    up_teacher.city = teacher.city
    session.add(up_teacher)
    session.commit()
    print(up_teacher)
    return up_teacher



@app.delete('/delete-teacher/{id}')
def delete_teacher(id:int, session=Depends(get_session)):
    teacher = session.query(models.Teacher).get(id)
    session.delete(teacher)
    session.commit()
    session.close()
    return  'deleted'
    
    
    
            
        
        
        