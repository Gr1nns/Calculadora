def contar_vogais(frase):
    vogais = "aeiou"
    total_vogais = 0

    frase = frase.lower()

    for letra in frase:
        if letra in vogais:
            total_vogais += 1

    return total_vogais

frase_usuario = input("Digite uma frase: ")
total = contar_vogais(frase_usuario)

print("Total de vogais: {}".format(total))