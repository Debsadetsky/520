var = 10

def escopo():
    var = 5
    print(var)

escopo()
print(var)

# Só mudará  o valor de "var" dentro da função, no entanto 
# quando sair da função, "var" volta a ser 10

def esc():
    global var
    var = 5
    print(var)

escopo()
print(var)

# O tipo "global" muda o valor de "var" dentro e fora da função com os comandos de dentro da função