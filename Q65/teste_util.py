from util_arquivos.escrita import escrever_arquivo
from util_arquivos.leitura import ler_arquivo


NOME_ARQUIVO = "mensagem.txt"
MENSAGEM = "Olá, mundo!"

def main():
   
    print(f"Criando o arquivo '{NOME_ARQUIVO}' e escrevendo a mensagem...")
    escrever_arquivo(NOME_ARQUIVO, MENSAGEM)
    print("Arquivo criado com sucesso!")

    print("-" * 20)

  
    print(f"Lendo o conteúdo do arquivo '{NOME_ARQUIVO}'...")
    conteudo_lido = ler_arquivo(NOME_ARQUIVO)

    
    print("\nConteúdo lido do arquivo:")
    print(conteudo_lido)

if __name__ == "__main__":
    main()