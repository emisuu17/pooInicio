class Missao:
    def __init__(self, titulo):
        self.titulo = titulo

    def concluir(self):
        print(f"Missão '{self.titulo}' concluída!")

class MissaoPrincipal(Missao):
    def concluir(self):
        print(f"Missão '{self.titulo}' concluída!")
        print("Recompensa: 1000 moedas de ouro e uma espada lendária!")

class MissaoSecundaria(Missao):
    def concluir(self):
        print(f"Missão '{self.titulo}' concluída!")
        print("Recompensa: 200 moedas de ouro e uma poção de cura.")

m1 = MissaoPrincipal("Derrotar o Chefe Final")
m2 = MissaoSecundaria("Ajudar o aldeão")

m1.concluir()
m2.concluir()

