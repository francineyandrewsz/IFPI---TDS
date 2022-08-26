class Relógio_Digital_Simples:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.bateria = True
        self.cor = 'Prata'
        self.modelo = 'Omega'
        
    def alteração(self):
        if self.bateria == True:
            self.horas = int(input('Digite a hora: '))
            self.minutos = int(input('Digite os minutos: '))
            self.segundos = int(input('Digite os segundos: '))
        else:
            self.horas = 0
            self.minutos = 0
            self.segundos = 0
            
if __name__ == "__main__":
    relogio1 = Relógio_Digital_Simples()
    print(f'Meu relógio de marca {relogio1.modelo} e cor {relogio1.cor}')
    relogio1.alteração()
    print(f'A hora atual é de {relogio1.horas}:{relogio1.minutos}:{relogio1.segundos}')
    
    