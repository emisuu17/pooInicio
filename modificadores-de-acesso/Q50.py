# Classe Item
class Item:
    def __init__(self, nome):
        self.nome = nome
        print(f"Item '{self.nome}' criado!")

    def usar(self):
        print(f"Usando o item '{self.nome}'.")

    def destruir(self):
        print(f"Item '{self.nome}' destruído!")


class Inventario:
    def __init__(self):
        self.itens = [] 
        print("Inventário criado!")

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item '{item.nome}' adicionado ao inventário.")

    def usar_item(self, nome_item):
        for item in self.itens:
            if item.nome == nome_item:
                item.usar()
                return
        print(f"Item '{nome_item}' não encontrado no inventário.")

    def finalizar(self):
        print("Finalizando o inventário...")
        for item in self.itens:
            item.destruir()  
        self.itens.clear()  

inventario = Inventario()

item1 = Item("Espada")
item2 = Item("Poção de Vida")

inventario.adicionar_item(item1) 
inventario.adicionar_item(item2)

inventario.usar_item("Espada")  
inventario.usar_item("Escudo") 

inventario.finalizar()  
