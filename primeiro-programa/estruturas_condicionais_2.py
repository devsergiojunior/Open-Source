saldo = 2000
cheque_especial = 450
opcao = int(input("Informa o tipo de conta bancaria: \n[1] - Conta Corrente \n[2] - Conta Universitaria \nTipo de Conta: "))
"""
conta_normal = False
conta_universitaria = True
"""
saque = float(input("Informa o valor para saque: R$ "))

if opcao == 1:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif opcao == 2:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente!")
