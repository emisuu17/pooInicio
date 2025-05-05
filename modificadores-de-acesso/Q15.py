class Pontuação:
    def __init__(self,pontos):
        self.__pontos = pontos
    
    @property
    def pontos(self):
        return self.__pontos
    

    def ad_pontos(self,valor):
        if valor >= 0:
            self.__pontos += valor
            return True
        else:
            return False
        

p1 = Pontuação(10)
p1.ad_pontos(200)
print(f'seus pontos atuais são {p1.pontos}')





    
     
