'''3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.'''
def primo(valor):
  if type(valor) == int and valor > 0:
    for c in range(2, valor+1):
      if valor % c == 0:
        return True
      else:
        return False
  else:
    return Exception

assert primo(3) == False
assert primo(4) == True
assert primo(-2) == Exception
assert primo(0) == Exception
assert primo('a') == Exception
print('Testes ok!')
