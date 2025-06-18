class Missao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"Missão: {self.nome} - {self.descricao}"


class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.missoes_aceitas = [] 
    
    def aceitar_missao(self, missao):
        self.missoes_aceitas.append(missao)
        print(f"{self.nome} aceitou a missão: {missao.nome}")
    
    def listar_missoes(self):
        if self.missoes_aceitas:
            print(f"{self.nome} tem as seguintes missões:")
            for missao in self.missoes_aceitas:
                print(missao)
        else:
            print(f"{self.nome} não tem missões aceitas.")


missao1 = Missao("Salvar a Aldeia", "Proteger a aldeia contra os ataques de goblins.")
missao2 = Missao("Recuperar o Artefato", "Encontrar o artefato perdido na masmorra.")
missao3 = Missao("Resgatar o Prisioneiro", "Libertar o prisioneiro capturado por bandidos.")

personagem = Personagem("Lancelot")
personagem.listar_missoes()  
personagem.aceitar_missao(missao1)  
personagem.aceitar_missao(missao2) 
personagem.listar_missoes()  