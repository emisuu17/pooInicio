from operacoes import somar, multiplicar
from matematica import somar, potencia

resultado = multiplicar(somar(5, 3), 2)
print(resultado)

print("Executando o codigo da questão 63")

resultado_soma = somar(2, 3)
resultado_potencia = potencia(2, 3)

print(f"O resultado de somar(2, 3) é: {resultado_soma}")
print(f"O resultado de potencia(2, 3) é: {resultado_potencia}")