menu = """
[d] Depositar
[s] Sacar(Você só tem até 3 tentativas de saques diários e com limite de até R$500,00 por saque)
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
valores_depositados = 0
valores_sacados = 0

while True:
    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
        deposito = float(input("Informe o valor a ser depositado: "))
        if deposito < 0:
            print("Não é possível depositar valores negativos.")
        else:
            print("Depósito realizado com sucesso.")
            saldo += deposito
            valores_depositados += deposito
    elif opcao == "s":
        print("Saque")
        saque1 = float(input("Informe o valor a ser sacado: "))
        if saque1 <= saldo and saque1 <= limite and numero_saques < limite_saques:
            numero_saques += 1
            valores_sacados += saque1
            saldo -= saque1
            print("Saque realizado com sucesso!")
            novo_saque = input("Você deseja realizar um novo saque? (s) para sim ou (n) para não: ")
            if novo_saque == "s":
                saque2 = float(input("Informe o valor a ser sacado: "))
                if saque2 <= saldo and saque2 <= limite and numero_saques < limite_saques:
                    numero_saques += 1
                    valores_sacados += saque2
                    saldo -= saque2
                    print("Saque realizado com sucesso!")
                    novo_saque = input("Você deseja realizar um novo saque? (s) para sim ou (n) para não: ")
                    if novo_saque == "s":
                        saque3 = float(input("Informe o valor a ser sacado: "))
                        if saque3 <= saldo and saque3 <= limite and numero_saques < limite_saques:
                            numero_saques += 1
                            valores_sacados += saque3
                            saldo -= saque3
                            print("Saque realizado com sucesso!")
                            print("Fim de saque.")
                        else:
                            print("Você não tem saldo suficente ou atingiu o limite de saques diários verifique no extrato.")
                            print("*Você não pode sacar mais de R$500,00")
                    else:
                        print("Fim de saque.")
                else:
                    print("Você não tem saldo suficinte ou atingiu o limite de saques diários verifique no extrato.")
                    print("*Você não pode sacar mais de R$500,00")
            else:
                print("Fim de saque.")
        else:
            print("Você não tem saldo suficiente ou atingiu o limite de saques diários. ")
            print("*Você não pode sacar mais de R$500,00")
    elif opcao == "e":
        print("-------------Extrato---------------")
        print(f"Saldo atual R${saldo:.2f} ")
        print(f"Valor depositado R${valores_depositados:.2f} ")
        print(f"Total sacado R${valores_sacados:.2f} ")
        print(f"Tentativas de saque {numero_saques} ")
        print("-----------------------------------")
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    else:
        print("Operação inválida, por favor digite novamente a operação desejada.")