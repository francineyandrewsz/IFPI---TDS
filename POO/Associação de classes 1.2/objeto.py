from classes import Banco
from classes import Conta
from classes import Cliente

# 3 Instâncias de cliente, 6 Instâncias de conta e 3 Instâncias de banco
b1 = Banco(nome='BANCO MAIS GRANA')
b2 = Banco(nome='Banco VERDÃO')
b3 = Banco(nome='Banco DIN-DIN $_$')
cliente1 = Cliente(cpf=8456.234-23, nome='Andrews')
print(cliente1)
cliente1 = Conta(numero=34567)
print(cliente1)
b1.adicionar(cliente1)
cliente1.depositar(350)
print('-'*40)

cliente2 = Cliente(cpf=8934.345, nome='Ângela')
print(cliente2)
cliente2 = Conta(numero=63527)
print(cliente2)
b2.adicionar(cliente2)
cliente2.sacar(234)
print('-'*40)

cliente3 = Cliente(cpf=45623.345, nome='Lima')
print(cliente3)
cliente3 = Conta(numero=624892)
print(cliente3)
b3.adicionar(cliente3)
cliente3.depositar(1287)
print(cliente3)
print('-'*40)