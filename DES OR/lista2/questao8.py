'''Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra "A".
OBS: Fazer crítica na entrada do caractere para aceitar somente letras.
'''
def receber_caracteres():
  print("\nDigite os caracteres da lista. DIgite * para finalizar")
  while True:
    letra= input("Digite uma letra quaquer: ").upper()
    while (letra< "A" or letra >"Z" or len(letra) > 1) and (letra != "*"):
      print("\nCaractere digitado não é letra: %s" % letra)
      letra = input("Digite novamente uma letra qualquer: ").upper()

    if letra == "*":
      break

    else:
      l.append(letra)

def quant_letra():
  cont_a = 0
  for i in range(len(l)):
    if l[i] == "A":
      cont_a += 1
  return cont_a

l= []
receber_caracteres()
print("Caracteres digitados: ", l)
print("Quantidade de letras 'A' digitadas: %d"% quant_letra())
print("Quantidade de letras 'A' digitadas: %d"% l.count("A"))
