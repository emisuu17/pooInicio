class personagem:
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida


p1 = personagem('guts',9999)
print(p1.nome)
print(p1.vida)