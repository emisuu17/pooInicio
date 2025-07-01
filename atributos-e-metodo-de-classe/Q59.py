class Personagem:
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca

    @staticmethod
    def calcular_dano_base(forca):
        if forca <= 0:
            return 0
        return forca * 5

forca_do_ataque = 15
dano_calculado = Personagem.calcular_dano_base(forca_do_ataque)

print(f"Chamando o método estático diretamente da classe:")
print(f"Para uma força de {forca_do_ataque}, o dano base é: {dano_calculado}")
print("-" * 30)

guerreiro = Personagem("Aragorn", 20)

dano_com_instancia = guerreiro.calcular_dano_base(10)

print(f"Chamando o método a partir de uma instância ('{guerreiro.nome}'):")
print(f"Calculando o dano para uma força de 10 (não a do guerreiro, que é {guerreiro.forca}).")
print(f"Dano base resultante: {dano_com_instancia}")