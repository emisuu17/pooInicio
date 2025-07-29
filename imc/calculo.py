def calcular_imc(peso: float, altura: float) -> float:
   
    if altura <= 0:
        raise ValueError("A altura deve ser um valor positivo.")
    
    imc = peso / (altura ** 2)
    return imc