class Personagem:
    def __init__(self, defesa):
        self.__defesa = defesa

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        if valor <= 0 or valor >= 100:
            print('Valor inválido! A defesa deve estar entre 0 e 100.')
        else:
            self.__defesa = valor
            print(f'Defesa atualizada para: {self.__defesa}')

p1 = Personagem(50)
p1.defesa = 80
p1.defesa = 290