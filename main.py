"""Projetinho"""

menu = '''Menu Banco Nossa Divida

        1 - Saque
        2 - Deposito
        3 - Extrato
        4 - Sair
'''

saque = float
deposito = float
saldo = 0

extrato = " "

LIMITE_SAQUE = 3
LIMITE_VALOR = 500

contador_saque = 0

escolha = 1

while escolha != 4:
    print(menu)
    escolha = int(input("Escolha sua opção: "))

    match escolha:
        case 1:
            if contador_saque < 3:
                saque = float(input("Digite o valor do saque: "))
                if saque <= saldo:
                    if saque <= LIMITE_VALOR:
                        if saque > 0:
                            saldo -= saque
                            extrato += f"Saque: R$ {saque:.2f}\n"
                            print("Saque efetuado com sucesso!")
                            contador_saque += 1

                        else:
                            print("Valor de saque invalido, tente novamente!")
                    else:
                        print("Valor de saque excede o limite de saque.")
                else:
                    print("Valor de saque excede o valor de saldo!")
            else:
                print("O limite de saques diarios foi atingido!")

        case 2:
            deposito = float(input("Digite o valor de deposito: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Deposito: R$ {deposito:.2f}\n"
                print("Deposito efetuado com sucesso!")

            else:
                    print("Valor de deposito invalido, tente novamente!")

        case 3:
            extrato += f"Saldo: R$ {saldo:.2f}\n"
            print(extrato)

        case 4:
            break

        case _:
            print("Escolha invalida, tente novamente!")