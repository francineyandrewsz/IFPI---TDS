class Bicicleta:
    def __init__(self, cor, marca, veloc_atual=0):
        self.__cor = cor
        self.__marca = marca
        self.__veloc_atual = veloc_atual 
        self.veloc_max = 20   
    
    def getcor(self):
        return self.__cor

    def getmarca(self):
        return self.__marca

    @property
    def pedalar(self):
        return self.__veloc_atual
    
    @pedalar.setter
    def pedalar(self, velocidade):
        if velocidade > 1:
            self.__veloc_atual += velocidade
            if self.__veloc_atual > self.veloc_max:
                self.__veloc_atual = self.veloc_max
        print(f'Estou pedalando minha bike com velocidade de {self.__veloc_atual} Km/h')
    
    def parar(self):
        if self.__veloc_atual == 0:
            print('Minha bike está parada')
        
        
    
        
        
bike = Bicicleta('Vermelha', 'caloi')
print(f'Minha bike tem a cor {bike.getcor()} e possui marca {bike.getmarca()}')
bike.pedalar = 15

    
    