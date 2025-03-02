import json

from models import Partido


class Futbol:

    def __init__(self):
        self.filepartidos = open('data/futboldata.json')
        self.partidos = json.load(self.filepartidos)


    def all_partidos(self):
        return self.partidos['partidos']


    def partido(self, skip:int=0, total:int=0, filtroName:str | None=None):

        partidoEncontrado = []

        if filtroName:
            for item in self.partidos['partidos']:
                if filtroName in item['equipolocal']:
                    partidoEncontrado.append(item)
            return partidoEncontrado

        else:
            return self.partidos['partidos'][skip:(total + skip)]


    def get_partidoId(self, id_partido:int):

        partido = None

        for item in self.partidos['partidos']:
            if item['id'] == id_partido:
                partido = item

        return partido


    def get_partidoTeam(self, name_equipo:str):

        listaPartido = []

        for item in self.partidos['partidos']:
            if item['equipolocal'] == name_equipo:
                listaPartido.append(item)

        if listaPartido:
            return listaPartido

        else:
            return None

    def write_partido(self, partido:Partido):

        with open('data/futboldata.json', 'w') as file:

            ultimoId = self.partidos['partidos'][-1]['id']
            partidoDict = partido.model_dump()
            partidoDict['id'] = ultimoId + 1

            self.partidos['partidos'].append(partidoDict)
            json.dump(self.partidos, file, indent=2)

            return partidoDict


    def update_partido(self, id_partido:int, partido:Partido):

        with open('data/futboldata.json', 'w') as file:
            partidoEncontrado = None
            index = 0

            for item in self.partidos['partidos']:
                if item['id'] == id_partido:
                    partidoEncontrado = item
                    break
                index += 1

            if partidoEncontrado:

                partidoDict = partido.model_dump()
                for elem in partidoDict:
                    self.partidos['partidos'][index][elem] = partidoDict[elem]

                json.dump(self.partidos, file, indent=2)
                return self.partidos['partidos'][index]

            else:
                return {"Error": "Id incorrecto"}



    def delete_partidos(self, id_partido:int):

        with open('data/futboldata.json', 'w') as file:
            partidoEncontrado = None
            index = 0

            for item in self.partidos['partidos']:
                if item['id'] == id_partido:
                    partidoEncontrado = item
                    break
                index += 1

            if partidoEncontrado:

                self.partidos['partidos'].pop(index)
                json.dump(self.partidos, file)
                return {'partido': f'{id_partido} id borrado correctamente'}

            else:
                return {"Error": "Id incorrecto"}

