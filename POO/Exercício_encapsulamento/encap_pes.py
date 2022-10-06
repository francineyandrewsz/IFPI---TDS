class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, altura:float, sexo:str, estado='vivo(a)', estado_civil='solteiro(a)'):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = None
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        self.__idade = valor
        print('Sem permissão!')
    
    @property
    def peso(self):
        return self.__peso
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def estado_civil(self):
        return self.__estado_civil
    
    @property
    def conjuge(self):
        return self.__conjuge
    
    def envelhecer(self):
        #atualizar em 1 ano a idade da pessoa
        self.__idade += 1
        #sendo a idade menor que 21, deve crescer 0,5 cm
        if self.__idade < 21:
            self.__altura += 0.5
        print(f'{self.__nome} tem {self.__idade} anos de idade e {self.__altura} cm de altura')
    
    def engordar(self, valor):
        #somar o peso atual da pessoa ao argumento valor do método
        self.__peso += valor
        if self.__estado == 'vivo(a)':
            print(f'{self.__nome} engordou {valor} e agora pesa {self.__peso} Kg')
        else:
            print(f'Operação não realizada. {self.__nome} está morto(a)')
    
    def emagrecer(self, valor):
        #subtrair o peso atual da pessoa ao argumento valor do método
        self.__peso -= valor
        if self.__estado == 'vivo(a)':
            print(f'{self.__nome} emagreceu {valor} e agora pesa {self.__peso} Kg')
        else:
            print(f'Operação não realizada. {self.__nome} está morto(a)')
    
    def crescer(self, valor):
        #se a pessoa tiver até 21 de idade
        if self.__idade <= 21:
            #somar a altura atual com o valor do método
            self.altura += valor
            print(f'{self.__nome} cresceu {valor} e agora tem {self.__altura} cm de altura')
        else:
            print(f'{self.__nome} já não pode mais crescer, pois já tem 21 anos ou mais')
    
    def casar(self, conjuge):
        #mudar o estado civil da pessoa (self) para “casado(a)”
        if type(conjuge) == Pessoa:
            if self.estado == 'vivo(a)' and conjuge.estado == 'vivo(a)':
                if self.idade >= 18 and conjuge.idade >= 18:
                    if self.estado_civil != 'casado(a)' and conjuge.estado_civil != 'casado(a)':
                        conjuge.__estado_civil = 'casado(a)'
                        self.__conjuge = conjuge
                        conjuge.__conjuge = self
                        print(f'{self.__nome} está casado(a) com {self.__conjuge}')
                    else:
                        print(f'Casamento não realizado. {self.__conjuge} é casado(a)!')
                else:
                    print(f'Casamento não permitido. {self.__conjuge} é de menor')
            else:
                print(f'Casamento não realizado. {self.__conjuge} está morto(a)')
        else:
            print(f'Casamento não realizado. {self.__conjuge} não representa uma Pessoa!')

    def morrer(self):
        self.__estado = 'morto(a)'
        if self.__estado_civil == 'casado(a)':
            conjuge = self.conjuge
            if conjuge.estado == 'vivo(a)':
                conjuge.__estado_civil = 'viuvo(a)'
        print(f'{self.__nome} morreu')
    
    
if __name__== '__main__':
    #objeto de nome maria
    maria = Pessoa(nome='Maria', idade=5, peso=20, altura=100, sexo='M')
      
    #objeto de nome joao
    joao = Pessoa(nome='João', idade=12, peso=40, altura=140, sexo='M')
    
    #objeto de nome pedro
    pedro = Pessoa(nome='Pedro', idade=22, peso=65, altura=170, sexo='M')
    
    #objeto de nome bia
    bia = Pessoa(nome='Bia', idade=18, peso=55, altura=160, sexo='F')
    
    ##objeto de nome julia
    julia = Pessoa(nome='Julia', idade=30, peso=65, altura=170, sexo='F')
    
    #objeto de nome cadu
    cadu = Pessoa(nome='Carlos Eduardo', idade=2, peso=11, altura=80, sexo='M')
    
    #objeto de nome jonas
    jonas = Pessoa(nome='Jonas', idade=34, peso=70, altura=180, sexo='M')

    #Realize as operações abaixo:
    #a) atribua a idade de maria para o valor: 10
    maria.idade=10
    #b) Maria fez aniversário. Chame o método necessário.
    maria.envelhecer()
    #c) Pedro quer crescer 2 cm. Chame o método necessário.
    pedro.crescer(2)
    #d) Bia quer casar com Carlos. Chame o método necessário.
    bia.casar('Carlos Eduardo')
    #e) Pedro quer casar com Maria. Chame o método necessário.
    pedro.casar('Maria')
    #f) Pedro quer casar com Julia.
    pedro.casar('Julia')
    #g) Pedro quer casar com Bia.
    pedro.casar('Bia')
    #h) Maria morreu.
    maria.morrer()
    #i) Maria quer engordar.
    maria.engordar(2)
    #j) Bia quer casar com Jonas.
    bia.casar('Jonas')
    #k) Bia morreu.
    bia.morrer()
    #l) Pedro Morreu
    pedro.morrer()
    #m) Jonas quer casar com Júlia
    jonas.casar('Júlia')