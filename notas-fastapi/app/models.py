from typing import Optional
from sqlmodel import Field, SQLModel


class NotaBase(SQLModel):
    titulo: str
    descripcion: str
    terminado: Optional[bool] = False
    fecha_creacion: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "titulo":"Comer",
                "descripcion":"Una buena pajarita",
                "terminado": False
                # "fecha_creacion":"2023-11-09"
            }
        }

class Nota(NotaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class NotaCrear(NotaBase):
    pass

class NotaLeer(NotaBase):
    id: int
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = None
    fecha_creacion: Optional[str] = None

class NotaUpdate(NotaBase):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = None
    fecha_creacion: Optional[str] = None
