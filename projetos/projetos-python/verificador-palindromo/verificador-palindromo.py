def eh_palindromo(texto):
    texto_limpo = texto.replace(" ", "").lower()
    texto_invertido = texto_limpo[::-1]

    return texto_limpo == texto_invertido

texto = input("Digite uma frase ou palavra aqui.")
if eh_palindromo(texto):
    print("É um palindromo")
else:
    print("Não é palindromo")