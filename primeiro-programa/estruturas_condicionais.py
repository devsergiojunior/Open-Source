"""
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")
else :
    print("Saldo insufuciente!")

""" # Usando 3 aspta duplas ele vai comentar um bloco de texto


saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))
opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato \nOpção: "))

if opcao == 1:
    valor = float(input("Informa a quantia para saque: "))
    # ...
    if saldo >= valor:
        print("Realizando o saque!")
    else :
        print("Saldo insufuciente!")


elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    print("Opção invalida"), SystemExit