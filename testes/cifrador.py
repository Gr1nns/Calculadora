def cifrar(mensagem, deslocamento):
    resultado = ""
    
    for letra in mensagem:
        if letra.isalpha():  # Verifica se o caractere é uma letra
            # Definir o ponto de referência (A ou a)
            base = ord('A') if letra.isupper() else ord('a')
            
            # Aplicar o deslocamento
            nova_letra = chr((ord(letra) - base + deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            resultado += letra  # Mantém espaços e outros caracteres

    return resultado

def decifrar(mensagem, deslocamento):
    # Para decifrar, basta inverter o deslocamento
    return cifrar(mensagem, -deslocamento)

# Solicitar entrada do usuário
escolha = input("Escolha: [C]ifrar ou [D]ecifrar: ").strip().upper()
mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite o número de deslocamento: "))

if escolha == 'C':
    mensagem_cifrada = cifrar(mensagem, deslocamento)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
elif escolha == 'D':
    mensagem_decifrada = decifrar(mensagem, deslocamento)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
else:
    print("Escolha inválida!")
