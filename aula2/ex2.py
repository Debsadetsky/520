'''
Dado uma matriz

m = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]

somar todos os elementos da diagonal principal e da diagonal secundária
'''

m = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]
soma=0
cont=2
for n in range(3):
    soma+= m[n][n] + m[n][cont]
    cont-=1
print(soma)

# ou
#a = 0
#for c,i in enumerate(m):
#    a += i[c] + i[-(c+1)]
#print(a)
