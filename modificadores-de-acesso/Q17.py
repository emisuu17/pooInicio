class Jogador:
    def __init__(self,energia):
        self.__energia = energia

    @property
    def energia(self):
        return self.__energia
    
    def usar_energia(self,valor,):
        uso = self.__energia
        uso -= valor
        if uso == 0:
            print('sem energia')
        
        elif uso >0:
            print(f'voce tem {uso} de energia')
            
        else:return False

    def recuperar_energia(self,valor):
        up = self.__energia
        up += valor
        if up >= 100:
            print('sua energia esta no maximo')
        
        else:
            print(f'voce recuperou {valor}')



j1 = Jogador(100)
j1.usar_energia(100)
j1.recuperar_energia(30)

