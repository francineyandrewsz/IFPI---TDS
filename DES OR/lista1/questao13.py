'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.'''

def valor_s(n):
    s = 0
    for i in range(1, n+1):
        s += 1/i
    return s

while True:
    try:
        num = int(input('Digite um valor inteiro positivo: '))
        print(f'O valor de {num} é igual a {valor_s(num):.2f}')
        break
    except:
        print('Error no programa! Tente novamente.')
        