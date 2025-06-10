class Jogador:
    def __init__(self, nome, energia, pontos):
        
        self.nome = nome
        self.energia = energia
        self.pontos = pontos

    def exibir_status(self):
   
        print(f"Nome: {self.nome}")
        print(f"Energia: {self.energia}")
        print(f"Pontos: {self.pontos}")


if __name__ == "__main__":
  
    jogador1 = Jogador("Herói", 100, 0)

    print("--- Status do Jogador 1 ---")
    jogador1.exibir_status()

    jogador2 = Jogador("Vilão", 120, 50)

    print("\n--- Status do Jogador 2 ---")
    jogador2.exibir_status()
