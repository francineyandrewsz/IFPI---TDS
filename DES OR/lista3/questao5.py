'''5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.'''
def idade(valor, ano, mes, dias):
  ano = valor // 365
  valor = valor - ano * 365

  mes = valor // 30
  valor = valor - mes * 30

  dias = valor

  return Exception

assert idade(23) == Exception


  