

class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email

    def dame_tu_nombre(self):
        return self.__nombre__ 


class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ =""
        self.__mentor__ = None

    def mentoria(self, profesor):
        self.__mentor__= profesor

    def falta(self):
        self.__inasistencias__ += 1

    def elegir_dieta_especial_uwu(self, la_dieta):
        self.__dieta__ = la_dieta 
    def es_vegano(self):
        self.__dieta__ = "veganojaja"

    def esta_libre(self):
        if self.__inasistencias__ > 5:
            return "ESTA LIBRE"
        else: 
            return "OK"

#Profesor_data

profe_elion_musk = Profesor("Elio", "elio@um.edu.ar")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

#print(profe_elio.dame_tu_nombre())
#print(profe_gabi.dame_tu_nombre())

alumno_juanca = Alumno("Juan")
alumno_chachi = Alumno("Sacchi")

#Inasistencias

alumno_chachi.falta()
alumno_chachi.falta()
alumno_chachi.falta()
alumno_chachi.falta()
alumno_chachi.falta()
print(alumno_chachi.esta_libre())
alumno_chachi.falta()
print(alumno_chachi.esta_libre())

#Dietas

alumno_chachi.elegir_dieta_especial_uwu("vegetariano")
print(alumno_chachi.dieta)
alumno_chachi.es_vegano()
print(alumno_chachi.dieta)

#Mentoria

alumno_chachi.mentoria(profe_elion_musk)
print(alumno_chachi.__mentor__)

los_alumnos = [alumno_juanca, alumno_chachi]





