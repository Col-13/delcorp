import random

def lancar_dados():
    """Simula o lançamento de dois dados e exibe os resultados."""

    while True:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"Resultado do lançamento: {dado1} e {dado2}")

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    lancar_dados()