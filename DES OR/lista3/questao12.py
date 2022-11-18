'''12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente.'''

def crescente(n1,n2):
    if type(n1) != int or type(n2) != int:
        return Exception

    lista = []
    if n1> n2:
        lista.append(n1)
        lista.append(n2)
        return lista
    elif n2 > n1:
        lista.append(n2)
        lista.append(n1)
        return lista
    elif n2 == n1:
        lista.append(n2)
        return lista



assert crescente(268,172) == [268,172]
assert crescente(26111,17) ==[26111,17]
assert crescente(2,12) == [12,2]
assert crescente(344,344) == [344]
assert crescente('268',172) == Exception
print('Todos os testes OK!')