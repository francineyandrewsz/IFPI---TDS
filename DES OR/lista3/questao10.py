'''10. Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:
   Nota / Conceito
de 0,0  a  4,9 D
de 5,0  a  6,9 C
de 7,0  a  8,9 B
de 9,0  a  10,0A
'''
def aluno(média):
    if 0 <= média <= 4.9:
        return 'Nota D'
    elif 5 <= média <= 6.9:
        return 'Nota C'
    elif 7 <= média <= 8.9:
        return 'Nota B'
    elif 9 <= média <= 10.0:
        return 'Nota A'

assert aluno(3) == 'Nota D'
assert aluno(7) == 'Nota B'
assert aluno(9.4) == 'Nota A'
print('Todos os testes OK!')
    