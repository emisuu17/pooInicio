def ler_arquivo(nome_arquivo: str) -> str:

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return f"Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {e}"