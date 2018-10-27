def funcao():
    return 'Hello World!'
# crio uma função que retorna "Hello World!"

a = funcao()
# atribuo para "a" o retorno da função

print(a)
print(funcao().title())

# Se a função não retorna nada, a saíde será "none"

# OBS: A funcao deve ter um nome com todas as letras minúsculas

def somar(x, y):
    return x + y

print(somar(3,5))

# Parametros: Quando definimos a função (x e y)
# Argumentos: Quando chamamos a função (3 e 5)

print(somar(somar(3,5), somar(2,2)))

somar(y=2,x=6)
# Quando chamo a função sem me preocupar com a ordem dos argumentos

def subtrair(x, y=5):
    return x + y

print(subtrair(3,4))
#Se eu não tivesse passado o argumento 4 para y, a função "subtrair" utilizaria y=5

def func():
    pass

for x in range(1):
    pass
# Utilizamos o "pass" para ele ignorar o comando anterior, o código irá rodar normalmente
#como se a função ou comando nem existisse