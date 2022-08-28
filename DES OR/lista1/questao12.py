'''Escreva uma função que recebe, por parâmetro, um valor inteiro e 
positivo e retorna o somatório desse valor.'''

def somatorio(n):
    soma = 0
    for i in range(0, n+1):
        soma += i
    return soma

while True:
    try:
        num = int(input('Digite um valor inteiro positivo: '))
        print(f'O somatório do valor {num} é {somatorio(num)}')
        break
    except:
        print('Error no programa! Tente novamente.')
