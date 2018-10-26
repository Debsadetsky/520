ling = input("Qual é a melhor linguagem de programação? ")
ling = ling.strip().lower() 
#strip tira os espaços no início e no final da string e lower tira as letras maiúsculas
print(ling)

try:
    if ling == 'python':
        print('Você está no caminho certo!')
    elif ling == 'html' or ling == 'css':
        raise ValueError('Isso não é uma linguagem de programação.')
        # 'raise' força/cria um erro no Python
    else:
        print('Mude para Python!')
except ValueError as e:
    print(e)
exit()
