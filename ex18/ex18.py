# Simulador de Atendimento em uma Clínica Médica:
# Você está desenvolvendo um sistema para organizar o atendimento de pacientes em uma clínica médica. O programa deve permitir que o usuário adicione pacientes à fila de atendimento (nome e idade). Os pacientes devem ser atendidos em ordem de chegada, mas idosos (idade ≥ 60 anos) têm prioridade. Ao chamar um paciente, o programa deve removê-lo da fila e exibir seu nome. O usuário deve digitar "próximo" para chamar o próximo paciente ou "listar" para ver a fila de espera. Caso a fila esteja vazia, exibir uma mensagem apropriada.

# vou usar opção com inteiros para "recepção"

fila_list = []

def fila_fun(nome, idade):
    if idade < 60:
        fila_list.append(nome)
    else:
        fila_list.insert(0, nome)

print('Inclua o 1o paciente na fila:')
idade1 = int(input('Idade: '))
nome1 = input('Nome: ')
fila_fun(nome1, idade1)

while len(fila_list) > 0:

    recepcao = int(input(' Chamar paciente[1]' \
        ' Incluir paciente[2]' \
        ' Listar fila[3] '))

    if recepcao != 1 and recepcao != 2 and recepcao != 3:
        print('Opção inválida!')

    elif recepcao == 2:
        idade2 = int(input('Idade: '))
        nome2 = input('Nome: ')

        fila_fun(nome2, idade2)

    elif recepcao == 1 and len(fila_list) >= 1:
        atendimento = fila_list.pop(0)
        print(f'Paciente {atendimento} sala 1, o médico te aguarda.')

    elif recepcao == 3:
        print('Fila: ')
        for i in fila_list:
            print(f'{i}')

print('Fila de atendimento vazia.')