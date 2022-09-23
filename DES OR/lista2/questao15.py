'''Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''
lista_d = []
lista_e = []
def inverso():
    for c in range(1, 11):
        lista_d.append(input(f'Digite o {c}ª número: '))
    print(f'Os elementos da lista D = {lista_d}')
    lista_e = lista_d[::-1]
    print(f'Os elementos da lista E = {lista_e}')

inverso()
