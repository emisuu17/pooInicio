class Jogo:
    def __init__(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor > 3 or valor <= 0:
            print('valor inválido')
        else:
            self.__dificuldade = valor
            print(f'Nível de dificuldade escolhido: {self.__dificuldade}')

j = Jogo(1)
j.dificuldade = 2
j.dificuldade = 5  
