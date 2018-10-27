def parametross(*args):
    print(args)

parametross('daniel', 'maria', 5, [], {})

# Tudo que eu passar em args vai virar uma tupla

def parametros(**kwargs):
    print(kwargs['nome'])

parametros(nome = 'daniel', idade = 24)

# Tudo que eu passar em kwargs vai virar um dicionário
# Dicionário é um objeto desordenado (não importa a ordem)

