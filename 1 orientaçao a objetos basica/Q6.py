class Personagem:
    def __init__(self):
        self.nome = 'ermeson'
    def dizer_nome(self):
        print(f'meu nome é {self.nome}')

nome1 = Personagem()
nome1.dizer_nome()