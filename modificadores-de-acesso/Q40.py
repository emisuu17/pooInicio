class Menu:
    def exibir(self):
        print("Opções do Menu:")
        print("1. Iniciar")
        print("2. Sair")


class MenuAvancado(Menu):
    def exibir(self):
        
        print("Opções do Menu:")
        print("1. Iniciar")
        print("2. Sair")
       
        print("3. Opção Avançada 1")
        print("4. Opção Avançada 2")
        print("5. Opção Avançada 3")


menu = MenuAvancado()
menu.exibir()
