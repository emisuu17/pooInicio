class Jogador:
    def __init__(self):
        self.energia = 50
    
    def recuperar_energia(self,x):
        self.energia += x
        
    def usar_energia(self,x):
        self.energia -= x

        if self.energia <= 0:
            print('sem energia')
        else:
            print(f'tem {self.energia} de energia restante')

jogador1 = Jogador()
jogador1.recuperar_energia(0)
jogador1.usar_energia(50)

