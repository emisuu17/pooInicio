class Personagem:
    def __init__(self,vida):
        self.__vida = vida  

    @property
    def vida(self):
        return self.__vida
    
v1 = Personagem(150)
print(v1.vida)