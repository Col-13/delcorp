import random
import string

def gerar_senha(tamanho, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    """Gera uma senha aleatória personalizada.

    Args:
        tamanho (int): Tamanho da senha.
        maiusculas (bool, optional): Incluir letras maiúsculas. Defaults to True.
        minusculas (bool, optional): Incluir letras minúsculas. Defaults to True.
        numeros (bool, optional): Incluir números. Defaults to True.
        especiais (bool, optional): Incluir caracteres especiais. Defaults to True.

    Returns:
        str: Senha aleatória gerada.
    """

    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha: "))
    maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    numeros = input("Incluir números? (s/n): ").lower() == 's'
    especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, especiais)
    print("Senha gerada:", senha)