'''Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1 = feminino 2 = masculino) de uma pessoa. Depois faça uma função chamada peso ideal
que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal,
utilizando as seguintes fórmulas:
- para homens: (72.7 * h) - 58
- para mulheres: (62.1 * h) - 44.7
Observação: Altura = h (na fórmula acima).
'''
def peso_ideal(s, h):
    if s == 1:
        return (62.1 * h) - 44.7
    elif s == 2:
        return (72.7 * h) - 58

while True:
    try:
        sexo = int(input('Digite o sexo da pessoa: [1 - Feminino 2 - Masculino]: '))
        while sexo != 1 and sexo != 2:
            print('Opção inválida! Digite novamente.')
            sexo = int(input('Digite o sexo da pessoa: [1 - Feminino 2 - Masculino]: '))
            if sexo in [1, 2]:
                break
        altura = float(input('Digite a altura da pessoa: '))
        break
    except:
        print('Error no programa! Tente novamente.')
print(f'O peso ideal é {peso_ideal(sexo, altura)}')
      
   