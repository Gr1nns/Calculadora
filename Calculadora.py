print("Bem vindo à calculadora")
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro: "))
ac = str(input("Escolha o que quer fazer: Adição(A), Subtração(S), Divisão(D) ou Multiplicação(M): "))

if ac == "A" or ac == "a":
    A = n1 + n2
    print("A soma de {} + {} é igual a {}".format(n1, n2, A))

elif ac == "S" or ac == "s":
    S = n1 - n2
    print("A subtração de {} - {} é igual a {}".format(n1, n2, S))

elif ac == "D" or ac == "d":
    if n2 != 0:
        D = n1 / n2
        print("A divisão de {} / {} é igual a {}".format(n1, n2, D))
    else:
        print("You can not divide by zero!")
elif ac == "M" or ac == "m":
    M = n1 * n2
    print("A Multiplicação de {} * {} é igual a {}".format(n1, n2, M))
