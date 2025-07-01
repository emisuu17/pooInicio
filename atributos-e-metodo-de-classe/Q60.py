class Loja:
    catalogo_itens = [
        {'nome': 'Poção de cura', 'preco': 50.0},
        {'nome': 'Poção de velocidade', 'preco': 150.0},
        {'nome': 'Poção de resistencia ao fogo', 'preco': 100.0}
    ]

    def __init__(self, nome_loja):
        self.nome_loja = nome_loja

    @classmethod
    def ajustar_preco_itens(cls, fator):
        print(f"\nAjustando preços com um fator de {fator}...")
        for item in cls.catalogo_itens:
            item['preco'] = round(item['preco'] * fator, 2)

    @classmethod
    def mostrar_catalogo(cls):
        print("\n--- Catálogo de Itens ---")
        for item in cls.catalogo_itens:
            print(f"- {item['nome']}: R$ {item['preco']:.2f}")
        print("-------------------------")

print("Preços originais na classe Loja:")
Loja.mostrar_catalogo()

fator_inflacao = 1.10
Loja.ajustar_preco_itens(fator_inflacao)

print("\nPreços após o ajuste de inflação:")
Loja.mostrar_catalogo()

loja_da_cidade = Loja("vila")
loja_da_floresta = Loja("Cabana do villager")

print(f"\nCatálogo visto da instância '{loja_da_cidade.nome_loja}':")
loja_da_cidade.mostrar_catalogo()

fator_deflacao = 0.95
Loja.ajustar_preco_itens(fator_deflacao)

print("\nPreços após o segundo ajuste (deflação):")
loja_da_floresta.mostrar_catalogo()