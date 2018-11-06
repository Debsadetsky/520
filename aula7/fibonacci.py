N = int(input())
fibonacci = []
aux = 1
for i in range(0, N):
    if(i == 0):
        aux = 0
    elif(i == 1):
        aux = 1
    else:
        aux +=  fibonacci[i-2]
    fibonacci.append(aux)
fibonacci = list(map(str, fibonacci))
print(' '.join(fibonacci))