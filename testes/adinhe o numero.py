import random

numero_aleatorio = random.randint(1, 100)

palpite = None

print ("Tente adivinhar o número entre 1 e 100!") 

while palpite != numero_aleatorio:
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_aleatorio:
        print("O numero é maior.")

    elif palpite > numero_aleatorio:
        print("O numero é menor.")

    else:
        print("Parabens!!! Você adivinhou o numero!!")