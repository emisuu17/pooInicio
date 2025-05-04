class Pontuação:
    def __init__(self):
        self.__pontos = 10

    @property
    def __adicionar_pontos(self):
        return self.__pontos
    
p1 = Pontuação()
p1.__adicionar_pontos()
