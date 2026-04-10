#Inicio

print(" Pesquisa de satistação TudoWeb ")
total_entrevistados = int(input(" Digite o número total de entrevistados desejado: "))
Quantidade_excelente = 0
Quantidade_bom = 0
quantidade_ruim = 0

#Laço de repetição

for i in range(total_entrevistados):
    print(f" Entrevistados {i + 1} de {total_entrevistados}")
    nome = input(" Digite seu nome: ")
    idade = input(" Digite sua idade: ")
    print("Opiniões sobre o atendimento")
    print("1: Excelente")
    print("2: Bom")
    print("3: Ruim")

    opinião = int(input(" Digite o número correspondente a sua opinião (1, 2 ou 3): "))
    if opinião == '1':
        Quantidade_excelente += 1
    elif opinião == '2':
        Quantidade_bom += 1
    elif opinião == '3':
        quantidade_ruim += 1

    total_respostas = i + 1
    print(f" Quantidade de respostas 'excelente': {Quantidade_excelente}")
    print(f" Quantidade de respostas 'Bom': {Quantidade_bom}")
    print(f" Quantidade de respostas 'Ruim': {quantidade_ruim}")