import json

from fastapi import FastAPI, Response, status
from futboldata import Futbol
from models import Partido

app = FastAPI()
futbol = Futbol()



@app.get('/', status_code=status.HTTP_200_OK)
def read_root():
    return {'bienvenido':'aanyelo'}


@app.get('/partidos', status_code=status.HTTP_200_OK)
async def read_partido(total:int=10, skip:int=0, all:bool | None = None):
    if all:
        return futbol.all_partidos()
    else:
        return futbol.partido(skip, total)


@app.get('/partidos/{id_partido}', status_code=status.HTTP_200_OK)
async def get_partidoId(id_partido:int, response:Response):

    partidoEncontrado = futbol.get_partidoId(id_partido)
    if partidoEncontrado:
        return partidoEncontrado

    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error!": "id no encontrado"}


@app.get('/partidos/nombre/{name_equipo}', status_code=status.HTTP_200_OK)
async def get_partidoTeam(name_equipo:str, response:Response):

    partidoEncontrado = futbol.get_partidoTeam(name_equipo)
    if partidoEncontrado:
        return partidoEncontrado

    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error!": "id no encontrado"}



@app.post('/partidos', status_code=status.HTTP_201_CREATED)
async def write_partido(partido:Partido, response:Response):

    return futbol.write_partido(partido)



@app.put('/partidos/{id_partido}', status_code=status.HTTP_200_OK)
async def update_partido(id_partido:int, partido:Partido, response:Response):
    return futbol.update_partido(id_partido, partido)



@app.delete('/partidos/{id_partido}')
async def delete_partido(id_partido:int):
    return futbol.delete_partidos(id_partido)



