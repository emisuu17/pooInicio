class Jogo:
    # 1. Atributo de classe: 'dificuldade_global'
    # Este valor é compartilhado por todas as instâncias (objetos) da classe Jogo.
    # Definimos um valor padrão inicial.
    dificuldade_global = "Normal"

    def __init__(self, nome):
        """O construtor da classe, executado ao criar um novo jogo."""
        self.nome = nome
        print(f"Jogo '{self.nome}' foi instalado.")

    def exibir_dificuldade_atual(self):
        """
        Um método de instância que lê o atributo de classe.
        Quando 'self.dificuldade_global' é acessado, o Python primeiro procura
        o atributo na instância. Se não encontrar, ele busca na classe.
        """
        print(f"-> Em '{self.nome}', a dificuldade global está definida como: '{self.dificuldade_global}'")

    @classmethod
    def alterar_dificuldade_global(cls, nova_dificuldade):
        """
        2. Método de classe para alterar o atributo de classe.
        'cls' se refere à própria classe 'Jogo'.
        Alterar 'cls.dificuldade_global' muda o valor para todas as instâncias.
        """
        print(f"\n! A dificuldade global do jogo foi alterada para '{nova_dificuldade}'.\n")
        cls.dificuldade_global = nova_dificuldade

jogo_corrida = Jogo("Forza Horizon")
jogo_aventura = Jogo("The Legend of Zelda")

print("-" * 40)
print("Verificando a dificuldade inicial...")
jogo_corrida.exibir_dificuldade_atual()
jogo_aventura.exibir_dificuldade_atual()

print("-" * 40)

jogo_aventura.alterar_dificuldade_global("Difícil")
print("Verificando a dificuldade após a alteração...")

jogo_corrida.exibir_dificuldade_atual()
jogo_aventura.exibir_dificuldade_atual()
print("-" * 40)
Jogo.alterar_dificuldade_global("Fácil")


print("Verificando a dificuldade após a segunda alteração...")
jogo_corrida.exibir_dificuldade_atual()
jogo_aventura.exibir_dificuldade_atual()