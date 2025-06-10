class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def exibir(self):
        print("=== " + self.titulo + " ===")

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {}

    def salvar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva como: {valor}")

    def mostrar_configuracoes(self):
        print("Configurações salvas:")
        for chave, valor in self.configuracoes.items():
            print(f"{chave}: {valor}")
            
menu = MenuAvancado("Configurações do Jogo")
menu.exibir()

menu.salvar_configuracao("volume", "80%")
menu.salvar_configuracao("dificuldade", "média")

menu.mostrar_configuracoes()
