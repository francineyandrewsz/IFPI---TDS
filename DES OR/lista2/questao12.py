"""Lista2_q12) Deseja-se publicar o número de acertos de cada aluno em uma prova em
forma de testes. A prova consta de 30 questões objetivas, cada uma com cinco alternativas
identificadas por A, B, C, D e E. Para isso são dados: 
1. cartão gabarito; 
2. número de alunos da turma; 
3. cartão de respostas para cada aluno, contendo o seu número e suas respostas."""
quant_questoes = 3
gabarito = []
respostas = []
def receber_gabarito():
    print("\n******* Digite o gabarito oficial da prova *******")
    for i in range(quant_questoes):
        while True:
                resposta = input("\nQuestão %d: " % (i + 1)).upper()
                if resposta in ("A","B","C","D","E"):
                    gabarito.append(resposta)
                    break
                else:
                    print("Resposta inválida. Digite apenas A,B,C,D,E.")
    print("Gabarito oficial: ", gabarito)
       
def receber_respostas_alunos():
    n_alunos = int(input("\nDigite o número de alunos da turma: "))
    for i in range(n_alunos):
        numero_do_aluno = int(input("\nDigite o número do(a) %dº aluno(a): " % (i + 1)))
        acertos = 0
        respostas = list(range(quant_questoes))
        for j in range(quant_questoes): # receber as respostas do aluno i + 1
            while True:
                resposta = input("\nDigite a resposta da questão %d: " % (j + 1)).upper()
                if resposta in ("A","B","C","D","E"):
                    respostas[j] = resposta
                    break
                else:
                    print("Resposta inválida. Digite apenas A,B,C,D,E.")
            if respostas[j] == gabarito[j]:
                acertos += 1
        print("\n",gabarito)
        print("\n",respostas)
        print("O aluno de número %d teve %d acerto(s)." % (numero_do_aluno, acertos))

receber_gabarito()
receber_respostas_alunos()