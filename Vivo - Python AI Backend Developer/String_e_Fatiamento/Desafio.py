'''
DESCRIÇÃO
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é 
implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido 
para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de 
aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as 
operações bancárias
'''

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

    elif opcao == "s":
        print("Saque")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        print("Saindo do sistema...")
        break
    else:
        print("Operação inválida, por favor, selecionar novamente a operação desejada.")