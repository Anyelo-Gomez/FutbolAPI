from pydantic import BaseModel, Field

class Partido(BaseModel):


    anyo: int = Field(title="año del partido")
    fase : str | None = None
    equipolocal : str = Field(title="Nombre del equipo local")
    goleslocales: int | None = None
    golesvisitante: int | None = None
    equipovisitante :str | None = None
    estaequipoanfitrion : int | None = None
