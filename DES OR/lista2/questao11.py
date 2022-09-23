'''Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
==== =MENU========
1)Cadastar nome
2)Pesquisar nome
3)Listar todos os nome
0) Sair do programa
'''
lista = []
def cadastrar_nome():
    q = int(input('Digite quantos nomes deseja cadastrar: '))
    for c in range(q):
        lista.append(str(input(f'Nome da {c}ª pessoa: ')).strip().upper())
        

def pesquisar_nome():
    p = str(input('Digite um nome que procura: ')).strip().upper()
    for i in lista:
        if (i == p):
            print(f'O nome {p} está na lista')
        else:
            print(f'O nome {p} não está na lista')

def excluir_nome():
    delete = str(input('Informe o nome que deseja remover da lista: ')).strip().upper()
    for i in lista:
        if (i == delete):
            lista.remove(delete)
            print('Nome excluído')
        else:
            print('Nome não está na lista')
while True:
    try:
        menu = print('''====== MENU ======
        [1] Cadastrar nome
        [2] Pesquisar nome
        [3] Listar todos os nome
        [4] Excluir nome
        [0] Sair do programa''')
        opção = int(input('Digite sua opção: ')) 
        if opção == 1:
            cadastrar_nome()
        elif opção == 2:
            pesquisar_nome()
        elif opção == 3:
            print(f'Os nome da lista = {lista}')
        elif opção == 4:
            excluir_nome()
        elif opção == 0:
            break
    except:
        print('Operação inválida! Tente novamente.')


