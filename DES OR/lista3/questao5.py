'''5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.'''
def tempo_em_dias(ano, mes, dias):
  if type(ano) != int or type(mes) != int or type(dias) != int:
    return Exception
  
  if (ano not in range(0, 121)) or (mes not in range(0, 13)) or (dias not in range(0, 31)):
    return Exception
  
  return ano * 365 + mes * 30 + dias 
 
assert tempo_em_dias(10, 1, 2) == 3682 # testando classe válida
assert tempo_em_dias(0, 1, 2) == 32 # testando classe válida
assert tempo_em_dias(0, 1, 1) == 31 #testando classe válida
assert tempo_em_dias(0, 0, 0) == 0 # testando classe válida valores limitrofes
assert tempo_em_dias(120, 12, 30) == 44190 # testando classe válida valores limitrofes
assert tempo_em_dias(1, 1, 31) == Exception # testando classe inválida
assert tempo_em_dias(121, 1, 2) == Exception # testando classe inválida
assert tempo_em_dias(10, 13 ,2) == Exception # testando classe inválida
assert tempo_em_dias(-1, 1, 2) == Exception # testando classe inválida
assert tempo_em_dias('*', 1, 2) == Exception # testando classe inválida
assert tempo_em_dias(10, 5.1, 2) == Exception # testando classe inválida
print('Todos os testes OK!')
