'''Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um
deles;
b) O programa principal lê 4 séries de 4 números a, b, c e d. Para cada série lida imprime o maior dos quatro números usando a função
Max.'''

def max(n1, n2, n3, n4):
    maior = n1 
    if n2 >= maior:
        maior = n2
    elif n3 >= maior:
        maior = n3
    elif n4 >= maior:
        maior = n4
    return maior

while True:
    try:
        a = int(input('Primeiro número: '))
        b = int(input('Segundo número: '))
        c = int(input('Terceiro número: '))
        d = int(input('Quarto número: '))
        print(f'O maior número entre eles é {max(a, b, c, d)}')
        break
    except:
        print('Error no programa! Digite uma opção válida.')

        