'''Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.'''

lista_x = []
lista_y = []
def criar_lista():
    for c in range(5):
        lista_x.append(input('Digite elementos da lista X: '))
    print(f'Os elementos da Lista X = {lista_x}')
    #O mesmo conteúdo da lista x, só que inverso
    lista_y = lista_x[::-1]
    print(f'Os elementos da Lista Y = {lista_y}')

criar_lista()
