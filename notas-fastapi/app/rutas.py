from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.models import NotaCrear,NotaLeer,NotaUpdate
from app.db import get_db
from app.crud import leer_notas,crear_nota,obtener_nota,eliminar_nota,actualizar_nota


router_notas = APIRouter(prefix='/nota', tags=['Nota'])


@router_notas.get('/',response_model=List[NotaLeer])
def leer(db:Session=Depends(get_db)):
    return leer_notas(db=db)


@router_notas.post('/',response_model=NotaLeer)
def agregar(nota:NotaCrear,db:Session=Depends(get_db)):
    return crear_nota(nota=nota,db=db)


@router_notas.get('/{id}', response_model=NotaLeer)
def una_nota(id:int,db:Session=Depends(get_db)):
    return obtener_nota(id=id,db=db)

@router_notas.delete('/{id}')
def delete_nota(id:int,db:Session=Depends(get_db)):
    return eliminar_nota(id=id,db=db)


@router_notas.patch('/{id}',response_model=NotaLeer)
def update_nota(id:int, nota:NotaUpdate,db:Session=Depends(get_db)):
    return actualizar_nota(id=id,nota=nota,db=db)