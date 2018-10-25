quantidade = int(input("Quantas provas voce teve por semestre? "))

soma = 0
semestre = {}
for x in range(2):
    print('Notas do semestre {}'.format(x+1))
    for y in range (quantidade):
        nota = float(input('Nota da prova {}: '.format(y+1)))
        soma += nota 

    media = float(soma/quantidade)

    if(media>=7):
        print("Aprovado com média {}.".format(media))
    elif(media>3):
        print("Recuperação com média {}.".format(media))
    else:
        print("Reprovado com média {}.".format(media))
    soma = 0
    semestre['Semestre {}'.format(x+1)] = media

sum = float(semestre['Semestre 1']) + float(semestre['Semestre 2'])

if(sum/2 < 7):
    print("Bombou")
else:
    print('Ufa!')

print(semestre)
