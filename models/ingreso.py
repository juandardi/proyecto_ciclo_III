from pydantic import BaseModel

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
