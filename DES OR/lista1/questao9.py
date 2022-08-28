'''Escreva uma função que recebe 2 números inteiros n1 e n2 
como entrada e retorna a soma de todos os números inteiros 
contidos no intervalo [n1,n2]. Use esta função em um programa 
que lê n1 e n2 do usuário e imprime a soma.'''

def soma(n1, n2):
    s = 0
    if n2 < 0:
        n2 -= 1
    else:
        n2 += 1
    for n in range(n1, n2):
        s += n
    return s

while True:
    try:
        valor1 = int(input('Digite um número: '))
        valor2 = int(input('Digite outro número: '))
        print(f'A soma dos números em um intervalo entre {valor1} e {valor2} é igual a {soma(valor1, valor2)}')
        break
    except:
        print('Opção inválida! Digite novamente.')
