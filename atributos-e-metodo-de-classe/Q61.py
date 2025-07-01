class Fase:
    tempo_maximo = 300

    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

    def mostrar_info(self):
        print(f"--- Informações da Fase ---")
        print(f"Nome: {self.nome}")
        print(f"Dificuldade: {self.dificuldade}")
        print(f"Tempo Máximo para Completar: {self.tempo_maximo} segundos")
        print("---------------------------")

print(f"Configuração global do jogo: O tempo máximo padrão para qualquer fase é de {Fase.tempo_maximo} segundos.")

fase1 = Fase(nome="Floresta palida", dificuldade="Fácil")
fase2 = Fase(nome="THE NETHER", dificuldade="Difícil")

print("\nExibindo informações das fases criadas:")
fase1.mostrar_info()
fase2.mostrar_info()

print("\n>>> Evento no jogo: 'O tempo está se esgotando!'. O tempo máximo de todas as fases foi reduzido.")
Fase.tempo_maximo = 180

print("\nExibindo novamente as informações após a mudança global:")
fase1.mostrar_info()
fase2.mostrar_info()

fase_bonus = Fase(nome="Caverna Secreta", dificuldade="Normal")
print("\nExibindo informações de uma nova fase criada após a alteração:")
fase_bonus.mostrar_info()