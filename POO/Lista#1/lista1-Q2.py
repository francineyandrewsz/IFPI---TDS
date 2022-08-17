class Gato:
    nome = None
    sexo = None
    peso = None
    idade = None
    fertil = None
    cio = None
    prenhe = None
    puerperio = None
    
    def receber_nome(self, nome):
        self.nome = nome
    
    def engordar(self, peso):
        self.peso += peso
    
    def envelhecer(self):
        self.idade += 1
        if self.idade >= 1:
            self.fertil = True
    
    def entrar_no_cio(self):
            if self.idade >= 1 and self.sexo == "F":
                self.cio = True
                print(f'{self.nome} está no cio')
                
    
    def cruzar(self, gato):
        if type(gato) == type(Gato()):
            if (self.sexo != gato.sexo) and (self.fertil and gato.fertil) and (self.cio == True or gato.cio == True):
                if self.puerperio != True and gato.puerperio != True:
                    print('Cruzamento realizado com sucesso! Um novo gatinho nasceu.')
                    if self.sexo == 'F':
                        self.prenhe = True
                        self.puerperio = True
                    else:
                        gato.prenhe = True
                        gato.puerperio = True
            print('Um dos gatos não está em condiçoes de acasalar.')
        else:
            print('Informe um gato em condições de acasalamento.')
                        
nino = Gato()
nino.nome = 'Nino'
nino.sexo = 'M'
nino.idade = 2
nino.peso = 1.5
nino.envelhecer()
nino.engordar(1)
print(f'O nome do meu gato é {nino.nome}')
print(f'ele pesa atualmente {nino.peso} quilos')
print(f'sua idade atual é {nino.idade} anos')



luna = Gato()
luna.nome = 'Luna'
luna.sexo = 'F'
luna.idade = 2
luna.peso = 1
luna.envelhecer()
luna.engordar(2)
luna.entrar_no_cio()
print(f'O nome do minha gata é {luna.nome}')
print(f'ela pesa atualmente {luna.peso} quilos')
print(f'sua idade atual é {luna.idade} anos')
