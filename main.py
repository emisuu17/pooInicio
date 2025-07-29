#codigo referente a questão numero 66
from imc import calcular_imc

def main():
    print("--- Calculadora de IMC ---")
    
    try:
        peso_usuario = float(input("Digite seu peso em kg:"))

        altura_usuario = float(input("Digite sua altura em metros:"))

        imc_resultado = calcular_imc(peso_usuario, altura_usuario)

        print(f"\nSeu IMC é: {imc_resultado:.2f}")

    except ValueError:
        print("\nErro: Peso e altura devem ser valores numéricos.")
    except Exception as e:
       
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main()