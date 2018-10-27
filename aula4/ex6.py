
def ler_arquivo(nome_arq:str)->list:
    ''' 
    Função para ler arquivo
    -> str nome do arquivo
    return -> list conteúdo do arquivo
    '''
    with open(nome_arq, 'r') as arquivo:
        return arquivo.readlines()

def escrever_arquivo(nome_arq, conteudo):
    '''
    Funço para escrever em um arquivo
    '''
    with open(nome_arq, 'a') as arquivo:
        arquivo.write(conteudo + '\n')

    return

'''
if __name__ == '__main__':
    print('hello')
'''