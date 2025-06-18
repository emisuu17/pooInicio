class Menu:
    def __init__(self):
        print("Menu criado!")

    def exibir(self):
        print("Exibindo o menu do jogo...")

    def destruir(self):
        print("Menu destruído!")


class Jogo:
    def __init__(self):
        print("Jogo iniciado!")
        self.menu = Menu()  

    def iniciar(self):
        print("Iniciando o jogo...")
        self.menu.exibir()

    def finalizar(self):
        print("Finalizando o jogo...")
        self.menu.destruir() 

jogo = Jogo()  
jogo.iniciar()  
jogo.finalizar()  
