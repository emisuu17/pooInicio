class Fase:
    def gerar_inimigos(self):
        print("Gerando inimigos padrões...")

class FaseDeserto(Fase):
    def gerar_inimigos(self):
       
        print("Gerando inimigos do deserto:")
        print("1. Escorpião gigante")
        print("2. Serpente venenosa")
        print("3. Golem de areia")
        print("4. Falcão de deserto")


fase = FaseDeserto()
fase.gerar_inimigos()
