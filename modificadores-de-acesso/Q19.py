class Pontuação:
    def __init__(self, pontos):
        self.__pontos = pontos

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor < 0:
            print('Valor inválido')
        else:
            self.__pontos += valor
            print(f'Pontuação atual: {self.__pontos}')

p1 = Pontuação(100)
p1.pontos = -50
p1.pontos = 9899



    
