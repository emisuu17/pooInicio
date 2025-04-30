class Livro:
    def __init__(self):
        self.nome = 'chapeuzinho vermelho'
        self.preço = '10$'
        self.plataforma = 'digital'

livro1 = Livro()

livro1.nome = 'jojo'
livro1.preço = 20
livro1.plataforma = 'fisico'
print(livro1.nome)
print(livro1.preço)
print(livro1.plataforma)

class ContaBancaria:
    def __init__(self):
        self.nome = None
        self.banco = None
        self.dinheiro = None

contaBancaria1 = ContaBancaria()

contaBancaria1.nome ='jose'
contaBancaria1.banco = 'caixa'
contaBancaria1.dinheiro = '10000$'

print(contaBancaria1.nome)
print(contaBancaria1.banco)
print(contaBancaria1.dinheiro)

class Tarefa:
    def __init__(self):
        self.tarefa1 = None
        self.tarefa2 = None
        self.tarefa3 = None

tarefas = Tarefa()

tarefas.tarefa1 = 'limpar o quarto'
tarefas.tarefa2 = 'limpar casa'
tarefas.tarefa3 = 'lavar roupa'

print(tarefas.tarefa1)
print(tarefas.tarefa2)
print(tarefas.tarefa3)




