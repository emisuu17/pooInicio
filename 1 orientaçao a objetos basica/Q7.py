class Pontuação:
    def __init__(self):
        self.pontos = 0
    
    def adicionar_pontos(self,x):
        self.pontos += x

    def mostrar_pontos(self):
        print(f'seus pontos são {self.pontos}')
     
ponto1 = Pontuação()
ponto1.adicionar_pontos(25)
ponto1.mostrar_pontos()
