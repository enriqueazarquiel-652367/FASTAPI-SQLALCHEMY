from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import autores, libros # Importar las rutas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi Biblioteca API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluimos los routers
app.include_router(autores.router)
app.include_router(libros.router)

@app.get("/")
def read_root():
    return {"mensaje": "API de Biblioteca lista. Ve a /docs para probarla."}