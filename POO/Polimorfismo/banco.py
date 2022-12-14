class contaCorrente:
    def __init__(self, numero, saldo=0):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def __str__(self):
        return f'Número:{self.__numero}' + f'\nSaldo:{self.__saldo}'

    def creditar(self, valor):
        self.__saldo += valor
        print(f'Com valor acrescendado de  R${valor}, o seu saldo fica R${self.__saldo}')

    def debitar(self, conta, valor):
        if type(conta) == contaCorrente:
            if self.saldo > valor:
                self.saldo -= valor
                print(f'Você tem R${self.saldo} na conta.')

    def transferir(self, valor, conta):
        if type(conta) == contaPoupanca:
            if self.__saldo > 0:
                self.__saldo += valor
                print(f'Seu saldo atual: R${self.__saldo}')
            else:
                print('Saldo Insuficiente')

    def sacar(self, valor):
        valor = self.__saldo - 2
        print(f'O valor do seu saldo ficou R${valor}')


class contaPoupanca(contaCorrente):
    def __init__(self, numero, taxa_juros, saldo=0):
        super().__init__(numero, saldo)
        self.__taxa_juros = taxa_juros

    def render_juros(self, saldo):
        self.__taxa_juros += saldo

    def sacar(self, saque, valor):
        for v in range(1, saque):
            if v > 5:
                valor = self.__saldo - 0.50
                print(f'O valor do seu saldo ficou R${valor}')
            else:
                valor = self.__saldo
                print(f'O valor do seu saldo é R${valor}')
                

    def __str__(self):
        return super().__str__() + '\n' + f'taxa juros:{self.__taxa_juros}'


class contaImposto(contaCorrente):
    def __init__(self, percentual_imposto):
        self.__percentual_imposto = percentual_imposto

    def calcula_imposto(self, valor):
        pass

    def __str__(self):
        return f'Valor do imposto: R${self.__percentual_imposto}'


class Banco:
    def __init__(self):
        self.contas = []
    
    
    def adicionar_conta(self, c):
        if isinstance(c, contaCorrente):
            self.contas.append(c)
            
      
     
    def Sacar(self, conta):
      conta = self.contas
      for i in conta:
        print(i)
            

        
        


print('##### CONTA CORRENTE ######')
print('Cliente 1')
c1 = contaCorrente(1, 200)
print(c1)
c1.creditar(500)
c1.debitar(1, 120)
c1.sacar(valor=20)
c1 = contaImposto(23)
c1.calcula_imposto(2)
print('-' * 15)
print('Cliente 2')
c2 = contaCorrente(2, 350)
print(c2)
c2.debitar(2, 220)
c2.transferir(200, c1)
print(c2)

print('##### CONTA POUPANÇA #####')
c1 = contaPoupanca(1, 23, 300)
print(c1)
#c1.sacar(5, 350)
c2 = contaPoupanca(2, 10)
print(c2)
c2.debitar(2, 150)
print(c2)
c2 = contaImposto(33)
print(c2)
print('-'*15)

print('##### BANCO #####')
banco1 = Banco()
banco1.adicionar_conta(c1)
banco1.Sacar(c1)

