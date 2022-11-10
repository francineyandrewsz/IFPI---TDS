'''9. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano.'''
def valor_n(n):
    if type(n) != int:
      return Exception
    if n % 2 == 0:
        return True #O número é Par
    else:
        return False #O número é Ímpar
assert valor_n(4) == True
assert valor_n(3) == False
assert valor_n('a') == Exception
assert valor_n('%') == Exception
print('Todos os testes OK!')
