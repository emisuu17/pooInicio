class Jogador:
    def __init__(self,energia):
        self.__energia = energia

    @property
    def energia(self):
        return self.__energia
    
    def usar_energia(self,valor):
        self.__energia -= valor
        print(f'energia restante:{self.__energia}')

    def recuperar_energia(self,valor2):
        self.__energia += valor2
        print(f'energia recuperada:{self.__energia}')
     
    

e1 = Jogador(100)
e1.usar_energia(100)
e1.recuperar_energia(200)
