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
def receber_quantidade_elementos():
   global max_lista
   while True:
      try:
         quantidade = int(input("\nDigite a quantidade de elementos da lista: "))
         while quantidade <= 0:
            quantidade = int(input("\nQuantidade deve ser maior que 0: "))
         max_lista = quantidade
         break
      except:
         print("\nQuantidade inválida. Digite novamente!")

def gravar_nome():
   if len(nomes) < max_lista:
      nome = input("\nDigite o nome da pessoa: ")
      nomes.append(nome)
      print("\nInclusão com sucesso!")
   else:
      print("\nA lista já está cheia!!")

def pesquisar_nome():
   if len(nomes) != 0:
      nome = input("\nDigite o nome a pesquisar: ")
      if nomes.count(nome) > 0: 
         print("\nO nome está na lista na posição %d." % nomes.index(nome))
      else:
         print("\nO nome não está na lista!")
   else:
      print("\nA lista está vazia!!")

def listar_nomes():
   if len(nomes) != 0:
      print(nomes)
   else:
      print("\nA lista está vazia!!")
def excluir_nome():
   if len(nomes) > 0:
      nome = input("\nDigite o nome a excluir: ")
      if nomes.count(nome) > 0:
         del nomes[nomes.index(nome)]
         print("\nO nome %s foi excluido com sucesso." % (nome))
      else:
         print("\nO nome não está na lista!")
   else:
      print("\nA lista está vazia!!")
def alterar_nome():
   if len(nomes) > 0:
      nome = input("\nDigite o nome a alterar: ")
      if nomes.count(nome) > 0:
         print("\nNome anterior: %s." % (nome))
         novo_nome = input("\nNome atual: ")
         nomes[nomes.index(nome)] = novo_nome
         print("\nAlteração realizada com sucesso")
      else:
         print("\nO nome não está na lista!")
   else:
      print("\nA lista está vazia!!")

def menu():
   while True:
      print("\n=========== MENU ============")
      print(" 1)Cadastrar nome")
      print(" 2)Pesquisar nome")
      print(" 3)Listar todos os nomes")
      print(" 4)Excluir nome")
      print(" 5)Alterar nome")
      print(" 0)Sair do programa")
      print("-----------------------------")
      try:
         opc = int(input("\nDigite sua opção: "))
         if opc == 0:
            break
         elif opc == 1:
            gravar_nome()
         elif opc == 2:
            pesquisar_nome()
         elif opc == 3:
            listar_nomes()
         elif opc == 4:
            excluir_nome()
         elif opc == 5:
            alterar_nome()
      except:
         print("Opção inválida. Digite novamente!")
max_lista = 0
nomes = []
receber_quantidade_elementos()
menu()
