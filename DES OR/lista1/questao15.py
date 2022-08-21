'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
'''
def valor_s(n):
    s = 0
    for i in range(1, n + 1):
        s += (i ** 2 + 1) / (i + 3)
    return s
while True:
    try:
        num = int(input('Digite um número: '))
        while num < 0:
            num = int(input('Operação inválida! Por favor, digite um número: '))
        print(f'O resultado fica {valor_s(num):.2f}')
        break
    except:
        print('Error no programa! Tente novamente.')
        