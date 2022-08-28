'''Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.'''
def qual_poligono(n_lados, m_lado):
    if n_lados == 3:
        p = n_lados * m_lado
        print(f'TRIÂNGULO. Seu perímetro é {p:.2f}')
    elif n_lados == 4:
        area = m_lado * m_lado
        print(f'QUADRADO. Sua área é de {area:.2f}')
    else:
        print('PENTÁGONO')    
   
while True:
    try:
        opção = int(input('''Digite:
                            [3] - TRIÂNGULO
                            [4] - QUADRADO
                            [5] - PENTÁGONO
                            Sua opção: '''))
        while opção not in [3, 4, 5]:
            opção = int(input('''Opção inválida! Digite novamente:
                                [3] - TRIÂNGULO
                                [4] - QUADRADO
                                [5] - PENTÁGONO
                                Sua opção: '''))
        medida = float(input('Digite a medida do lado: '))
        while medida <= 0:
            medida = float(input('Opção inválida! Digite novamente a medida do lado: '))
        qual_poligono(opção, medida)
        break
    except:
        print('Error no programa! Digite um valor válido') 
                                   
    
        
    