from ex3 import Conta, Poupanca

Titular = input("Qual é o nome do Titular da conta? ")
Numero = input("Digite o número da conta: ")

conta1 = Conta(Titular, Numero, 500)
conta2 = Poupanca('Maria', 4234, 500)

print(conta1.transferir(55, conta2))
conta2.render_juros()

print(conta1.saldo)
print(conta2.saldo)

