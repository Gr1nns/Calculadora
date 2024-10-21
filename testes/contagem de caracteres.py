en = input("Digite uma palavra ou frase: ")

contagem = {}

for caractere in en:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

print("Contagem de caracteres:")
for caractere, quantidade in contagem.items():
    print("{}: {}".format(caractere, quantidade))