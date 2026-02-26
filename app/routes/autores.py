from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/autores", tags=["Autores"])

@router.get("/", response_model=List[schemas.Autor])
def leer_autores(db: Session = Depends(get_db)):
    return crud.get_autores(db)

@router.post("/", response_model=schemas.Autor)
def crear_nuevo_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return crud.crear_autor(db=db, autor=autor)