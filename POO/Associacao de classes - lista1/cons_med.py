from typing import Type
from random import *
class Médico:
    def __init__(self, crm:int, nome:str, especialidade:str):
        self.__crm = crm
        self.__nome = nome
        self.__especialidade = especialidade
    
    @property
    def crm(self):
        return self.__crm
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def especialidade(self):
        return self.__especialidade

class Paciente:
    def __init__(self, cpf:int, nome:str):
        self.__cpf = cpf
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome

consulta = {'Dia': randint(1, 31), 'Mês': randint(1, 12), 'Ano': randint(2022, 2024)}
class ConsultaMédica:
    def __init__(self):
        self.__data_consulta = None
        self.__data_retorno = None
        self.__valor = 300
        self.__pago = False
       
           
    @property
    def data_consulta(self):
        return self.__data_consulta
    
    @property
    def data_retorno(self):
        return self.__data_retorno
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def pago(self):
        return self.__pago
    
       
    def agendar_consulta(self, pessoa: Type[Paciente]):
        if pessoa == self.__data_consulta:
            for v in consulta.values():
                print(f'Sua consulta foi marcada para o dia {v[0]}/{v[1]}/{v[2]}')
    
    def pagar_consulta(self):
        self.__pago = True
    
    def cancelar_consulta(self):
        self.__data_consulta = None
    
    def agendar_retorno(self, data):
        self.__pago == True
        print('Consulta paga')

#Objeto     
medico = Médico(crm=1234, nome='Afonso', especialidade='Cirurgia')

paciente = Paciente(cpf=234, nome='Andrews')
paciente = ConsultaMédica()
paciente.agendar_consulta(consulta)
paciente.pagar_consulta = 300
paciente.cancelar_consulta()
paciente.agendar_retorno(consulta)
    