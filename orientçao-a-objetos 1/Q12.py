import random
import time

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def adicionar(self, valor):
        self.pontos += valor
        print(f"+{valor} pontos! Pontuação atual: {self.pontos}")

    def __str__(self):
        return f"Pontuação: {self.pontos}"

class Inimigo:
    def __init__(self, nome, vida=60):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f"{self.nome} ({self.vida}/{self.vida_maxima})"

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.energia_maxima = 100

    def atacar(self, alvo, placar):
        custo_energia = 10
        if self.energia < custo_energia:
            print("Energia insuficiente para atacar! Você precisa descansar.")
            return

        print(f"{self.nome} se prepara para o ataque...")
        self.energia -= custo_energia
        dano = random.randint(15, 25)
        alvo.vida -= dano
        if alvo.vida < 0:
            alvo.vida = 0
        
        print(f"Ataque efetuado! Causou {dano} de dano em {alvo.nome}.")

        if not alvo.esta_vivo():
            print(f"{alvo.nome} foi derrotado!")
            placar.adicionar(10)

    def descansar(self):
        if self.energia == self.energia_maxima:
            print("Energia já está no máximo. Não precisa descansar.")
            return
            
        print("{self.nome} está descansando para recuperar as forças...")
        self.energia += 20
        if self.energia > self.energia_maxima:
            self.energia = self.energia_maxima
        print(f"Energia recuperada! Energia atual: {self.energia}")

    def __str__(self):
        return f"{self.nome} ({self.energia}/{self.energia_maxima})"

if __name__ == "__main__":
    jogador = Jogador("Valente")
    placar = Pontuacao()
    inimigos = [Inimigo("Goblin"), Inimigo("Orc"), Inimigo("Dragão Bebê", vida=100)]
    inimigo_atual_idx = 0

    print("--- Bem-vindo à Arena! ---")

    while inimigo_atual_idx < len(inimigos):
        inimigo_atual = inimigos[inimigo_atual_idx]
        print("\n" + "="*30)
        print(f"Um {inimigo_atual.nome} selvagem aparece!")
        
        while inimigo_atual.esta_vivo():
            print("\n--- Seu Turno ---")
            print(f"Jogador: {jogador}")
            print(f"Inimigo: {inimigo_atual}")
            print(f"Placar: {placar.pontos}")
            print("-" * 17)
            
            escolha = input("O que você faz? (1-Atacar, 2-Descansar, 3-Sair): ")

            if escolha == '1':
                jogador.atacar(inimigo_atual, placar)
            elif escolha == '2':
                jogador.descansar()
            elif escolha == '3':
                print("Você fugiu da batalha. Jogo encerrado.")
                exit()
            else:
                print("Opção inválida! Tente novamente.")
            
            time.sleep(1)

        print(f"Você venceu o combate contra {inimigo_atual.nome}!")
        inimigo_atual_idx += 1
        time.sleep(2)

    print("\n" + "="*30)
    print("PARABÉNS! Você derrotou todos os inimigos da arena!")
    print(f"Sua pontuação final é: {placar.pontos} pontos!")

