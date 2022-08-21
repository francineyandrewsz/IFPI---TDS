'''Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.

S = 1 + 1/1! + 1/2! + 1/3! + 1 /N!
'''
def valor_s(s):
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s
while True:
    try:
        n = int(input('Digite um número: '))
        while n <= 0:
            n = int(input('Operação inválida! Por favor, digite um número: '))
        print(f'O resultado é {valor_s(n):.2f}')
        break
    except:
        print(f'Error no programa! Tente novamente.')
    