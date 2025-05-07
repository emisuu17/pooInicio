class Pontuação:
    def __init__(self,pontos):
        self.__pontos = pontos

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self,valor):
        if valor < 0:
            print('valor invalido')

        else:print(self.__pontos)

p1 = Pontuação(100)
p1.pontos = -1
print(p1.pontos)


    
