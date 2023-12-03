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

def ataque_frequencia(texto_cifrado, num_resultados=1):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultados = []

    for chave in range(1, 26):
        texto_decifrado = cifra_cesar(texto_cifrado, chave, modo='decriptar')
        frequencias = {letra: texto_decifrado.upper().count(letra) for letra in alfabeto}
        pontuacao = sum(frequencias.values())

        resultados.append((texto_decifrado, pontuacao, chave))

    # Ordena os resultados por pontuação em ordem decrescente
    resultados.sort(key=lambda x: x[1], reverse=True)

    # Mostra os resultados solicitados
    for i in range(min(num_resultados, len(resultados))):
        print(f"Resultado {i + 1}:")
        print("Texto Decifrado:", resultados[i][0])
        print("Pontuação:", resultados[i][1])
        print("Chave Usada:", resultados[i][2])
        print("\n")

def main():
    texto_cifrado = input("Digite o texto cifrado: ")
    num_resultados = int(input("Número de resultados a serem exibidos (por exemplo, 10): "))

    ataque_frequencia(texto_cifrado, num_resultados)

if __name__ == "__main__":
    main()