menu = """

Menu:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Por favor, digite uma das opções acima: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido. Por favor, digite um valor positivo para depósito.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if (valor > saldo):
            print("Não há saldo suficiente em conta para o saque.")

        elif (valor > limite):
            print("O valor do saque excede o limite da conta.")

        elif (numero_saques >= LIMITE_SAQUES):
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print ("Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")