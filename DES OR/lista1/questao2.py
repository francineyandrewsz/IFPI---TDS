def area(r):
    return 3.1415 * r ** 2

def perimetro(r):
    return 3.1415 * 2 * r

while True:
    try:
        num = int(input('Digite o raio do círculo: '))
        print(f'A área do círculo é {area(num):.2f}')
        print(f'O perémtro do círculo é {perimetro(num):.2f}')
        break
    except:
        print('Error no programa! Digite um valor válido.')
