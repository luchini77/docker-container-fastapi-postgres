from fastapi import HTTPException, status,Depends
from sqlmodel import Session, select
from datetime import datetime

from app.db import get_db
from app.models import Nota,NotaCrear,NotaUpdate


def fecha_actual():
    fecha = datetime.today()
    date = fecha.strftime("%d/%m/%Y")
    return date


def crear_nota(nota:NotaCrear,db:Session=Depends(get_db)):
    nueva_nota = Nota.model_validate(nota)

    nueva_nota.fecha_creacion = fecha_actual()

    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)

    return nueva_nota


def obtener_nota(id:int,db:Session=Depends(get_db)):
    nota = db.get(Nota,id)
    if not nota:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No existe esa nota con el id {id}')
    return nota


def eliminar_nota(id:int,db:Session=Depends(get_db)):
    seleccion = select(Nota).where(Nota.id == id)

    if seleccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No existe esa nota con el id {id}')
    
    res = db.exec(seleccion)
    nota = res.one()
    db.delete(nota)
    db.commit()
    return {"Nota borrada": True}


def leer_notas(db:Session=Depends(get_db)):
    notas = db.exec(select(Nota)).all()
    return notas


def actualizar_nota(id:int,nota:NotaUpdate,db:Session=Depends(get_db)):
    nota_update = db.get(Nota,id)
    if not nota_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra nota con ese id: {id}')
    
    nota_data = nota.model_dump(exclude_unset=True)

    for key,value in nota_data.items():
        setattr(nota_update,key,value)

    db.add(nota_update)
    db.commit()
    db.refresh(nota_update)
    return nota_update