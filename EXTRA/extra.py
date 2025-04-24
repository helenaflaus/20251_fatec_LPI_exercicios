# Escrever um programa para uma máquina de preenchimento automático de cheques, com valores de Rs 1,00 a Rs 100.000,00 (sem centavos)

int_valor = int(input('Informe um valor: '))

str_unidades = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'}
str_dezenas_ate19 = {10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'catorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 19: 'dezoito'}
str_dezenas = {20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa'}
str_centenas = {100: 'cem', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos', 500: 'quinhentos', 600: 'seiscentos', 700: 'setecentos', 800: 'oitocentos', 900: 'novecentos'}
str_mil = {1000: 'mil'}

# construindo o numero 98.754 - noventa e oito mil setecentos e cinquenta e quatro
# 90 + e + 8 + 1000 + 700 + e + 50 + e + 4
# 98.754 // 1.000 = 98 -> se maior que 10 ... 90, 80, 70 ... 'dezMilhares' + 'e' ou '1000'
# (98.754 // 1.000) % 10 = 8 -> se maior que 1 ... 9, 8, 7, 6 ... 'milhares' + '1000'
# (98.754 % 1.000) // 100 = 7 -> se maior que 1 ... 900, 800, 700 ... 'centenas' + 'e'
# 98.754 % 100 = 54 -> se maior que 20 ... 20, 30, 40 'dezenas' + 'e'
# 98.754 % 100 = 54 -> se menor que 20 e maior que 10 ... 11, 12, 13 'dezenas_ate19'
# 98.754 % 100 = 54 -> se menor que 10 ... 1, 2, 3 ... 'unidades'
# 98.754 % 10 = 54 -> se menor que 10 ... 1, 2, 3 ... 'unidades'

def dezmilhares(int_valor):
    
    dezmilhares = int_valor // 1000

    if dezmilhares >= 90:
        if dezmilhares == 90:
            return f'{str_dezenas[90]} mil'
        else:
            return f'{str_dezenas[90]} e'
    elif dezmilhares >= 80:
        if dezmilhares == 80:
            return f'{str_dezenas[80]} mil'
        else:
            return f'{str_dezenas[80]} e'
    elif dezmilhares >= 70:
        if dezmilhares == 70:
            return f'{str_dezenas[70]} mil'
        else:
            return f'{str_dezenas[70]} e'
    elif dezmilhares >= 60:
        if dezmilhares == 60:
            return f'{str_dezenas[60]} mil'
        else:
            return f'{str_dezenas[60]} e'
    elif dezmilhares >= 50:
        if dezmilhares == 50:
            return f'{str_dezenas[50]} mil'
        else:
            return f'{str_dezenas[50]} e'
    elif dezmilhares >= 40:
        if dezmilhares == 40:
            return f'{str_dezenas[40]} mil'
        else:
            return f'{str_dezenas[40]} e'
    elif dezmilhares >= 30:
        if dezmilhares == 30:
            return f'{str_dezenas[30]} mil'
        else:
            return f'{str_dezenas[30]} e'
    elif dezmilhares >= 20:
        if dezmilhares == 20:
            return f'{str_dezenas[20]} mil'
        else:
            return f'{str_dezenas[20]} e'
    elif dezmilhares >= 10:
        if dezmilhares == 10:
            return f'{str_dezenas_ate19[10]} mil'
        elif dezmilhares == 11:
            return f'{str_dezenas_ate19[11]} mil'
        elif dezmilhares == 12:
            return f'{str_dezenas_ate19[12]} mil'
        elif dezmilhares == 13:
            return f'{str_dezenas_ate19[13]} mil'
        elif dezmilhares == 14:
            return f'{str_dezenas_ate19[14]} mil'
        elif dezmilhares == 15:
            return f'{str_dezenas_ate19[15]} mil'
        elif dezmilhares == 16:
            return f'{str_dezenas_ate19[16]} mil'
        elif dezmilhares == 17:
            return f'{str_dezenas_ate19[17]} mil'
        elif dezmilhares == 18:
            return f'{str_dezenas_ate19[18]} mil'
        elif dezmilhares == 19:
            return f'{str_dezenas_ate19[19]} mil'
    return ''

def uniddezenasmil(int_valor):
    
    int_unidmilhares = (int_valor // 1000) % 10

    if int_unidmilhares == 9:
        return f'{str_unidades[9]} mil'
    elif int_unidmilhares == 8:
        return f'{str_unidades[8]} mil'
    elif int_unidmilhares == 7:
        return f'{str_unidades[7]} mil'
    elif int_unidmilhares == 6:
        return f'{str_unidades[6]} mil'
    elif int_unidmilhares == 5:
        return f'{str_unidades[5]} mil'
    elif int_unidmilhares == 4:
        return f'{str_unidades[4]} mil'
    elif int_unidmilhares == 3:
        return f'{str_unidades[3]} mil'
    elif int_unidmilhares == 2:
        return f'{str_unidades[2]} mil'
    elif int_unidmilhares == 1:
        return f'{str_unidades[1]} mil'
    return ''

# preciso refatorar essa operação, pois esta colocando mil nos valores de unidade também
def milhares(int_valor):
    
    if int_valor >= 1000:
        int_milhares = int_valor % 10000

        if int_milhares == 9:
            return f'{str_unidades[9]} mil'
        elif int_milhares == 8:
            return f'{str_unidades[8]} mil'
        elif int_milhares == 7:
            return f'{str_unidades[7]} mil'
        elif int_milhares == 6:
            return f'{str_unidades[6]} mil'
        elif int_milhares == 5:
            return f'{str_unidades[5]} mil'
        elif int_milhares == 4:
            return f'{str_unidades[4]} mil'
        elif int_milhares == 3:
            return f'{str_unidades[3]} mil'
        elif int_milhares == 2:
            return f'{str_unidades[2]} mil'
        elif int_milhares == 1:
            return f'{str_unidades[1]} mil'
    return ''

def centenas(int_valor):
    
    int_centenas = (int_valor % 1000) // 100
    
    if int_centenas == 9:
        return f'{str_centenas[900]} e'
    elif int_centenas == 8:
        return f'{str_centenas[800]} e'
    elif int_centenas == 7:
        return f'{str_centenas[700]} e'
    elif int_centenas == 6:
        return f'{str_centenas[600]} e'
    elif int_centenas == 5:
        return f'{str_centenas[500]} e'
    elif int_centenas == 4:
        return f'{str_centenas[400]} e'
    elif int_centenas == 3:
        return f'{str_centenas[300]} e'
    elif int_centenas == 2:
        return f'{str_centenas[200]} e'
    elif int_centenas == 1:
        return f'{str_centenas[100]} e'
    return ''

def dezenas(int_valor):
    
    int_dezenas = int_valor % 100

    if int_dezenas >= 90:
        if int_dezenas == 90:
            return f'{str_dezenas[90]}'
        else:
            return f'{str_dezenas[90]} e'
    elif int_dezenas >= 80:
        if int_dezenas == 80:
            return f'{str_dezenas[80]}'
        else:
            return f'{str_dezenas[80]} e'
    elif int_dezenas >= 70:
        if int_dezenas == 70:
            return f'{str_dezenas[70]}'
        else:
            return f'{str_dezenas[70]} e'
    elif int_dezenas >= 60:
        if int_dezenas == 60:
            return f'{str_dezenas[60]}'
        else:
            return f'{str_dezenas[60]} e'
    elif int_dezenas >= 50:
        if int_dezenas == 50:
            return f'{str_dezenas[50]}'
        else:
            return f'{str_dezenas[50]} e'
    elif int_dezenas >= 40:
        if int_dezenas == 40:
            return f'{str_dezenas[40]}'
        else:
            return f'{str_dezenas[40]} e'
    elif int_dezenas >= 30:
        if int_dezenas == 30:
            return f'{str_dezenas[30]}'
        else:
            return f'{str_dezenas[30]} e'
    elif int_dezenas >= 20:
        if int_dezenas == 20:
            return f'{str_dezenas[20]}'
        else:
            return f'{str_dezenas[20]} e'
    elif int_dezenas == 19:
        return f'{str_dezenas_ate19[19]}'
    elif int_dezenas == 18:
        return f'{str_dezenas_ate19[18]}'
    elif int_dezenas == 17:
        return f'{str_dezenas_ate19[17]}'
    elif int_dezenas == 16:
        return f'{str_dezenas_ate19[16]}'
    elif int_dezenas == 15:
        return f'{str_dezenas_ate19[15]}'
    elif int_dezenas == 14:
        return f'{str_dezenas_ate19[14]}'
    elif int_dezenas == 13:
        return f'{str_dezenas_ate19[13]}'
    elif int_dezenas == 12:
        return f'{str_dezenas_ate19[12]}'
    elif int_dezenas == 11:
        return f'{str_dezenas_ate19[11]}'
    elif int_dezenas == 10:
        return f'{str_dezenas_ate19[10]}'
    return ''

def unidades(int_valor):

    int_unidades = int_valor % 10

    if int_unidades == 9:
        return f'{str_unidades[9]}'
    elif int_unidades == 8:
        return f'{str_unidades[8]}'
    elif int_unidades == 7:
        return f'{str_unidades[7]}'
    elif int_unidades == 6:
        return f'{str_unidades[6]}'
    elif int_unidades == 5:
        return f'{str_unidades[5]}'
    elif int_unidades == 4:
        return f'{str_unidades[4]}'
    elif int_unidades == 3:
        return f'{str_unidades[3]}'
    elif int_unidades == 2:
        return f'{str_unidades[2]}'
    elif int_unidades == 1:
        return f'{str_unidades[1]}'
    return '' 

if int_valor == 100000:
    print('cem mil reais')
elif int_valor == 1:
    print('um real')
else:
    print(dezmilhares(int_valor),uniddezenasmil(int_valor),milhares(int_valor),centenas(int_valor),dezenas(int_valor),unidades(int_valor), 'reais')