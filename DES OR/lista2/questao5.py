'''Faça um programa que leia duas listas de 10 elementos
 numéricos cada um e intercale oselementos deste em uma
  outra lista de 20 elementos.
  Exemplo:  l1 = [2, 6, 9] l2 = [10, 5, 12]
  lista intercalada l3 = [2, 10, 6, 5, 9, 12]
  Obs: Fazer uma segunda versão funçao para intercalar sem usar o comando append'''

l1 = []
l2 = []
def gravar_lista():
    for c in range(1, 11):
        l1.append(int(input(f'Digite o {c}ª valor da l1: ')))
    for c in range(1, 11):
        l2.append(int(input(f'Digite o {c}ª valor da l2: ')))
    print(f'A lista l1 = {str(l1)}')
    print(f'A lista l2 = {str(l2)}')
    l3 = l1 + l2
    l3[::2] = l1
    l3[1::2] = l2
    print(f'A lista intercalada é l3 = {l3}')

gravar_lista()
