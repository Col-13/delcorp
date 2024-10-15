def contar_palavras(texto):
    """Conta a frequência de cada palavra em um texto.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        dict: Um dicionário onde as chaves são as palavras e os valores são as suas contagens.
    """

    # Quebrar o texto em palavras, removendo pontuação e convertendo para minúsculas
    palavras = texto.lower().split()

    # Criar um dicionário para armazenar a contagem de cada palavra
    contagem_palavras = {}

    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1

    return contagem_palavras

# Exemplo de uso
texto = "Este é um exemplo de texto. Este texto é usado para testar o programa."
resultado = contar_palavras(texto)

print(resultado)