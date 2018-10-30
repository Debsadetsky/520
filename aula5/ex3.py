'''
atributos = Titular, numero da conta e o saldo
metodos = depositar, sacar, transferir
'''

class Conta(): 
    #A classe sempre deve ter a inicial maiúscula
    '''Tentando abstrair uma conta corrente'''
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.taxa = 0.5
    
    def depositar(self, valor):
        '''Método que faz depósito em uma conta'''
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        '''Método que faz saque de uma conta'''
        if self.saldo >= (valor + self.taxa):
            self.saldo -= (valor+ self.taxa)
            return 'Saque realizado com sucesso!'
        else:
            raise ValueError("Saldo insuficiente: {}".format(self.saldo))

    def transferir(self, valor, conta):
        '''Método que faz tranferencia de uma conta para outra'''
        try:
            self.sacar(valor)
            conta.depositar(valor)
            return "Transferência realizada com sucesso! :)"
        except ValueError as e:
            print(e)
            return "Não foi possível realizar a tranferência. :("
        except Exception:
            return "Conta destino inválida! :("
        
    def __str__(self):
        return "Conta: {}  Titular: {}".format(self.numero, self.titular)

class Poupanca(Conta):
    #A classe "Poupança" herda tudo da classe "Conta"
    #Além disso podemos acrescentar coisas
    def __init__(self, titular, numero, saldo):
        super().__init__(titular, numero, saldo)
        self.taxa = 0

    def render_juros(self):
        self.saldo += self.saldo * 0.005


