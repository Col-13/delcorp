def calcular_imc():
    """Calcula o índice de massa corporal (IMC)."""

    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    peso = float(input("Digite seu peso em quilogramas: "))

    imc = peso / (altura ** 2)

    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Seu peso está normal.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está obeso.")

if __name__ == "__main__":
    calcular_imc()