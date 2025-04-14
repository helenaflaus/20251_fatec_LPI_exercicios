# Gerenciador de Senhas:
# Uma senha deve atender aos critérios mínimos:
# a) Pelo menos 12 caracteres;
# b) Pelo menos dois números;
# c) Pelo menos duas letras maiúsculas e duas minúsculas
# d) Pelo menos dois caracteres especiais.
# Utilize o código ASCII para validar se há caracteres especiais na senha.

# RESPOSTA: 

# atentar para letras com acentos, ç etc ... são caracteres especiais
# ord() transforma o caractere no valor ASCII correspondente
# char() transforma um número no caractere ASCII correspondente

pedir_senha = 'Insira senha com no mínimo 12 caracteres, 2 números, 2 letras maiusculas, 2 minusculas e 2 caracteres especiais: ' # deixar em uma mensagem para o caso de querer mudar mensagem
invalida = 'Senha inválida' # deixar em uma mensagem para o caso de querer mudar mensagem
strSenha = str(input(pedir_senha)) # apenas para encurtar

# contadores dos critérios mínimos
acentuadas = "áàâãéêíóõôúÁÀÂÃÉÊÍÓÕÔÚçÇ" # não constam na ASCII e são caracteres especiais
intN = 0
intLet_mai = 0
intLet_min = 0
intCarac_esp = 0

#checar se possui espaços vazios
for i in strSenha:
   if ord(i) == 32:
      print(invalida)
      strSenha = str(input(pedir_senha))

#checar se possui pelo menos 12 caracteres
if len(strSenha) < 12:
  print(invalida)
  strSenha = str(input(pedir_senha))

else:
  
  # contando numeros
  for i in strSenha:
    if ord(i) >= 48 and ord(i) <= 57: # contando numeros
        intN += 1
    elif ord(i) >= 65 and ord(i) <= 90: # contando letras maiusculas
        intLet_mai += 1
    elif ord(i) >= 97 and ord(i) <= 122: # contando letras minusculas
        intLet_min += 1
    elif i in list(acentuadas): # contando caracteres especiais lista
       intCarac_esp += 1
       # 33-47, 58-64, 91-96, 123-126
    elif (ord(i) >= 33 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126): # contando caracteres especiais ASCII
       intCarac_esp += 1
     
  if intN < 2 and intLet_min < 2 and intLet_mai and intCarac_esp < 2: # verificando criterios mínimos
    print(invalida)
    strSenha = str(input(pedir_senha))
    
print(f'numeros: {intN}, maiusculas: {intLet_mai}, minusculas: {intLet_min}, caracteres: {intCarac_esp}') #apenas para checar
print('Senha válida')

# no começo estava pensando em fazer checagens por criterio e retorno por critério, mas a senha só sera válida se atender todos os critérios
# sendo assim, achei melhor deixar a chegar para o final e fazendo um unico retorno