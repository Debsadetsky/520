'''
arquivo = open('teste.txt', 'r')

print(arquivo.read())

arquivo.close()
'''

with open('teste.txt', 'r') as arquivo:
    cont = arquivo.readlines()

#salvei o arquivo em uma variavel, mesmo fechando o arquivo tenho a variavel
print(cont)

with open('teste.txt', 'a') as arq:
    arq.write('Estou escrevendo lero lero no arquivo\n')
#escreve no final do arquivo

lista = ['a', 'b', 'c']
with open('teste.txt', 'a') as arq:
    for x in lista:
        arq.write('{}\n'.format(x))
#escrevi minha lista no arquivo

with open('teste.txt', 'r') as arquivo:
    #with garante que o arquivo vai fechar quando acabar a identação
    print(arquivo.readlines())
    #readlines transforma todos os elementos do arquivo em uma string, 
    #onde cada linha é o elemento de uma lista
    arquivo.seek(0)
    #zera o cursor
    print(arquivo.read())
    #só read seria uma string contendo todo o arquivo
    arquivo.seek(0)
    #zera o cursor
    print(arquivo.readline(), end='')
    #printa uma linha e o "(end='')" faz nao pular linha depois
    print(arquivo.tell())
    # o 'tell' traz a posição da linha em bytes  

with open('teste.txt', 'w') as arquivo:
    arquivo.writelines(cont)
#apago o conteúdo existente no meu arquivo e dentro dele escrevo um a um dos elementos da lista 'cont'