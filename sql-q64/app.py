from banco_dados_nosql import Conexao
from banco_dados_sql import Conexao

def main():

    print("Iniciando a aplicação...")
    conexao_db = Conexao()
    status = conexao_db.conectar()
    
    print(f"Resultado da conexão: {status}")

if __name__ == "__main__":
    main()

