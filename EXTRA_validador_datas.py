# versão 1 python

intData = 28022024
intDia = intData // 1000000
intMes = (intData % 1000000) // 10000
intAno = intData % 10000

if intMes < 10:
    print(f'{intDia}/0{intMes}/{intAno}')
else:
    print(f'{intDia}/{intMes}/{intAno}')
print('Vejamos se ela é válida...')

if intAno < 1:
   print('Data inválida!!')
elif intMes < 1 or intMes > 12:
    print('Data inválida!!')
elif intDia < 1 or intDia > 31:
    print('Data inválida!!')
elif intMes in {4, 6, 9, 11} and intDia > 30:
    print('Data inválida!!')
elif intMes == 2:
    if (intAno % 4 == 0 and intAno % 100 != 0) or (intAno % 400 == 0):
        if intDia > 29:
            print('Data inválida!!')
        else:
            print('Data válida!!')
    else:
        if intDia > 28:
            print('Data inválida!!')
        else:
            print('Data válida!!')
else:
    print('Data válida!!')


# versão 2 python

intData = 29022024
intDia = intData // 1000000
intMes = (intData % 1000000) // 10000
intAno = intData % 10000

def validador_data(dia, mes, ano):
    if ano < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in {4, 6, 9, 11} and dia > 30:
        return False
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    
    return True 

print(f'{intDia}/{intMes:02}/{intAno}')
print('Vejamos se ela é válida...')

if validador_data(intDia, intMes, intAno):
    print('Data válida!!')
else:
    print('Data inválida!!')


# versão 3 python

intData = 29022024
intDia = intData // 1000000
intMes = (intData % 1000000) // 10000
intAno = intData % 10000

def validador_data(dia, mes, ano):
    if ano < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
        return False
    if mes in {4, 6, 9, 11} and dia > 30:
        return False
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    
    return True 

print(f'{intDia}/{intMes:02}/{intAno}')
print('Vejamos se ela é válida...')

if validador_data(intDia, intMes, intAno):
    print('Data válida!!')
else:
    print('Data inválida!!')
