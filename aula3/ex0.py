'''
try:
    numero = int(input("Digite um número inteiro: "))

    if(numero%2==0):
        print("Esse número é par.")
    else:
        print("Esse número é ímpar.")
except Exception as e:
    print(e)
print("Não parei a execução")
'''

try:
    numero = input("Digite um número inteiro: ")
    numero = int(numero)
    if(numero%2==0):
        print("Esse número é par.")
    else:
        print("Esse número é ímpar.")

except ValueError:
    res = []
    for x in numero:
        res.append(ord(x))
    res = sum(res)
    #res = [ord(x) for x in numero]
    #res=sum(res)
    if  res % 2 == 0:
        print("par {}".format(res))
    else:
        print("ímpar {}".format(res))

except Exception:
    print("Tratamento genérico.")
print("Não parei a execução.")