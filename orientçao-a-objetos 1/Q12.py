import random
import time

class Pontuacao:
    """
    Controla e armazena a pontuação do jogador.
    """
    def __init__(self):
        self.pontos = 0

    def adicionar(self, valor):
        """Adiciona um valor à pontuação total."""
        self.pontos += valor
        print(f"✨ +{valor} pontos! Pontuação atual: {self.pontos}")

    def __str__(self):
        """Retorna a representação em string da pontuação."""
        return f"Pontuação: {self.pontos}"

class Inimigo:
    """
    Representa um inimigo no jogo com nome e vida.
    """
    def __init__(self, nome, vida=60):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida

    def esta_vivo(self):
        """Verifica se o inimigo ainda tem pontos de vida."""
        return self.vida > 0

    def __str__(self):
        """Retorna o status atual do inimigo."""
        return f"{self.nome} (❤️ {self.vida}/{self.vida_maxima})"

class Jogador:
    """
    Representa o jogador, com seus atributos de energia e ações.
    """
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.energia_maxima = 100

    def atacar(self, alvo, placar):
        """
        Ataca um alvo se tiver energia suficiente.
        Se o alvo for derrotado, adiciona pontos ao placar.
        """
        custo_energia = 10
        if self.energia < custo_energia:
            print("⚡ Energia insuficiente para atacar! Você precisa descansar.")
            return

        print(f"⚔️  {self.nome} se prepara para o ataque...")
        self.energia -= custo_energia
        dano = random.randint(15, 25)
        alvo.vida -= dano
        if alvo.vida < 0:
            alvo.vida = 0
        
        print(f"💥 Ataque efetuado! Causou {dano} de dano em {alvo.nome}.")

        if not alvo.esta_vivo():
            print(f"☠️  {alvo.nome} foi derrotado!")
            placar.adicionar(10) # Adiciona 10 pontos por inimigo derrotado

    def descansar(self):
        """
        Recupera 20 de energia, limitado ao máximo de 100.
        """
        if self.energia == self.energia_maxima:
            print("💤 Energia já está no máximo. Não precisa descansar.")
            return
            
        print("💤  {self.nome} está descansando para recuperar as forças...")
        self.energia += 20
        if self.energia > self.energia_maxima:
            self.energia = self.energia_maxima
        print(f"⚡ Energia recuperada! Energia atual: {self.energia}")

    def __str__(self):
        """Retorna o status atual do jogador."""
        return f"{self.nome} (⚡ {self.energia}/{self.energia_maxima})"


# --- Início da Simulação do Jogo ---
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
        
        # Loop de batalha para o inimigo atual
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
            
            time.sleep(1) # Pausa para legibilidade

        print(f"Você venceu o combate contra {inimigo_atual.nome}!")
        inimigo_atual_idx += 1
        time.sleep(2)

    print("\n" + "="*30)
    print("🏆 PARABÉNS! Você derrotou todos os inimigos da arena!")
    print(f"Sua pontuação final é: {placar.pontos} pontos!")

