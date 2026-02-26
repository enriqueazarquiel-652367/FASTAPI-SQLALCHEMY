from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.get("/", response_model=List[schemas.Libro])
def leer_libros(db: Session = Depends(get_db)):
    return crud.get_libros(db)

@router.post("/", response_model=schemas.Libro)
def crear_nuevo_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.crear_libro(db=db, libro=libro)