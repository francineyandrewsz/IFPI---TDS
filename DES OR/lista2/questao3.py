'''Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''
lista_núm = []
def gravar_lista(lista_núm):
    q = int(input('Digite quantos valores haverá na lista: '))
    for c in range(1, q+1):
        lista_núm.append(int(input(f'Digite o {c}ª número: ')))
    return lista_núm

print(f'Os valores da lista_núm = {gravar_lista(lista_núm)}')
#Sua ordem inversa
lista_núm.reverse()
print(f'E seus valores inverso são = {lista_núm}')
