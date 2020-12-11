from pydantic.types import ConstrainedStr
from models import ingreso
from pydantic import BaseModel
from typing import Dict

class IngresoInDB(BaseModel):
    id_ingreso: int = 0
    tipo: str
    valor: int
    constante: bool


tipos_validos = ['salario', 'ocasional', 'inversion']

database_ingresos = {
    101: IngresoInDB(**{"id_ingreso": 101,
                        "tipo": "ocasional",
                        "valor": 1000,
                        "constante": False}),
    102: IngresoInDB(**{"id_ingreso": 102,
                        "tipo": "inversion",
                        "valor": 5000,
                        "constante": False})
}
generator = {'id': 102}

def save_ingresos(ingreso_in_db: IngresoInDB):
    generator['id'] = generator['id'] + 1
    ingreso_in_db.id_ingreso = generator['id']
    database_ingresos[generator['id']] = ingreso_in_db
    return ingreso_in_db

def get_ingresos(id: int):
    if id in database_ingresos.keys():
        return database_ingresos[id]
    else: 
        return None

def update_ingresos(ingreso_in_db: IngresoInDB, database_ingresos: dict):
    ingreso_in_db[ingreso_in_db.id_ingreso] = ingreso_in_db
    return ingreso_in_db
