class Aliado:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo  
        print(f"Aliado {self.nome} do tipo {self.tipo} criado!")

    def ajudar(self):
        print(f"{self.nome} está ajudando na aventura!")


class Jogador:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe  
        self.aliado = None  
        print(f"Jogador {self.nome} da classe {self.classe} criado!")

    def adicionar_aliado(self, aliado):
        self.aliado = aliado
        print(f"{self.nome} agora tem um aliado: {aliado.nome}!")

    def listar_aliado(self):
        if self.aliado:
            print(f"{self.nome} está acompanhado de {self.aliado.nome}, um aliado do tipo {self.aliado.tipo}.")
        else:
            print(f"{self.nome} não tem aliado.")

    def aventura(self):
        print(f"{self.nome} está em uma grande aventura!")
        if self.aliado:
            self.aliado.ajudar() 
        else:
            print(f"{self.nome} está sozinho na aventura.")


aliado1 = Aliado("Lancelot", "Cavaleiro")
aliado2 = Aliado("Merlin", "Mago")

jogador = Jogador("Arthur", "Cavaleiro")
jogador.listar_aliado() 
jogador.adicionar_aliado(aliado1)  
jogador.listar_aliado()  
jogador.aventura()  

jogador.adicionar_aliado(aliado2)  
jogador.listar_aliado()  
