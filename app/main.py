from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importar esto
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi Biblioteca API")

# Configuración del CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción aquí pondrías la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "API funcionando con CORS y Esquemas listos"}