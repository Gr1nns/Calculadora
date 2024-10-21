print("Olá, Bem Vindo ao Conversor de temperaturas")
print("")



op1 = int(input("Digite o número da temperatura em celsius: "))

f1 = (op1 * 1.8)
fa = f1 + 32
kel = op1 + 273.15

print("A temperatura {}oC é igual a {} fahrenheits e igual a {} Kelvins".format(op1, fa, kel))
