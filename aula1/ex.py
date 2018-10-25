idade = int(input('qual a sua idade? '))
if (idade>=18):
    print("voce pode entrar no cinema")
else:
    bin = str(input('Esta acompanhado dos pais? '))
    if(bin=='sim'):
        print("voce pode entrar no cinema")
    else:
        print("voce nao pode entrar no cinema")
