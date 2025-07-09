import random
import time
import os

def limpar_tela():
    """Limpa o console para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Pontuacao:
    """Controla e armazena a pontuação do jogador."""
    def __init__(self):
        self.pontos = 0

    def adicionar(self, valor):
        self.pontos += valor
        print(f"✨ +{valor} pontos! Pontuação atual: {self.pontos}")

class Inimigo:
    """Representa um inimigo no jogo com nome, vida e capacidade de ataque."""
    def __init__(self, nome, vida=50, dano_min=5, dano_max=15):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.dano_min = dano_min
        self.dano_max = dano_max

    def atacar(self, alvo):
        """Ataca o jogador, causando dano à sua energia."""
        dano = random.randint(self.dano_min, self.dano_max)
        print(f"💥 {self.nome} ataca {alvo.nome} e causa {dano} de dano!")
        alvo.receber_dano(dano)

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f"{self.nome} (❤️ {self.vida}/{self.vida_maxima})"

class Jogador:
    """Representa o jogador, com energia que funciona como vida."""
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.energia_maxima = 100

    def atacar(self, alvo):
        custo_energia = 10
        if self.energia < custo_energia:
            print("⚡ Energia insuficiente para atacar! Você precisa descansar.")
            return False

        self.energia -= custo_energia
        dano = random.randint(15, 25)
        alvo.vida -= dano
        if alvo.vida < 0:
            alvo.vida = 0
        print(f"⚔️  Você ataca {alvo.nome}, causando {dano} de dano.")
        return True

    def descansar(self):
        if self.energia == self.energia_maxima:
            print("💤 Energia já está no máximo.")
            return
        
        energia_recuperada = 20
        print(f"💤  Você descansa e recupera {energia_recuperada} de energia.")
        self.energia += energia_recuperada
        if self.energia > self.energia_maxima:
            self.energia = self.energia_maxima

    def receber_dano(self, dano):
        self.energia -= dano
        if self.energia < 0:
            self.energia = 0
    
    def esta_vivo(self):
        return self.energia > 0

    def __str__(self):
        return f"Jogador: {self.nome} (⚡ {self.energia}/{self.energia_maxima})"

class Menu:
    """Exibe o menu principal e gerencia as escolhas do jogador."""
    def mostrar(self):
        limpar_tela()
        print("="*30)
        print("      ARENA DE COMBATE")
        print("="*30)
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
        print("="*30)

    def obter_escolha(self):
        return input("Escolha uma opção: ")

def iniciar_jogo():
    """Contém o loop principal do jogo, da criação à conclusão."""
    limpar_tela()
    jogador = Jogador("Valente")
    placar = Pontuacao()
    
    pool_inimigos = [
        Inimigo("Goblin Fraco", vida=40, dano_min=5, dano_max=10),
        Inimigo("Orc Musculoso", vida=60, dano_min=8, dano_max=18),
        Inimigo("Feiticeiro das Sombras", vida=50, dano_min=10, dano_max=20)
    ]
    
    num_inimigos = random.randint(1, 3)
    inimigos_da_partida = random.choices(pool_inimigos, k=num_inimigos)
    
    print(f"Prepare-se! Você enfrentará {num_inimigos} inimigo(s)!\n")
    time.sleep(2)

    for i, inimigo_atual in enumerate(inimigos_da_partida):
        limpar_tela()
        print(f"--- Inimigo {i+1} de {num_inimigos} ---")
        print(f"Um {inimigo_atual.nome} selvagem aparece!\n")

        while inimigo_atual.esta_vivo() and jogador.esta_vivo():
            print(f"{jogador} | {placar}")
            print(f"Inimigo: {inimigo_atual}")
            print("-" * 20)
            
            escolha = input("O que você faz? (1-Atacar, 2-Descansar): ")
            limpar_tela()

            if escolha == '1':
                jogador.atacar(inimigo_atual)
                if not inimigo_atual.esta_vivo():
                    print(f"☠️  {inimigo_atual.nome} foi derrotado!")
                    placar.adicionar(10)
                    time.sleep(2)
                    break
            elif escolha == '2':
                jogador.descansar()
            else:
                print("Opção inválida!")

            time.sleep(1)
            
            # Turno do inimigo
            if inimigo_atual.esta_vivo():
                print("\n--- Turno do Inimigo ---")
                inimigo_atual.atacar(jogador)
                time.sleep(2)

            if not jogador.esta_vivo():
                print("\n" + "="*30)
                print("☠️  VOCÊ FOI DERROTADO! ☠️")
                print(f"Pontuação final: {placar.pontos}")
                print("="*30)
                input("\nPressione Enter para voltar ao menu...")
                return

    print("\n" + "="*30)
    print("🏆 PARABÉNS! Você derrotou todos os inimigos! �")
    print(f"Sua pontuação final é: {placar.pontos} pontos!")
    print("="*30)
    input("\nPressione Enter para voltar ao menu...")

def mostrar_opcoes():
    limpar_tela()
    print("="*30)
    print("            OPÇÕES")
    print("="*30)
    print("- O objetivo é derrotar todos os inimigos da arena.")
    print("- Atacar custa 10 de energia.")
    print("- Descansar recupera 20 de energia.")
    print("- Se sua energia chegar a 0, você perde o jogo.")
    print("- Cada inimigo derrotado vale 10 pontos.")
    print("="*30)
    input("\nPressione Enter para voltar ao menu...")

# --- Ponto de Entrada Principal ---
if __name__ == "__main__":
    menu = Menu()
    while True:
        menu.mostrar()
        escolha = menu.obter_escolha()

        if escolha == '1':
            iniciar_jogo()
        elif escolha == '2':
            mostrar_opcoes()
        elif escolha == '3':
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(1)
