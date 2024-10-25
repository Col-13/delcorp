def contar_letras_e_palavras(texto):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTWXYZ"

    num_vogais = sum(1 for letra in texto if letra in vogais)
    num_consoantes = sum(1 for letra in texto if letra in consoantes)
    num_palavras = len(texto.split())

    return {
        "vogais": num_vogais,  # Corrigido para nun_vogais
        "consoantes": num_consoantes,
        "palavras": num_palavras
    }

texto = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Cumque suscipit libero rem aspernatur, eaque officiis, quas architecto exercitationem earum in autem optio voluptatibus culpa ullam laudantium odio dolore unde corporis?"
resultado = contar_letras_e_palavras(texto)
print(resultado)