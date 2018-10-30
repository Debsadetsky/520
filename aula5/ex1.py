class Dog():
    '''Tentando abstrair um dog'''
    def __init__(self, nome, raca, idade, energia):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5

    def latir(self):
        print(self.nome)
        print('Auauauauau...')

    def dormir(self):
        self.energia = 5 
        print('Zzz... {}'.format(self.energia))
        #sleep(5)
        
    def andar(self):
        if self.energia:
            self.energia -= 1
            print('Andando ... {}'.format(self.energia))
        else:
            print('Ele está cansado e não pode mais andar.')
    
    def __str__(self):
        return 'nome: {}  idade: {}  raça: {} '.format(self.nome, self.idade, self.raca)

dog1 = Dog('bilu', 'pitbull', 1, 5)
dog2 = Dog('rex', 'poodle', 2, 5)

#print(dog1.nome)
#print(dog2.nome)

dog2.latir()