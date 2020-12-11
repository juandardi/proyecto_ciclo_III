from pydantic import BaseModel

class IngresoIn(BaseModel):
    tipo: str
    valor: float
    constante: bool

class IngresoOut(BaseModel):
    id_ingreso: int
    tipo: str
    valor: float

'''
class Salario(BaseModel):
    valor: int
    tipo = 'salario'
    constante = True

class GananciaOcasional(BaseModel):
    valor: int
    tipo = 'ocasional'  
    constante = False

class Inversion(BaseModel):
    valor: int
    tipo = 'inversion'
    constante = False
'''