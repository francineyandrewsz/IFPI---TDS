'''Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.'''
lista_W = []
lista_V = []
contador = 0
from random import randint
def verificar():
    for i in range(1, 11):
        lista_W= randint(0, 11)
  
    while True:
        try:
            n = int(input("Digite um valor entre 0 e 10: "))
            while n < 0 or  n > 10:
                n = int(input("O número deve estar entre 0 e 10: "))
   
            for i in range(len(lista_W)):
                if lista_W[i] == n:
                    print(f'Ele aparece na posição {i}')
                    contador += 1
            break
        except:
            print("Digite um valor válido!")
            

    print(f'O número digitado se repete {contador} vezes.')

verificar()
    
    