'''3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.'''
def primo(valor):
  if type(valor) == int and valor >= 0:
    for c in range(2, valor+1):
      if valor % c == 0:
        return False
      else:
        return True
  else:
    return Exception

assert primo(3) == True
print('Testes ok!')