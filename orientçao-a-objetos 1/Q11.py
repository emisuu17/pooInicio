import random
import time

class Personagem:
    
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
      
        dano = random.randint(5, 20)
        print(f"⚔️  {self.nome} ataca {alvo.nome} e causa {dano} de dano!")
        alvo.vida -= dano
        if alvo.vida < 0:
            alvo.vida = 0

    def esta_vivo(self):
        return self.vida > 0

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} ataca {self.nome} e causa {dano} de dano!")
        alvo.vida -= dano
        if alvo.vida < 0:
            alvo.vida = 0

    def esta_vivo(self):
        return self.vida > 0

if __name__ == "__main__":
    heroi = Personagem("Aragorn")
    monstro = Inimigo("Orc de Mordor")

    print(f"A batalha começa! {heroi.nome} ({heroi.vida}) vs. {monstro.nome} ({monstro.vida})\n")
    while heroi.esta_vivo() and monstro.esta_vivo():
        heroi.atacar(monstro)
        print(f"Status: {monstro.nome} está com {monstro.vida} de vida.\n")
        time.sleep(1)

        if not monstro.esta_vivo():
            break

        monstro.atacar(heroi)
        print(f"Status: {heroi.nome} está com {heroi.vida} de vida.\n")
        time.sleep(1) 
    
    print("--------------------")
    print("A batalha terminou!")
    
    if heroi.esta_vivo():
        print(f"O grande vencedor é {heroi.nome}!")
    else:
        print(f"O {monstro.nome} foi vitorioso.")