'''Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''
lista_núm = []
maior = menor = 0 
while True:
    try:
        for c in range(0, 15):
            lista_núm.append(int(input(f'Digite um valor para a Posição {c}: ')))
            if c == 0:
                maior = menor = lista_núm[c]
            else:
                if lista_núm[c] > maior:
                    maior = lista_núm[c]
                if lista_núm[c] < menor:
                    menor = lista_núm[c]
        break
    except:
        print('Operação inválida! Tente novamente...')
print(f'Você digitou os Valores {lista_núm}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_núm):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_núm):
    if v == menor:
        print(f'{i}...', end='')
print()
 