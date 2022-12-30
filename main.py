from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = 'FastAPI Portfolio'
app.version = '0.0.1'

class Ruta(BaseModel):
    id: Optional[str] = None
    salida: str = Field(max_length=25)
    llega: str = Field(max_length=25)

rutas = [
    {
        'id': 'R7',
        'salida': 'Blvd de las Americas',
        'llega': 'Fracc Vistana'
    },
    {
        'id': 'R9',
        'salida': 'Chedraui',
        'llega': 'Fracc Vistana'
    }
]

@app.get("/", tags=['Home'])
def root():
    return HTMLResponse('<h1>Hola Mundo</h1>')

@app.get('/rutas', tags=['Rutas'])
def get_rutas():
    return(rutas)

@app.get('/rutas/{id}', tags=['Rutas'])
def get_ruta(id: str):
    ruta = list(filter(lambda x: x['id'] == id,rutas))
    return ruta if len(ruta) > 0 else 'No existe la ruta'

@app.get('/rutas/salida/', tags=['Rutas'])
def get_ruta_by_salida(salida: str):
    ruta = list(filter(lambda x: x['salida'] == salida,rutas))
    return ruta if len(ruta) > 0 else 'No existe la ruta'

@app.get('/rutas/llega/', tags=['Rutas'])
def get_ruta_by_llega(llega: str):
    ruta = list(filter(lambda x: x['llega'] == llega,rutas))
    return ruta if len(ruta) > 0 else 'No existe la ruta'

@app.post('/rutas/nueva/', tags=['Rutas'])
def post_ruta(ruta: Ruta):
    rutas.append(ruta)
    return rutas

def obtener_ruta(id):
    for ruta in rutas:
        if ruta['id'] == id:
            return ruta
    return None

@app.put('/rutas/{id}', tags=['Rutas'])
def put_ruta(id: str, ruta: Ruta):
    item = obtener_ruta(id)
    if item is not None:
        item['salida'] = ruta.salida
        item['llega'] = ruta.llega
        return rutas
    else:
        return 'No existe la Ruta'

@app.delete('/rutas/{id}', tags=['Rutas'])
def delete_ruta(id: str):
    ruta = obtener_ruta(id)
    if ruta is not None:
        rutas.remove(ruta)
        return rutas
    else:
        return 'No existe la Ruta'