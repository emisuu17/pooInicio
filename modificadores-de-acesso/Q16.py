class Inimigo:
    def __init__(self,nome,forca):
        self.nome = nome
        self.__forca = forca

    @property
    def forca(self):
        return self.__forca

    def atacar(self):
        print(f'sua força é {self.forca}')


i1 = Inimigo('guerreiro',8500)
i1.atacar()




