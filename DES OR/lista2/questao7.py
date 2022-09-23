'''Dada uma lista contendo 10 elementos numéricos,
elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

def pertence_L():
    n = [7, 5, 15, 11, 2, 33, 41, 21, 18, 99]
    while True:
        try:
            núm = int(input('Digite um número: '))
            if núm in n:
                print(f'O número {núm} PERTENCE a lista "n".')
            else:
                print(f'O número {núm} NÃO PERTENCE a lista "n".')
            break
        except:
            print('Operação inválida! Tente novamente...')
pertence_L()
