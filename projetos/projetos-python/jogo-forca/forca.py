import random

def jogar_forca():
    """Função principal do jogo da forca."""

    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'dados']
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print("Bem-vindo ao jogo da Forca!")

    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Chute uma letra: ").strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

    if(acertou):
        print("Parabéns! Você ganhou!")
        print(f"A palavra era {palavra_secreta}.")
    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}.")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
    if(erros == 2):
        print(" |      \     ")
    if(erros == 3):
        print(" |       \    ")
    if(erros == 4):
        print(" |      / \   ")
    if(erros == 5):
        print(" |     /   \  ")
    if(erros == 6):
        print(" |      |     ")

    print(" |            ")
    print("_|__________")

if __name__ == "__main__":
    jogar_forca()