'''8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano.'''
def valor_n(n):
  
    if type(n) != int:
        return Exception
    if n >= 0:
        return True
    elif n < 0:
        return False
    return n

assert valor_n(5) == True
assert valor_n(-1) == False
assert valor_n(0) == True
assert valor_n('a') == Exception
assert valor_n('*') == Exception
print('Todos os testes OK!')