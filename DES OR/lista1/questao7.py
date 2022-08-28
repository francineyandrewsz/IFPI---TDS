'''Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
número, também do tipo inteiro.'''

def cal_fat(num):
    n_fat = 1
    for i in range(num, 1, -1):
        n_fat *= i
    return n_fat
while True:
    try:
        n = int(input('Digite um número inteiro: '))
        while n < 0:
            n = int(input('Número inválido. Por favor, Digite um número inteiro: '))
        print(f'O fatorial de {n} é {cal_fat(n)}')
        break
    except:
        print('Opção inválida! Digite novamente.')
    