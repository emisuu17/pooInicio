class MagiaElemental:
    def lancar_magia(self, elemento):
        if elemento == "fogo":
            print("Lançando magia de Fogo!")
        elif elemento == "agua":
            print("Lançando magia de Água!")
        elif elemento == "terra":
            print("Lançando magia de Terra!")
        elif elemento == "ar":
            print("Lançando magia de Ar!")
        else:
            print("Elemento inválido!")

class Mago:
    def conjurar(self):
        print("Conjurando feitiço!")

class MagoElemental(Mago, MagiaElemental):
    def __init__(self, nome):
        self.nome = nome

mago_elemental = MagoElemental("Merlin")
mago_elemental.conjurar() 
mago_elemental.lancar_magia("fogo")  
mago_elemental.lancar_magia("agua")  
mago_elemental.lancar_magia("terra") 
mago_elemental.lancar_magia("ar")  
