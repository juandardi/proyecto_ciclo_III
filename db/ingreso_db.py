from models import ingreso
from pydantic import BaseModel

class IngresoInDB(BaseModel):
    id_ingreso: int = 0
    tipo: str
    valor: int
    constante: bool

database_ingresos = []
generator = {'id': 0}

def save_ingresos(ingreso_in_db: IngresoInDB):
    generator['id'] = generator['id'] + 1
    ingreso_in_db.id_ingreso = generator['id']
    database_ingresos.append(ingreso_in_db)
    return ingreso_in_db


