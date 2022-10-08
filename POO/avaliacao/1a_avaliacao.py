'''Utilizando a linguagem python, crie uma classe para abstrair um Cartão de Crédito.
Atributos: numero, titular(dono), validade (mês,ano), limite_de_compras, cod_segurança, senha,
fatura_a_pagar, status (bloqueado/liberado)
Atributos opcionais: limite_de_compras.
• Todo cartão criado terá limite (opcional) padrão de R$ 100 para compras.
• Todo cartão criado terá os atributos: fatura_a_pagar=0, senha=None e status=’bloqueado’.
Criar construtor, encapsulamento e decoradores. Os atributos: numero, validade,
limite_de_compras, limite_saque, cod_segurança, fatura_a_pagar, valor_minimo_a_pagar e status
não podem ter decoradores de escrita (@setter).
Métodos:
• Desbloquear(...) – Muda o status do cartão para: “liberado”
• Bloquear(...) – Muda o status do cartão para: “bloqueado”
• Mudar_senha(...) – permite mudar a senha atual do cartão. Para isto é necessário que o titular do
cartão digite o código de segurança do mesmo. É necessário que o titular mude a senha pelo
menos uma vez.
• Comprar(...) – Permite realizar uma compra com o cartão. Para a compra ser aprovada é preciso:
a) que o valor seja menor que o limite de compras do cartão
b) que o cartão não esteja bloqueado
c) que o cartão não esteja vencido
d) que a senha esteja correta
Após a compra ser aprovada:
a) atualizar o limite de compras do cartão (diminuindo).
b) atualizar o atributo fatura_a_pagar (aumentando).
c) atualizar o valor_minimo_a_pagar: (30%) do total da fatura (fatura_a_pagar)
• pagar_fatura(...) – paga a fatura com o valor aceitável entre: o valor_minimo_a_pagar e o valor
total da fatura (fatura_a_pagar)
Após o pagamento da fatura:
a) atualizar o atributo: fatura_a_pagar, deduzindo do valor que foi pago.
b) Atualizar o limite do cartão (limite_de_compras) com o valor que foi pago.
• __str__ : retornar uma string com o numero do cartão, o nome do titular, o valor da
fatura e o valor mínimo a pagar
OBS: colocar prints em todos os métodos para saber se a operação foi realizada ou não.
Execução:
• Criar no mínimo 4 objetos (cartões) e realizar todas as operações possíveis através dos métodos
implementados.
'''
from datetime import *

class CartaodeCredito:
    def __init__(self, numero, titular, validade, cod_seg, limite_de_compras= 100):
        self.__numero = numero
        self.__titular = titular
        self.__validade = datetime.strptime(validade, '%m/%Y')
        self.__limite_de_compras = limite_de_compras
        self.__cod_seg = cod_seg
        self.__senha = None
        self.__fatura_pag = 0
        self.__status = 'bloqueado'

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def validade(self):
        return self.__validade
    
    @property
    def limiteCompras(self):
        return self.__limite_de_compras
    
    @property
    def codigo(self):
        return self.__cod_seg
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def fatura(self):
        return self.__fatura_pag
    
    @property
    def status(self):
        return self.__status
    
    def mudar_senha(self):
        if self.__status == 'liberado':
            codigo = input('Digite o código de segurança: ')
            if codigo == self.__cod_seg:
                novo = input('Digite sua nova senha: ')
                self.__senha = novo
                print('senha alterada com sucesso.')
            else:
                print('Código inválido')
        else:
            print('O cartão está bloqueado')
            

    
    def desbloquear(self):
        #Muda o status do cartão para: “liberado”
        if self.__status == 'bloqueado':
            self.__status = 'liberado'
            print('O cartão está liberado')
            if self.__senha == None:
                self.mudar_senha()
        else:
            print('O cartão já está liberado')

    def bloquear(self):
        #Muda o status do cartão para: “bloqueado”
        if self.__status == 'liberado':
            self.__status = 'bloqueado'
            print('O cartão está bloqueado')
        else:
            print('O cartão já está bloqueado')

    
    def comprar(self, valor):
        #Permite realizar uma compra com o cartão. Para a compra ser aprovada é preciso:
        #a) que o valor seja menor que o limite de compras do cartão
        if valor <= self.__limite_de_compras and self.__status == 'liberado':
            if str(date.today()) <= str(self.__validade):
                senha = input('Digite a senha: ')
                if senha == self.__senha:
                    print('A compra está aprovada.')
                    self.__limite_de_compras -= valor
                    self.__fatura_pag += valor
                else:
                    print('Senha incorreta')
            else:
                print('O cartão está vencido')
        else:
            print('O cartão está bloqueado ou a compra é acima do limite.')


    def pagar_fatura(self, valor):
        valor_min = 0.3 * self.__fatura_pag
        if valor <= valor_min:
            print('Valor insuficiente')
        else:
            self.__fatura_pag -= valor
            if self.__fatura_pag < 0:
                self.__fatura_pag = 0
            self.__limite_de_compras += valor
            print(f'Sua fatura agora {self.__fatura_pag} e seu limite agora é {self.__limite_de_compras}')

    def __str__(self):
        print(f'Número do cartão: {self.__numero}\nTitular: {self.__titular}\nValor da fatura: {self.__fatura_pag}\nValor minimo a pagar: {0.3*self.__fatura_pag}')
          
cliente1 = CartaodeCredito('1234', 'Nícolas', '03/2028', '0532')
cliente1.desbloquear()
cliente1.comprar(80)
cliente1.pagar_fatura(50)
cliente1.bloquear()
cliente1.__str__()

cliente2 = CartaodeCredito('888', 'Amanda', '08/2010', '9652')
cliente2.desbloquear()
cliente2.comprar(200)
cliente2.pagar_fatura(20)
cliente2.bloquear()
cliente2.__str__()

cliente3 = CartaodeCredito('13555', 'Franciney', '04/2025', '8642')
cliente3.desbloquear()
cliente3.comprar(15)
cliente3.pagar_fatura(15)
cliente3.bloquear()
cliente3.__str__()

cliente4 = CartaodeCredito('321', 'Adalberto', '07/2030', '8754')
cliente4.desbloquear()
cliente4.comprar(120)
cliente4.pagar_fatura(50)
cliente4.bloquear()
cliente4.__str__()
