def par_impar(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False

while True:
    try:
        num = int(input('Digite um número: '))
        if (par_impar(num)):
            print(f'{num} é verdadeiro')
        else:
            print(f'{num} é falso')
        break
    except:
        print('Digite um valor válido!')

