'''Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.'''
lista_X = []
lista_Y = []
def modificar():
    for c in range(1, 11):
        lista_X.append(int(input(f'{c}ª valor: ')))
    print(f'Valores da Lista X = {lista_X}')
    for núm in lista_X:
        if núm % 2 == 0:
            lista_Y.append(núm/2)
        if núm % 2 == 1:
            lista_Y.append(núm*3)
    print(f'Os valores da Lista Y = {lista_Y}')

modificar()
            
    