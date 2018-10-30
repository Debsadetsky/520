class Dog():
    def __init__(self):
        print('Método Construtor')
        self.nome = 'bilu'
        self.raca = 'pitbull'
        self.idade = 1


dog1 = Dog()
print(dog1.raca)