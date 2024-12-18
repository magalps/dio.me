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
valor_saque = 0
valor_deposito = 0
LIMITE_SAQUES = 3
cont = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito += float(input("Quanto deseja depositar: R$"))
        if valor_deposito < 0:
            print("Você não pode depositar um valor negativo")
        else:
            print("Depósito realizado com sucesso!")
            saldo += valor_deposito
            extrato += f"\n Depósito +{valor_deposito}\n"
            valor_deposito = 0

    elif opcao == "s":
        print("Saque")
        if cont >= LIMITE_SAQUES:
            print ("Você atingiu o limite de saques")
        else:
            valor_saque =  float(input("Quanto deseja sacar: R$"))
            if valor_saque > saldo:
                print("Saldo insuficiente")
            else:
                saldo -=valor_saque #atualiza o saldo
                print("Saque realizado com sucesso!")
                extrato += f"\n Saque -{valor_saque}\n"
                valor_saque = 0
                cont += 1

    elif opcao == "e":
        print("Extrato")
        print(f"{extrato}")
        print(f"Saldo: R${saldo}")

    elif opcao == "q":
        print("Saindo do sistema...")
        break
    else:
        print("Operação inválida, por favor, selecionar novamente a operação desejada.")