'''14. Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:

o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.
'''

def triangulo_lados(x,y,z):
    if type(x) != int or type(y)!=int or type(z) != int:
        return Exception

    if x == y == z:
        return 'equilatero'
    elif x != y == z or y != z == x or z != x == y :
        return 'isosceles'
    elif x != y != z:
        return 'escaleno'


assert triangulo_lados(2,2,2) == 'equilatero'
assert triangulo_lados(2,2,3) == 'isosceles'
assert triangulo_lados(2,6,8) == 'escaleno'
assert triangulo_lados('69',6,2) == Exception
print('Todos testes OK!')
    
