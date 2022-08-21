def caractere():
    c = input('Deseja continuar [S - sim ou N - não]? ').upper()
    # while c != 'S' and c != 'N':
    while c not in ['S', 'N']:
        c = input('\nCaractere inválido. Digite novamente: ').upper()
    return c
while True:
    try:
        num = int(input('\nDigite um número: '))
        print(f'O cubo do número {num} é {num**3:.2f}')
        if caractere() == 'N':
            break
    except:
        print('Número inválido, digite novamente!')
