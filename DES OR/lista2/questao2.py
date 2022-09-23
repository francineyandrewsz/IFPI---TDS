'''Faça um programa que grave uma lista com dez números reais,
 calcule e mostre a quantidade de números negativos e a soma 
 dos números positivos dessa lista.'''

lista_núm = []
pos = neg = n = 0
def gravar_lista(lista_núm):
    for c in range(1 ,11):
        lista_núm.append(int(input(f'Digite o {c}ª número: ')))
    return lista_núm

print(f'Os Valores da lista_núm = {gravar_lista(lista_núm)}')
while (n < len(lista_núm)):
    if lista_núm[n] >= 0:
        pos += 1
    else:
        neg += 1
    n += 1
print(f'A quantidade de números positivos são: {pos}')
print(f'A quantidade de números negativos são: {neg}')
