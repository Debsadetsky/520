'''
ler um número e dizer se é par ou ímpar
'''
numero = int(input("Digite um número inteiro: "))

if(numero%2==0):
    print("Esse número é par.")
else:
    print("Esse número é ímpar.")

'''
criar uma lista com os números pares de 0 a 100
'''

pares = []
for x in range (100):
    if(x%2 == 0):
        pares.append(x)
print(pares)

'''
ou
'''

even = list(range(0,100,2))