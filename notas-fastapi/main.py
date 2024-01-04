from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.rutas import router_notas
from app.db import create_tables

app = FastAPI()
app.title = 'Ejemplo FastAPI'

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.on_event("startup")
def on_starup():
    create_tables()



@app.get('/',tags=['Bienvenido'])
def bienvenido():
    return {'Bienvenido':'a la app'}

app.include_router(router_notas)


# if __name__ == '__main__':
#     uvicorn.run('main:app',port=8000,reload=True)