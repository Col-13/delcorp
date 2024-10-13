def calculadora():
    """Simula uma calculadora simples."""

    while True:
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        opcao = input("Digite sua opção (1/2/3/4/5): ")

        if opcao == '5':
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = num1 + num2
                print("Resultado:", resultado)
            elif opcao == '2':
                resultado = num1 - num2
                print("Resultado:", resultado)
            elif opcao == '3':
                resultado = num1 * num2
                print("Resultado:", resultado)
            elif opcao == '4':
                if num2 == 0:
                    print("Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print("Resultado:", resultado)
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

if __name__ == "__main__":
    calculadora()