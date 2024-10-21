n = int(input("Digite um número inteiro positivo: "))

f = 1

for i in range(1, n + 1):
    f *= i

print("O fatorial de {} é {}".format(n, f))
