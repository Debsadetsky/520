convidados = []

def adicionar(nome, idade):
    '''função para adicionar convidados na lista'''
    global convidados
    convidado = {'nome': nome, 'idade':idade}
    convidados.append(convidado)

# O retorno é opicional

while True:
    nome = input("Digite um nome ou sair: ")
    if nome.strip().lower() == 'sair':
        break
    idade = int(input("Digite a idade: "))
    adicionar (nome, idade)

print(convidados)