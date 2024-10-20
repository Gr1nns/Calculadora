print("Bem vindo à calculadora")

print("")

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro: "))

A = n1 + n2
S = n1 - n2
D = n1 / n2
M = n1 * n2

ac = str(input("Escolha o que quer fazer: Adição(A), Subtração(S), Divisão(D) ou Multiplicação(M): "))

if ac == "A":
    print("A soma de {} + {} é igual a {}".format(n1, n2, A))

elif ac == "S":
    print("A subtração de {} - {} é igual a {}".format(n1, n2, S))

elif ac == "D":
    print("A divisão de {} / {} é igual a {}".format(n1, n2, D))

elif ac == "M":
    print("A Multiplicação de {} * {} é igual a {}".format(n1, n2, M))
