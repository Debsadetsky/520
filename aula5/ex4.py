class Pai:
    a = "Classe Pai"
    b = "Classe"

class Mae:
    b = "Classe Mae"
    a = "Classe"
    d = "ulala"

class Filho(Pai, Mae):
    c = "Classe Filho"

objeto = Filho()

print(objeto.a, objeto.b, objeto.c, objeto.d)
#Uma classe com heranca múltipla herda os objetos da primeira classe
