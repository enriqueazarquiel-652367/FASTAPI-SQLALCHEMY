from sqlalchemy.orm import Session
from app import models, schemas

# --- OPERACIONES PARA AUTORES ---
def get_autores(db: Session):
    return db.query(models.Autor).all()

def crear_autor(db: Session, autor: schemas.AutorCreate):
    db_autor = models.Autor(
        nombre=autor.nombre,
        nacionalidad=autor.nacionalidad,
        edad=autor.edad,
        esta_vivo=autor.esta_vivo
    )
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

# --- OPERACIONES PARA LIBROS ---
def get_libros(db: Session):
    return db.query(models.Libro).all()

def crear_libro(db: Session, libro: schemas.LibroCreate):
    db_libro = models.Libro(**libro.model_dump())
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro