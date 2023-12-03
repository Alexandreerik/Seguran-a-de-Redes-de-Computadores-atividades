def cifra_cesar(texto, chave, modo):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''

    for char in texto:
        if char.upper() in alfabeto:
            indice = (alfabeto.index(char.upper()) + chave) % 26
            if char.isupper():
                resultado += alfabeto[indice]
            else:
                resultado += alfabeto[indice].lower()
        else:
            resultado += char

    return resultado

def main():
    texto = input("Digite o texto: ")
    chave = int(input("Digite a chave (um número inteiro): "))
    modo = input("Escolha o modo - 'encriptar' ou 'decriptar': ").lower()

    if modo == 'encriptar':
        resultado = cifra_cesar(texto, chave, modo='encriptar')
        print("Texto Encriptado:", resultado)
    elif modo == 'decriptar':
        resultado = cifra_cesar(texto, chave, modo='decriptar')
        print("Texto Decriptado:", resultado)
    else:
        print("Modo inválido. Escolha 'encriptar' ou 'decriptar'.")

if __name__ == "__main__":
    main()