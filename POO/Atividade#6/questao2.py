estações = {89.5:'Cocais', 91.5:'Mix', 94.1:'Boa', 99.1:'Clube'}

class radioFM:
    def __init__(self, volume, volume_max=10, volume_min=0):
        self.__volume_max = volume_max
        self.volume_min = volume_min
        self.ligado = False
        self.volume = volume
        self.freq_min = 87
        self.freq_max = 110
        self.freq_atual = None
        self.antena_habilitada = False
        self.estacao_atual = None
        
        
    def ligar(self):
        if self.ligado == True:
            print('O rádio está ligado')
        else:
            if self.antena_habilitada == True:
                self.freq_atual = 89.5
                print('O rádio está ligado')
                print('Fraquência está iniciando...')
                print(f'O volume está no {self.volume_min}')
                self.estacao_atual = estações[89.5]
                print(f'Sua estação atual é {self.estacao_atual}')
            else:
                self.ligado = True
                self.volume = self.volume_min
                print('O rádio está ligado')
        
    def desligar(self):
        self.ligado = False
        self.freq_atual = None
        self.estacao_atual = None
        print('O rádio está desligado')
    
    @property
    def mudar_volume(self):
        return self.__volume_max
    
    @mudar_volume.setter
    def mudar_volume(self, volume):
        if self.ligado == True:
            self.volume += volume
            if self.volume > self.__volume_max:
                self.volume = self.__volume_max
            print(f'O volume do rádio está em {self.volume}')
    
    def aumentar_vol(self, mudar_volume=1):
        if self.ligado == True:
            self.volume += mudar_volume
            if self.volume > self.__volume_max:
                self.volume = self.__volume_max
            print(f'Aumentei o volume para {self.volume}')
    
    def diminuir_vol(self, mudar_volume=1):
        if self.ligado == True:
            self.volume -= mudar_volume
            if self.volume < self.volume_min:
                self.volume = self.volume_min
            print(f'Diminui o volume para {self.volume}')
    
    def mudar_freq(self, freq):
        if self.ligado == True:
            if self.antena_habilitada == True:
                if freq > 0 and freq != 0:
                    self.freq_atual = freq
                    for i in estações.keys():
                        if freq == i:
                            self.estacao_atual = estações[i]
                elif freq == 0:
                    self.freq_atual = 89.5
                    self.estacao_atual = estações[89.5]
                    if self.freq_atual == 99.1:
                        self.freq_atual = 89.5
                        self.estacao_atual = estações[89.5]
                else:
                    print('Estação não existe.')
    
    def habilitar_antena(self):
        self.antena_habilitada = True
        self.freq_atual = 89.5
        self.estacao_atual = estações[89.5]
        print('A antena do rádio está habilitada')
        

radio1 = radioFM(5, 30)
radio1.ligar()
radio1.habilitar_antena()
radio1.aumentar_vol(6)
radio1.mudar_freq(99.1)
radio1.estacao_atual
print(' ')
radio2 = radioFM(4, 89.5)
radio2.ligar()
radio2.habilitar_antena()
radio2.mudar_freq(91.5)
radio2.estacao_atual
radio2.aumentar_vol(8)
radio2.diminuir_vol(5)
radio2.desligar()

radio1.mudar_volume

