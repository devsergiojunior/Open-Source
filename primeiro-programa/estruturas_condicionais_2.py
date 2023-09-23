saldo = 2000
cheque_especial = 450
opcao = int(input("Informa o tipo de conta bancaria: \n[1] - Conta Corrente \n[2] - Conta Universitaria \nTipo de Conta: "))

if opcao not in (1,2):
    print("Tipo de conta invalida, sistema sera encerrado.")
"""
conta_normal = False
conta_universitaria = True
"""
if opcao == 1:
    saque_cc = float(input("Informa o valor para saque: R$ "))
    if saldo >= saque_cc:
        print("Saque realizado com sucesso!")
    elif saque_cc <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")
elif opcao == 2:
    saque_cu = float(input("Informa o valor para saque: R$ "))
    if saldo >= saque_cu:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente!")
else:
    SystemExit
