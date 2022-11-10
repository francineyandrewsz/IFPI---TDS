'''15. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00.'''
def pesquisa(salários, filhos):
    if len(salários) != 0 or len(filhos) == 0:
        return Exception
    if len(salários) != len(filhos):
        return Exception
    somaSalário = somaFilhos = soma350 = 0
    for i in range(len(salários)):
        if type(salários[1]) != float or salários[i] <= 0:
            return Exception
        if type(filhos[i]) != int or filhos[i] <= 0 or filhos[i] >= 20:
            return Exception
        if salários[i] <= 350:
            soma350 += 1
        somaSalário += salários[i]
        somaFilhos += filhos[i]
    return somaSalário / len(salários), somaFilhos / len(filhos), max(salários)
assert pesquisa([1000.00, 2000.00, 300.00], [2, 3, 1]) == (1100.00, 2, 2000.00, 33.33)
assert pesquisa([-1000.00, 2000.00, 300.00], [2, 3, 1]) == Exception
print('Testes OK!')