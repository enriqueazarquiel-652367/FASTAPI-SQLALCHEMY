from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./biblioteca.db" # URL de la base de datos

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # Creamos el engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Creamos la sesión
Base = declarative_base() # Creamos la base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()