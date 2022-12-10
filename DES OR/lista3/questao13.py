'''13. Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro.'''

def jogo(hrsInicio, hrsTermino):
    if hrsInicio != int or hrsTermino != int:
        return Exception
    if not isinstance(hrsInicio, list) or not isinstance(hrsTermino, list):
        return False
    horas = hrsTermino[0] - hrsInicio[0]
    minutos = hrsTermino[1] - hrsInicio[1]
    if minutos < 0:
        minutos = 60 - abs(minutos)
        horas -= 1
    return [horas, minutos]

assert jogo([13, 30], [20, 10]) == [6, 40]
print('Todos os testes OK!')
