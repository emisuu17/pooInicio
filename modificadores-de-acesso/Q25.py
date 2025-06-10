class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def exibir(self):
        print("=== " + self.titulo + " ===")
        
meu_menu = Menu("Menu Principal")
meu_menu.exibir()
