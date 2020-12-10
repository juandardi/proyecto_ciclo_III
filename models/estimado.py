from pydantic import BaseModel

class Emergencias(BaseModel):
    valor: int
    tipo = 'emergencias'

class Alimentacion(BaseModel):
    valor: int
    tipo = 'alimentacion'

class Ocio(BaseModel):
    valor: int
    tipo = 'ocio'

class Vivienda(BaseModel):
    valor: int
    tipo = 'vivienda'

class Comunicacion(BaseModel):
    valor: int
    tipo = 'comunicacion'

class Vehiculo(BaseModel):
    valor: int
    tipo = 'vehiculo'

class Transporte(BaseModel):
    valor: int
    tipo = 'transporte'

class Compras(BaseModel):
    valor: int
    tipo = 'compras'
    
class Salud(BaseModel):
    valor: int
    tipo = 'salud'

class Impuestos(BaseModel):
    valor: int
    tipo = 'impuestos'