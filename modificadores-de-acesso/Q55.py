class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        print(f"Personagem {self.nome} criado com {self.vida} de vida e {self.ataque} de ataque!")

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} atacou {inimigo.nome} causando {self.ataque} de dano!")

    def esta_vivo(self):
        return self.vida > 0


class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        print(f"Inimigo {self.nome} criado com {self.vida} de vida e {self.ataque} de ataque!")

    def atacar(self, personagem):
        personagem.vida -= self.ataque
        print(f"{self.nome} atacou {personagem.nome} causando {self.ataque} de dano!")

    def esta_vivo(self):
        return self.vida > 0

class SistemaCombate:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo
        print("Sistema de combate iniciado!")

    def batalha(self):
        while self.personagem.esta_vivo() and self.inimigo.esta_vivo():
            self.personagem.atacar(self.inimigo)
            if self.inimigo.esta_vivo():
                self.inimigo.atacar(self.personagem)

        if self.personagem.esta_vivo():
            print(f"{self.personagem.nome} venceu a batalha!")
        else:
            print(f"{self.inimigo.nome} venceu a batalha!")

    def encerrar_combate(self):
        print("Sistema de combate encerrado!")


personagem = Personagem("Arthur", 100, 25)
inimigo = Inimigo("Goblin", 50, 15)

sistema_combate = SistemaCombate(personagem, inimigo)
sistema_combate.batalha()  
sistema_combate.encerrar_combate()  
