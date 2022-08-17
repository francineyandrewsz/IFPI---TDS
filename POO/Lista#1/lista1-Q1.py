class carro1:
    nome = 'Fusca'
    ano = 1965
    cor = 'Preto'
    veloc_max = 80
    veloc_atual = 20
    estado = 'ligado'
    
    def ligar(self, estado):
        self.estado = estado
        print(f'Fusca {self.estado}')
    def acelerar(self, veloc_atual):
        self.veloc_atual += veloc_atual
        print(f'Acelere o fusca para a velocidade: {self.veloc_atual}')
    
    def desligar(self, estado):
        self.estado = estado
        def parar(self, veloc_atual):
            self.veloc_atual = 0
        print(f'Fusca {self.estado}')
    

fusca = carro1()
fusca.ligar('ligado')
fusca.veloc_atual = 20
fusca.acelerar(20)
fusca.desligar('desligado')
fusca.ligar('ligado')
fusca.acelerar(60)
fusca.desligar('desligado')

class carro2:
    nome = 'Ferrari_sr2000'
    ano = 2014
    cor = 'vermelho'
    veloc_max = 300
    veloc_atual = 0
    estado = 'desligado'

    def ligar(self, estado):
        self.estado = estado
        print(f'Ferrari {self.estado}')
    def acelerar(self, veloc_atual):
        self.veloc_atual += veloc_atual
        print(f'Acelere a ferrari para a velocidade: {self.veloc_atual}')
    def desligar(self, estado):
        self.estado = estado
        print(f'Ferrari {self.estado}')
    def parar(self, estado):
        self.estado = estado
        print(f'Ferrari {self.estado}')
        

ferrari = carro2()
ferrari.ligar('ligado')
ferrari.acelerar(200)
ferrari.acelerar(120)
ferrari.parar('Parado')
ferrari.desligar('desligado')

    




        
        
        
 