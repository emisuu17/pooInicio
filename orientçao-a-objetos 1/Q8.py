class Personagem:
    def __init__(self):
        self.vida = 100
    
    def tomar_dano(self,x):
        self.vida -= x
        if self.vida <= 0:
            print('F')
        else:
            print('tankou')

dano1 = Personagem()
dano1.tomar_dano(99)
        
        