class Menu:
    def iniciar_jogo(self):
        print('start game')

    def mostrar_opcoes(self):
        print('reiniciar,configuraçoes,sair')
    
    def sair(self):
        print('sair')

menu1 = Menu()
menu1.iniciar_jogo()
menu1.mostrar_opcoes()
menu1.sair()