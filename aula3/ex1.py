letras = ['a', 'b']
ling = {'Daniel':'Python'}

try:
    print(letras[2])
except IndexError:
    print('A lista contém apenas {} elementos.'.format(len(letras)))

print(ling.get('Maria')) # maria ta ai? se não devolve 'none'