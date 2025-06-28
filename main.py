from fastapi import FastAPI
from database import Base, engine
from api import routes  # si tus rutas están agrupadas ahí

app = FastAPI()

# Crea las tablas
Base.metadata.create_all(bind=engine)

# Incluye las rutas
app.include_router(routes.router)
