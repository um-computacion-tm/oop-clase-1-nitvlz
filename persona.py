class Persona():

    def __init__(self, nombre: str = "chachi", apellido: str = "chachingo", du: int = 123456789):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du


    
    def __str__(self):
        return(f'Mis datillos son \n nombre = {self.__nombre__} \n apellido = {self.__apellido__} \n documento = {self.__du__}')


    # def mostrar_datos(self):
    #     return(f'Mis datos son \n nombre = {self.__nombre__} \n apellido = {self.__apellido__} \n documento = {self.__du__}')