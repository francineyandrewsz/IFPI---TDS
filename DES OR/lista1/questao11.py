'''Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.'''

def divisores(n):
    qtd = 0
    for c in range(1, n+1):
        if n % c == 0:
            qtd += 1
    return qtd
    
while True:
    try:
        num = int(input('Digite um valor inteiro positivo: '))
        print(f'A quantidade de divisores do número {num} é {divisores(num)}')
        break
    except:
        print('Error no programa! Tente novamente.')
        