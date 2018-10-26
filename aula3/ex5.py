nome = input('Digite o nome do seu arquivo: ')

shebang = '#!/usr/bin/python3'

try:

    with open(nome, 'x') as arq:
        arq.write(shebang)
    #se o arquivo nao existir, eu crio um escrevendo a shebang na primeira linha
except FileExistsError:
    with open(nome, 'r') as arq:
        conteudo = arq.readlines()
    #se o arquivo já existir eu atribuo o arquivo existente na variável 'conteudo'
    if conteudo: # é a mesma coisa que 'if len(conteudo) > 0'
        if conteudo[0] != shebang:
            conteudo.insert(0, shebang)
            #se a primeira linha da variavel 'conteudo' for diferente da shebang
            #como a variável 'conteudo' é uma lista, eu adiciono uma linha 0 e insiro a shebang nessa linha
        with open(nome, 'w') as arq:
            arq.writelines(conteudo)
        #apago o arquivo existente e subescrevo a minha variável 'conteudo'
    else:
        with open(nome, 'a') as arq:
            arq.write(shebang)
