from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'FastAPI Portfolio'
app.version = '0.0.1'

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