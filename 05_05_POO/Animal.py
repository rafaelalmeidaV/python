class Animal:
    
    def __init__(self,nome, peso):
        self.__nome = nome
        self.__peso = peso

    def getNome(self):
        return self.__nome
    
    def getPeso(self):
        return self.__peso
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setPeso(self, peso):
        self.__peso = peso
    
    def dormir(self):
        return ". . . dormindo . . ."
    

class Cachorro (Animal):
    
    def __init__(self, nome, peso):
        Animal.__init__(self, nome, peso)
    
    def enterrarOsso(self):
        print("Enterrando osso. . . .")
    

class Galinha (Animal):

    def __init__(self, nome, peso):
        Animal.__init__(self, nome, peso)
    
    def botarOvo(self):
        print("Botou . . . .")
