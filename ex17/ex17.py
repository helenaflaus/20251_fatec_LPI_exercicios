# ex 5 da lista: simulador de partida de futebol
# simulador básico de partida de futebol
# 2 times cada um começa com zero gols
# o jogo tem 2 tempos de 45 minutos simulados em um loop
# a cada iteração do loop deve haver uma CHANCE aleatória de um time marcar um gol (10%, 15% etc)
# o sistema exibe a cada minuto o tempo do jogo e o placar atual
# no final exibe o placar final e o time vencedor (ou empate)

int_time1 = 0
int_time2 = 0
int_tempos = 0
min = 0

import random # geração de valores aleatórios

while int_tempos != 2: # 2 tempos
    for min in range(45): # 45 "minutos"
        float_probabilidadeT1 = random.random()
        float_probabilidadeT2 = random.random()
        if float_probabilidadeT1 == float_probabilidadeT2:
            int_gol = 0
        elif float_probabilidadeT1 > float_probabilidadeT2:
            int_gol = random.randint(0, 1)
            int_time1 += int_gol
        elif float_probabilidadeT2 > float_probabilidadeT1:
            int_gol = random.randint(0, 1)
            int_time2 += int_gol
        min += 1
        print(f'PLACAR minuto[{min}] time 1 [{int_time1}] / time 2 [{int_time2}]')
    int_tempos += 1 # 2 tempos

print(f'PLACAR FINAL: time 1 [{int_time1}] / time 2 [{int_time2}]')
if int_time1 == int_time2:
    print('empate...')
elif int_time1 > int_time2:
    print('Time 1 vencedor!!')
else:
    print('Time 2 vencedor!!')