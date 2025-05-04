class Personagem:
    def __init__(self,vida):
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida

v1 = Personagem(100)

print(f'o personagem tem {v1.vida} de vida ')
        