class Bike:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.cor = 'Preta'
        self.aro = 26
        self.veloc_atual = 0
        self.altura_cela = 5
        self.calibragem_pneus = 20

    def pedalar(self):
        self.veloc_atual = int(input('Digite sua velocidade: '))
        if self.veloc_atual > 0:
            print(f'Estou pedalando na bike com velocidade de {self.veloc_atual} Km/h')
    def frear(self):
        self.veloc_atual = 0
        print(f'A bike está parada')
    def regular_cela(self):
        self.altura_cela = int(input('Digite a altura da cela: '))
        print(f'A altura da cela é {self.altura_cela}')
    def calibrar_pneus(self):
        self.calibragem_pneus = int(input('Digite sua calibragem: '))
        print(f'A calibragem está em {self.calibragem_pneus}')

if __name__ == "__main__":
    bike1 = Bike('13', '110')
    print(f'Minha bike pesa {bike1.peso} Kg e tem {bike1.altura} cm de altura')
    print(f'Sua cor é {bike1.cor} e possui aro {bike1.aro}')
    bike1.pedalar()
    bike1.frear()
    bike1.regular_cela()
    bike1.calibrar_pneus()


