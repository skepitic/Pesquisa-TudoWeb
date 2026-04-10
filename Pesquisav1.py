#INICIO

#TOTAL DE ENTREVISTADOS

TOTAL_ENTREVISTADOS = int(input(" Número total de entrevistados desejados")) 
QUANTIDADE_EXCELENTE = 0
QUANTIDADE_BOM = 0
QUANTIDADE_RUIM = 0

print(" Pesquisa de Satisfação TudoWeb ")

#ESTRUTURA DE REPETIÇÃO

for i in range(TOTAL_ENTREVISTADOS):  # Confesso que não entendi muito bem como usar a estrutura for
    print(F" Entrevistado {i + 1} de {TOTAL_ENTREVISTADOS}") # Ainda não entendi 100%, mas ficou funcional

#COLETA DE DADOS

    NOME = input("Digite o nome: ")
    IDADE = input(" Digite sua idade: ")

    print("Opiniões sobre o atendimento: ")
    print(" 1: Excelente")
    print(" 2: Bom")
    print(" 3: Ruim")

#Lê a opinião em texto e converte para número

    OPINIAO = int(input(" Digite o número correspondente a opinião ( 1, 2 ou 3):"))

    if OPINIAO == 1:
        QUANTIDADE_EXCELENTE += 1
    elif OPINIAO == 2:
        QUANTIDADE_BOM += 1
    elif OPINIAO == 3:
     QUANTIDADE_RUIM += 1

#RESULTADOS FINAIS

print(" Resultados da pesquisa TudoWeb ")
print(f" Quantidade de respostas 'Excelente': {QUANTIDADE_EXCELENTE}")
print(f" Quantidade de respostas 'Bom': {QUANTIDADE_BOM}")
print(f" Quantida de respostas 'Ruim': {QUANTIDADE_RUIM}")