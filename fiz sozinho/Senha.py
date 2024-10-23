n1 = []

x = input("Digite uma senha: ")
n1.append(x)

while True:

    n2 = input("Digite a senha para logar: ")

    if n2 == "fim":
        print("Programa encerrado.")
        break
    elif n2 == x:
        print("Acesso permitido!!")
        break
    else:
        print("Acesso nergado, tente novamente!")