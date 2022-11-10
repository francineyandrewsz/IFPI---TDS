'''4. Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.'''
def tempo(seg):
  if type(seg) != int or seg <= 0:
    return Exception
  th = seg // 3600
  tm = (seg % 3600) // 60
  ts = (seg % 3600) % 60
  return th, tm, ts

assert tempo(3600) == (1, 0, 0) #testando classe válida
assert tempo(3660) == (1, 1, 0) #testando classe válida
assert tempo(3661) == (1, 1, 1) #testando classe válida
assert tempo(3670) == (1, 1, 10) #testando valores improvável
assert tempo(0) == Exception #testando valores improvável
assert tempo(3600.5) == Exception #testando valores inválidos
assert tempo(-1) == Exception #testando valores improvável
assert tempo('*') == Exception #testando valores inválidos
print('Todos os testes ok!')
