import json
from idlelib.query import Query
from typing import Annotated

from fastapi import FastAPI, Response, status, Query, Path, HTTPException
from futboldata import Futbol
from models import Partido

app = FastAPI()
futbol = Futbol()



@app.get('/', status_code=status.HTTP_200_OK)
def read_root():
    return {'bienvenido':'anyelo'}


@app.get('/partidos', status_code=status.HTTP_200_OK)
async def read_partido(total:Annotated[int, Query(ge=1)]=10, skip:Annotated[int, Query(ge=0)]=0,
                       all:bool | None = None, filtroName:Annotated[str | None, Query(min_length=3)] = None):

    if all:
        return futbol.all_partidos()

    else:
        return futbol.partido(skip, total, filtroName)


@app.get('/partidos/{id_partido}', status_code=status.HTTP_200_OK)
async def get_partidoId(id_partido:Annotated[int, Path(ge=1, description="ID del partido a obtener")], response:Response):

    IdEncontrado = futbol.get_partidoId(id_partido)
    if IdEncontrado:
        return IdEncontrado

    else:
        raise HTTPException(status_code=404, detail="Partido not found")



@app.get('/partidos/nombre/{name_equipo}', status_code=status.HTTP_200_OK)
async def get_partidoTeam(name_equipo:str = Path(..., max_length=30)):

    partidoEncontrado = futbol.get_partidoTeam(name_equipo)
    if partidoEncontrado:
        return partidoEncontrado

    else:
        raise HTTPException(status_code=404, detail="Partido not found")


@app.post('/partidos', status_code=status.HTTP_201_CREATED)
async def write_partido(partido:Partido):

    return futbol.write_partido(partido)



@app.put('/partidos/{id_partido}', status_code=status.HTTP_200_OK)
async def update_partido(id_partido:int, partido:Partido, response:Response):
    return futbol.update_partido(id_partido, partido)



@app.delete('/partidos/{id_partido}')
async def delete_partido(id_partido:int):
    return futbol.delete_partidos(id_partido)



