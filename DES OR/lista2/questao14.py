'''Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.'''
lista_c = []
lista_c_mod = []
def mod_lista():
    for c in range(1, 11):
        lista_c.append(int(input(f'Digite {c}ª número: ')))
    
    print(f'Lista C = {lista_c}')
    for num in lista_c:
        if num < 0:
            lista_c_mod.append(0)
        else:
            lista_c_mod.append(num)
                
    print(f'Lista C modificada = {lista_c_mod}')
    
mod_lista()
