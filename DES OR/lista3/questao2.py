'''2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada.'''
def calc_media(n1, n2, n3, letra):
    if type(n1) == str or type(n2) == str or type(n3) == str:
        return Exception
    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        return Exception
    if letra == 'A':
        media = (n1 + n2 + n3) / 3
    elif letra == 'P':
        media = (n1*5 + n2*3 + n3*2) / 10
    else:
        return Exception
    return media

assert calc_media(3, 4, 5, 'X') == Exception
assert calc_media(3, 4, 5, 'a') == Exception
assert calc_media('A', 4, 5, 'P') == Exception
assert calc_media(3, 4, 5, 6) == Exception
assert calc_media(30, 4, 5, 'A') == Exception
assert calc_media(3, 40, 5, 'A') == Exception
assert calc_media(3, 4, 50, 'A') == Exception
assert calc_media(30, 4, 5, 'P') == Exception
assert calc_media(3, 40, 5, 'P') == Exception
print('Testes Ok!')