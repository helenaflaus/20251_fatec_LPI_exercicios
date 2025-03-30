# Etapa 1: Entrada de dados
#criando listas com as notas no início do dia
int100 = 10 * [100]
int50 = 20 * [50]
int20 = 50 * [20]
int10 = 100 * [10]
int5 = 200 * [5]
intCaixa = [int100, int50, int20, int10, int5]
#print(intCaixa)
intSaque = int(input('Valor a ser sacado: '))

intTotal_caixa = sum(int100 + int50 + int20 + int10 + int5)

# Etapa 2: Processamento de dados

#1 verificar se o valor pode ser sacado
if intSaque > intTotal_caixa:
  print('Valor indisponível para saque')

# 100
elif intSaque <= intTotal_caixa: #verificando se valor saque é menor que o total em caixa
  if intSaque // 100 > 0: #descobrir se temos as notas de 10
    notas100 = intSaque // 100 #quantidade de notas a serem sacadas
    if notas100 < 10:
      int100 = (10 - notas100) * [100] #removendo as notas do caixa
      print(f'Vai receber {notas100} notas de 100.') #mostra quantas vai receber
      intSaque = intSaque - sum(int100)
      intTotal_caixa = intTotal_caixa - sum(int100)
    else:
      intSaque = intSaque - sum(int100)
      intTotal_caixa = intTotal_caixa - sum(int100)
      int100 = []
      print('Vai receber 10 notas de 100.') #mostra quantas vai receber200