def converter_temperatura():
    """Converte temperatura entre Celsius e Fahrenheit."""

    while True:
        print("Selecione a unidade de temperatura inicial:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Sair")

        opcao = input("Digite sua opção (1/2/3): ")

        if opcao == '3':
            break

        try:
            temperatura = float(input("Digite o valor da temperatura: "))

            if opcao == '1':
                # Celsius para Fahrenheit
                fahrenheit = (temperatura * 9/5) + 32
                print(f"{temperatura:.2f} °C equivale a {fahrenheit:.2f} °F")
            elif opcao == '2':
                # Fahrenheit para Celsius
                celsius = (temperatura - 32) * 5/9
                print(f"{temperatura:.2f} °F equivale a {celsius:.2f} °C")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    converter_temperatura()