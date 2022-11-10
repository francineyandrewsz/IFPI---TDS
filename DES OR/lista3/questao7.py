'''7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo:
Idade Categoria
5 a 7 anos Infantil A
8 a 10 anos Infantil B
11-13 anos Juvenil A
14-17 anos Juvenil B
Maiores de 18 anos
(inclusive)'''
def nadador(idade):
    idade = 0
    if type(idade) != int:
        return Exception
    if 5 <= idade >= 7:
        return print('Infantil A')
    elif 8 <= idade >= 10:
        return print('Infantil B')
    elif 11 <= idade >= 13:
        return print('Juvenil A')
    elif 14 <= idade >= 17:
        return print('Juvenil B')
    elif idade >= 18:
        return print('Maiores de 18 anos')
    else:
        return Exception

assert nadador(15) == Exception
assert nadador(13) == Exception
print('Todos os testes OK! PARABÉNS!')
