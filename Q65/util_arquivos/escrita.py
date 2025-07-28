def escrever_arquivo(nome_arquivo: str, texto: str) -> None:
   
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")