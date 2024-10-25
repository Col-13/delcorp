saldo = 0
def depositar (valor):
    global saldo
    saldo += valor
    print(f"Deposito de R${valor:.2f} realizado com sucesso. Saldo atual R${saldo:.2f}.")
    
def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual R${saldo:.2f}.")
    else:
        print("Saldo insulficiente.")

def consultar_saldo():
    print(f"Seu saldo atual é R${saldo:.2f}.")

while True:
    print("\nBem vindo ao caixa eletrônico.")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        depositar(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor a ser sacado: "))
        sacar(valor)
    elif opcao == 3:
        consultar_saldo()
    elif opcao == 0:
        print("Obrigado por usar o caixa eletrônico!")
        break
    else:
        print("Opção invalida. Tente novamente.")
