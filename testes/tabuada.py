print("Bem vindo a tabuada!!!")
print("")

n1 = int(input("Digite um numero inteiro para tabuada: "))

for i in range(1, 11):
    r = n1 * i
    print("{} X {} = {}".format(n1, i, r))