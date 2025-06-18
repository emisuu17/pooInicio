class Fase:
    def __init__(self, nome):
        self.nome = nome
        print(f"Fase {self.nome} criada!")

    def iniciar(self):
        print(f"Iniciando a fase {self.nome}...")

    def finalizar(self):
        print(f"Finalizando a fase {self.nome}...")


class Mapa:
    def __init__(self, nome):
        self.nome = nome
        self.fases = []  
        print(f"Mapa {self.nome} criado!")

    def adicionar_fase(self, fase):
        self.fases.append(fase)
        print(f"Fase {fase.nome} adicionada ao mapa {self.nome}.")

    def listar_fases(self):
        if self.fases:
            print(f"Fases do mapa {self.nome}:")
            for fase in self.fases:
                print(f"- {fase.nome}")
        else:
            print(f"O mapa {self.nome} não tem fases.")


fase1 = Fase("Floresta Sombria")
fase2 = Fase("Montanhas Geladas")
fase3 = Fase("Deserto Ardente")

mapa = Mapa("Mundo Fantástico")
mapa.adicionar_fase(fase1)  
mapa.adicionar_fase(fase2)
mapa.adicionar_fase(fase3)

mapa.listar_fases()  
