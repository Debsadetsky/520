convidados = []

def dados()
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    telefone = input("Digite seu celular ")
    acompanhado = input("Você está acompanhado? (sim/nao) ").strip().lower()
    convidado = {'Nome': nome, 'Idade:' idade, 'Celular': celular, 'Acompanhado': acompanhado}
    return convidado
    pass

def continuar()
    while True:
    continua = input("Tem mais um convidado para inserir? ")
    if continua.strip().lower() == 'nao':
        break
    dados()
    adicionar (nome, idade, telefone, acompanhado)
    pass

def adicionar(nome, idade, telefone, acompanhado)
    '''função para adicionar convidados na lista'''
    global convidados
    if w = 's':
        dados()
    else:

    convidados.insert(convidado)
    pass
    return None
pass
adicionar()
# (nome da função).__doc__ traz a especificação 
# A especificação será o comentário feito dentro da função

