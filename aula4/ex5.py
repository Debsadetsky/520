lista = []

def funcao():
    for x in range (1, 11):
        lista.append((lambda y: y**2)(x))
    return lista

print(funcao())

#ou

quadrados = [lambda x : x**2 for x in range(1,11)]
print(quadrados)

#ou

quadrado = list(map(lambda x: x**2, range (1,11)))
print(quadrado)
#map()
