class Cliente:
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        saida = f'Nome do cliente: {self.__nome}\nCpf: {self.__cpf}'
        return saida



class Conta:

    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0
        self.__titular = Cliente

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Ciente depositou R${valor}')

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Você não pode sacar esse valor.')
        else:
            self.__saldo -= valor
            print(f'Você sacou R${valor}')
        
    def __str__(self):
        conta = f'Conta: {self.__numero}\nSaldo: {self.__saldo}'
        return conta
    

class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []

    @property
    def nome(self):
        return self.__nome

    def adicionar(self, conta):
        if type(conta) == Conta:
            self.__contas.append(conta)
            print(f'Conta adicionada ao {self.__nome}')
        else:
            print('ERROR!')

    def remover(self, conta):
        if type(conta) == Conta:
            self.__contas.remove(conta)
            print(' Conta deletada')
        else:
            print('ERROR!')
            
    
    def ValorTotal(self, total):
        if type(total) == Conta:
            total = self.__contas
    
    
    def __str__(self):
        saída = f'Banco: {self.__nome}\nValor total: {self.__contas}'
        return saída
    


