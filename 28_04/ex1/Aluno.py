class Aluno:
    __ra: None 
    __nota1: None
    __nota2: None
    __media: None
    __nome: None

    def __init__(self, nome, ra, nota1, nota2):
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nome = nome 

    def getNome(self):
        return self.__nome

    def getRa(self):
        return self.__ra

    def getNota1(self):
        return self.__nota1

    def getNota2(self):
        return self.__nota2

    def getMedia(self):
        return self.__media

    def setNome(self, nome):
        self.__nome = nome

    def setRa(self, ra):
        self.__ra = ra

    def setNota1(self, nota1):
        self.__nota1 = nota1

    def setNota2(self, nota2):
        self.__nota2 = nota2

    def setMedia(self, media):
        self.__media = media
           
    
    def calcular_media(self):
        self.media = (self.nota1 + self.nota2)/2
        return self.media
    
    def descri(self):
        print("Nome: ", self.nome)
        print("RA: ", self.ra)
        print("Nota 1: ", self.nota1)
        print("Nota 2: ", self.nota2)
        print("Media: ", self.media)

