'''6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.'''
def perfeito(n):
    if type(n) != int or n <= 0:
        return Exception
    soma=0
    for i in range(1,n):
        if n % i == 0:
            soma += i

    if soma == n:
        return True
    else:
        return False

assert perfeito(-1) == Exception
assert perfeito(1.5) == Exception
assert perfeito("A") == Exception
assert perfeito(0) == Exception
assert perfeito(1) == False
assert perfeito(20) == False
assert perfeito(5) == False
assert perfeito(6) == True
assert perfeito(496) == True
print('Todos os testes OK!')
