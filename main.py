import fastapi
from db.ingreso_db import IngresoInDB
from db.ingreso_db import save_ingresos, get_ingresos
from models.ingreso import IngresoIn, IngresoOut

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

@api.put("/user/ingresos/")
async def make_ingreso(ingreso: IngresoIn):
    ingreso_in_db = IngresoInDB(**ingreso.dict())
    ingreso_in_db = save_ingresos(ingreso_in_db)
    salida =  IngresoOut(tipo = ingreso_in_db.tipo, valor = ingreso_in_db.valor)
    return salida

@api.get("/user/ingresos/")
async def get_ingresos2():
    salida = get_ingresos()
    return salida