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

# depois de algumas tentativas achei melhor criar uma função que retorne se válida ou nao, ignorei inputs do usuário para este script

def confere_senha(senha):
    
    acentuadas = "áàâãéêíóõôúÁÀÂÃÉÊÍÓÕÔÚçÇ" # não constam na ASCII e são caracteres especiais
    int_n = 0
    int_let_mai = 0
    int_let_min = 0
    int_carac_esp = 0
    int_vazios = 0

    if len(senha) < 12:
        return print('Senha inválida'), print(f'numeros: {int_n}, maiusculas: {int_let_mai}, minusculas: {int_let_min}, caracteres: {int_carac_esp}')
    else:
        for i in senha:
            if ord(i) == 32: #checar se possui espaços vazios
                int_vazios += 1
            elif ord(i) >= 48 and ord(i) <= 57: # contando numeros
                int_n += 1
            elif ord(i) >= 65 and ord(i) <= 90: # contando letras maiusculas
                int_let_mai += 1
            elif ord(i) >= 97 and ord(i) <= 122: # contando letras minusculas
                int_let_min += 1
            elif i in list(acentuadas): # contando caracteres especiais lista
                int_carac_esp += 1
            # 33-47, 58-64, 91-96, 123-126
            elif (ord(i) >= 33 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126): # contando caracteres especiais ASCII
                int_carac_esp += 1
        if int_n >= 2 and int_let_min >= 2 and int_let_mai >= 2 and int_carac_esp >= 2 and int_vazios == 0:
            return print('Senha válida'), print(f'numeros: {int_n}, maiusculas: {int_let_mai}, minusculas: {int_let_min}, caracteres: {int_carac_esp}')
        else: 
            print('Senha inválida'), print(f'numeros: {int_n}, maiusculas: {int_let_mai}, minusculas: {int_let_min}, caracteres: {int_carac_esp}')
