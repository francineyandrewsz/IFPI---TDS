'''Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.'''
from random import randint
um = dois = três = quatro = cinco = seis = 0
jogador = int(input('Faça sua jogada: '))
for c in range(jogador):
    d = randint(1, 6)
    if d == 1:
        um += 1
    if d == 2:
        dois += 1
    if d == 3:
        três += 1
    if d == 4:
        quatro += 1
    if d == 5:
        cinco += 1
    if d == 6:
        seis += 1
print(f'1 caiu {um} vezes\n2 caiu {dois} vezes\n3 caiu {três} vezes\n4 caiu {quatro} vezes\n5 caiu {cinco} vezes\n6 caiu {seis} vezes')

        