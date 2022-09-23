'''Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.'''
from random import randint

lista_R= []
lista_X= []

def juntar(lista1, lista2):
   unir = list(lista1 + lista2)
   return unir


for i in range(5):
  lista_R.append(randint(0,10))

for c in range(10):
  lista_X.append(randint(-5,5))

print(f'A lista R = {lista_R}')
print(f'A lista X = {lista_X}')
print(f'As duas unidas são:{juntar(lista_R, lista_X)}')
