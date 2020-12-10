from pydantic import BaseModel

class IngresoIn(BaseModel):
    tipo: str
    valor: float
    constante: bool

class IngresoOut(BaseModel):
    tipo: str
    valor: float
    mensaje = "Registro exitoso"

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