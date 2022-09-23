'''Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista.
'''
def cont_Par(lista_núm):
    pares = 0
    for n in lista_núm:
        if n % 2 == 0:
            pares += 1
    return pares
def cont_Impar(lista_núm):
    impares = 0
    for n in lista_núm:
        if n % 2 == 1:
            impares += 1
    return impares
    
lista_núm = list(range(4))
q = int(input('Quantos valores haverá na lista? '))
while q < 0:
    try:
        q = int(input('Quantos valores haverá na lista? '))
    except:
        print('Operação inválida! Tente novamente...')

for c in range(q):
    num = int(input(f'Digite o {c}ª valor: '))
    lista_núm.append(num)

print(f'A quantidade de números pares {cont_Par(lista_núm)}')
print(f'A quantidade de números impares {cont_Impar(lista_núm)}')

