from pydantic import BaseModel
from typing import List, Optional

# --- Esquemas para LIBROS ---
class LibroBase(BaseModel):
    titulo: str
    genero: Optional[str] = None
    precio: float
    paginas: int

class LibroCreate(LibroBase):
    autor_id: int  # Necesario para crear un libro vinculado a un autor

class Libro(LibroBase):
    id: int
    autor_id: int

    class Config:
        from_attributes = True

# --- Esquemas para AUTORES ---
class AutorBase(BaseModel):
    nombre: str
    nacionalidad: Optional[str] = None
    edad: Optional[int] = None
    esta_vivo: bool = True

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    id: int
    libros: List[Libro] = [] # Al pedir un autor, veremos sus libros

    class Config:
        from_attributes = True