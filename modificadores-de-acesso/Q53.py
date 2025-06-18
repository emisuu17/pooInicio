class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        print(f"Item '{self.nome}' criado, preço: {self.preco}!")

    def exibir_info(self):
        print(f"Item: {self.nome}, Preço: {self.preco}")


class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []  
        print(f"Loja '{self.nome}' criada!")

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item '{item.nome}' adicionado à loja {self.nome}.")

    def listar_itens(self):
        if self.itens:
            print(f"Itens disponíveis na loja {self.nome}:")
            for item in self.itens:
                item.exibir_info()
        else:
            print(f"A loja {self.nome} não tem itens.")


item1 = Item("Espada", 150)
item2 = Item("Poção de Vida", 50)
item3 = Item("Escudo", 120)

loja = Loja("Loja do Herói")
loja.adicionar_item(item1)  
loja.adicionar_item(item2)
loja.adicionar_item(item3)

loja.listar_itens()  
