import random
import time

class Personagem:
    """
    Representa o personagem controlado pelo jogador ou um herói.
    """
    def __init__(self, nome):
        """
        Inicializa o personagem com um nome e 100 pontos de vida.
        """
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        """
        Ataca um alvo (inimigo), causando uma quantidade aleatória de dano.
        """
        # O dano é um valor aleatório entre 5 e 20
        dano = random.randint(5, 20)
        print(f"⚔️  {self.nome} ataca {alvo.nome} e causa {dano} de dano!")
        alvo.vida -= dano
        # Garante que a vida não fique negativa
        if alvo.vida < 0:
            alvo.vida = 0

    def esta_vivo(self):
        """
        Verifica se o personagem ainda tem pontos de vida.
        """
        return self.vida > 0

class Inimigo:
    """
    Representa um inimigo no jogo.
    """
    def __init__(self, nome):
        """
        Inicializa o inimigo com um nome e 100 pontos de vida.
        """
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        """
        Ataca um alvo (personagem), causando uma quantidade aleatória de dano.
        """
        # O dano é um valor aleatório entre 5 e 20
        dano = random.randint(5, 20)
        print(f"💥 {self.nome} ataca {self.nome} e causa {dano} de dano!")
        alvo.vida -= dano
        # Garante que a vida não fique negativa
        if alvo.vida < 0:
            alvo.vida = 0

    def esta_vivo(self):
        """
        Verifica se o inimigo ainda tem pontos de vida.
        """
        return self.vida > 0

# --- Início da Simulação da Batalha ---
if __name__ == "__main__":
    # 1. Criação dos combatentes
    heroi = Personagem("Aragorn")
    monstro = Inimigo("Orc de Mordor")

    print(f"A batalha começa! {heroi.nome} (❤️ {heroi.vida}) vs. {monstro.nome} (❤️ {monstro.vida})\n")
    
    # 2. Loop do jogo
    # O loop continua enquanto ambos estiverem vivos
    while heroi.esta_vivo() and monstro.esta_vivo():
        # Turno do Herói
        heroi.atacar(monstro)
        print(f"Status: {monstro.nome} está com {monstro.vida} de vida.\n")
        time.sleep(1) # Pausa para melhor legibilidade

        # Verifica se o inimigo foi derrotado
        if not monstro.esta_vivo():
            break

        # Turno do Inimigo
        monstro.atacar(heroi)
        print(f"Status: {heroi.nome} está com {heroi.vida} de vida.\n")
        time.sleep(1) # Pausa para melhor legibilidade
    
    # 3. Anúncio do Vencedor
    print("--------------------")
    print("A batalha terminou!")
    
    if heroi.esta_vivo():
        print(f"🏆 O grande vencedor é {heroi.nome}!")
    else:
        print(f"☠️  O {monstro.nome} foi vitorioso.")