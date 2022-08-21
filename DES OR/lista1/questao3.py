'''Escreva um programa para ler uma temperatura em graus Fahrenheit.
Faça uma função chamada celsius para calcular e retornar o valor
correspondente em graus Celsius.
        Fórmula: C = ((F-32)/9)*5
'''
def converter(f):
   return ((f - 32) / 9) * 5

while True:
    try:
        fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
        print(f'A área da temperatura em graus Celsius é {converter(fahrenheit)}ºC')
        break
    except:
        print('Temperatura inválida! Digite novamente.')
        