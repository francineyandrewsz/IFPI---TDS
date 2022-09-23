'''Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.'''
from random import randint

lista_X= []
lista_R= []

def copiar_lista():
    for i in range(10):
        lista_X.append(randint(-5, 5))

    for c in range(len(lista_X)):
        if lista_X[c] < 0:
            lista_R.append(lista_X[c])
  
    print(f'Lista X = {lista_X}')
    print(f'Lista R = {lista_R}')

copiar_lista()
