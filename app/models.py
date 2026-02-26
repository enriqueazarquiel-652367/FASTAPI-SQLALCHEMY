from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    nacionalidad = Column(String)
    edad = Column(Integer)
    esta_vivo = Column(Boolean, default=True)

    # uun autor tiene muchos libros
    libros = relationship("Libro", back_populates="autor")

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    genero = Column(String)
    precio = Column(Float)
    paginas = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autores.id"))

    # el libro pertenece a un autor
    autor = relationship("Autor", back_populates="libros")