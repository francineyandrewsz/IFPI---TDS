'''6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.'''
def perfeito(n):
    if type(n) != int or n <= 0:
        return Exception
    soma=0
    for val in range(1,n):
        if n % val == 0:
            soma += val

    if soma==n:
        return True
    else:
        return False

assert perfeito(-1) == Exception
assert perfeito(3.6) == Exception
assert perfeito(345678) == Exception
assert perfeito(234) == Exception
print('Todos os testes OK!')
