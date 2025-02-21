from pydantic import BaseModel

class Partido(BaseModel):


    anyo: int
    fase : str | None = None
    equipolocal : str
    goleslocales: int | None = None
    golesvisitante: int | None = None
    equipovisitante :str | None = None
    estaequipoanfitrion : int | None = None
