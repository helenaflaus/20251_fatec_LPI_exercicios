# @title Resposta:

#criando listas com as notas no início do dia
int100 = 10 * [100]
int50 = 20 * [50]
int20 = 50 * [20]
int10 = 100 * [10]
int5 = 200 * [5]
intTotal_caixa = sum(int100 + int50 + int20 + int10 + int5)

tentativa = 0

#1 verificar se o valor pode ser sacado
while intTotal_caixa // 5 > 0 or tentativa < 3:
  intSaque = int(input('Valor a ser sacado: '))

  if intSaque % 5 != 0 and intSaque < intTotal_caixa:
    print('Solicite um valor diferente, fornecemos notas de 100, 50, 20, 10 e 5 reais.') #aponta erro em valores solicitados diferentes de multiplo de 5
  elif intSaque > intTotal_caixa and tentativa < 3: #se nao valor suficiente em caixa ele vai rodar 3x a tentativa pedindo novos valores a serem sacados
    tentativa += 1
    print(f'Valor indisponível para saque. Tentativa {tentativa}')

  #2 verificar como o valor vai ser sacado
  else:
    #100
    if intSaque // 100 > 0 and len(int100) > 0: #descobrir se temos as notas
      notas100 = intSaque // 100 #quantidade de notas a serem sacadas
      if notas100 <= 10:
        int100 = (len(int100) - notas100) * [100] #removendo as notas do caixa
        intSaque -= notas100 * 100
        intTotal_caixa -= notas100 * 100
        print(f'Vai receber {notas100} notas de 100.') #mostra quantas vai receber
      else:
        intSaque -= 1000
        intTotal_caixa -= 1000
        int100 = []
        print('Vai receber 10 notas de 100.') #mostra quantas vai receber

    # 50
    if intSaque // 50 > 0 and len(int50) > 0: #descobrir se temos as notas
      notas50 = intSaque // 50 #quantidade de notas a serem sacadas
      if notas50 < 20:
        int50 = (len(int50) - notas50) * [50] #removendo as notas do caixa
        intSaque -= notas50 * 50
        intTotal_caixa -= notas50 * 50
        print(f'Vai receber {notas50} notas de 50.') #mostra quantas vai receber
      else:
        intSaque -= 1000
        intTotal_caixa -= 1000
        int50 = []
        print('Vai receber 20 notas de 50.') #mostra quantas vai receber

    # 20
    if intSaque // 20 > 0 and len(int20) > 0: #descobrir se temos as notas
      notas20 = intSaque // 20 #quantidade de notas a serem sacadas
      if notas20 < 50:
        int20 = (len(int20) - notas20) * [20] #removendo as notas do caixa
        intSaque -= notas20 * 20
        intTotal_caixa -= notas20 * 20
        print(f'Vai receber {notas20} notas de 20.') #mostra quantas vai receber
      else:
        intSaque -= 1000
        intTotal_caixa -= 1000
        int20 = []
        print('Vai receber 50 notas de 20.') #mostra quantas vai receber

    # 10
    if intSaque // 10 > 0 and len(int10) > 0: #descobrir se temos as notas
      notas10 = intSaque // 10 #quantidade de notas a serem sacadas
      if notas10 < 100:
        int10 = (len(int10) - notas10) * [10] #removendo as notas do caixa
        intSaque -= notas10 * 10
        intTotal_caixa -= notas10 * 10
        print(f'Vai receber {notas10} notas de 10.') #mostra quantas vai receber
      else:
        intSaque -= 1000
        intTotal_caixa -= 1000
        int10 = []
        print('Vai receber 100 notas de 10.') #mostra quantas vai receber

    # 5
    if intSaque // 5 > 0 and len(int5) > 0: #descobrir se temos as notas
      notas5 = intSaque // 5 #quantidade de notas a serem sacadas
      if notas5 < 200:
        int5 = (len(int5) - notas5) * [5] #removendo as notas do caixa
        intSaque -= notas5 * 5
        intTotal_caixa -= notas5 * 5
        print(f'Vai receber {notas5} notas de 5.') #mostra quantas vai receber
      else:
        intSaque -= 1000
        intTotal_caixa -= 1000
        int5 = []
        print('Vai receber 200 notas de 5.') #mostra quantas vai receber

  #print(f'O caixa possui {intTotal_caixa}') -> estava usando para testar enquanto construía o código
