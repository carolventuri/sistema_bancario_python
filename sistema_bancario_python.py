menu = """
Menu:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Novo Usuário
[5] Cadastrar Nova Conta
[6] Listar Contas
[0] Sair

Por favor, digite uma das opções acima: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"
numero_conta = 1

def depositar(saldo, valor, extrato, /): #todos os parâmetros que o que estão antes do / deve ser passados por posição
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print ("Depósito realizado com sucesso!")
    else:
        print("O valor informado é inválido. Por favor, digite um valor positivo para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # os parâmetros devem ser passados por nome (nomeado)
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
        print("Saque realizado com sucesso!")
    else:
        print("O valor informado é inválido.") 
    return saldo, extrato

def exibir_extrato (saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo, extrato

def criar_usuario (usuarios):
    cpf = input ("Informe o CPF: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print ("Já existe usuário com o CPF informado cadastrado!")
            return  # Sai da função se o CPF já existir
        
    nome = input ("Informe o nome completo: ")
    data_nascimento = input ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro, número - bairro - cidade/sigla estado)")

    usuarios.append ({"nome" : nome, "data_nascimento" : data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print ("Usuário cadastrado com sucesso!")


def criar_conta (agencia, numero_conta, usuarios):
    cpf = input ("Informe o CPF: ")
    criou_conta = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            criou_conta = True
            print ("Conta criada com sucesso!")
            return ({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
            
    
    if criou_conta == False:
        print ("Não há usuário cadastrado com o CPF informado. Favor, cadastrar usuário para posteriormente cadastrar a conta.")

def listar_contas (contas):
    for conta in contas:
        print(f"""
            Agência: {conta['agencia']}
            Conta Corrente: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
              """)
        print ("*" * 50)

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar (
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques= numero_saques,
            limite_saques= LIMITE_SAQUES,
        )
    
    elif opcao == "3":
        exibir_extrato (saldo, extrato = extrato)

    elif opcao == "4":
        criar_usuario (usuarios)

    elif opcao == "5":
        conta = criar_conta (AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append (conta)
            numero_conta += 1
            
    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        print ("Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")