'''Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação).'''
def notas_aluno(n1, n2):
    return (n1 + n2) / 2

while True:
    try:
        nota1 = float(input('Primeira nota: '))
        nota2 = float(input('Segunda nota: '))
        if (notas_aluno(nota1, nota2) >= 6):
            print('PARABÉNS! Você foi aprovado!')
        else:
            print('REPROVADO! Você precisa estudar mais.')
        break
    except:
        print('Error no programa! Digite um valor válido.')
print(f'Sua média foi de {notas_aluno(nota1, nota2)}')
