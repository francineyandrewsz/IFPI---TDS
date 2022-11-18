'''11. Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7.'''

def peso_ideal(altura,sexo):
    if type(altura) != float or type(sexo) != str:
        return Exception
    if sexo == 'm':
        m = 72.7 * altura - 58
        return round(m,2)
    elif sexo == 'f':
        f = 62.1 * altura - 44.7
        return round(f,2)

assert peso_ideal(1.74,'m') == 68.5
assert peso_ideal(1,'j') == Exception
assert peso_ideal(1.74,'f') == 63.35
print('Todos os testes OK!')
