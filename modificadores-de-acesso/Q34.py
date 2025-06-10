class Fase:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_info(self):
        print(f"Fase: {self.nome}")

class FaseFloresta(Fase):
    def mostrar_info(self):
        print(f"Fase: {self.nome}")
        print("Ambiente: Floresta densa com muitos inimigos escondidos.")
        print("Desafio: Visibilidade baixa e emboscadas.")

class FaseDeserto(Fase):
    def mostrar_info(self):
        print(f"Fase: {self.nome}")
        print("Ambiente: Deserto escaldante e aberto.")
        print("Desafio: Calor extremo e escassez de recursos.")


floresta = FaseFloresta("Floresta Sombria")
deserto = FaseDeserto("Deserto Ardente")

floresta.mostrar_info()
print()
deserto.mostrar_info()
