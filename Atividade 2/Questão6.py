import numpy

#Esta função cria uma matriz 3x3
#a partir da chave fornecida, onde os elementos da matriz
#são os valores numéricos equivalentes às letras da chave.
def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m


# C = P*K mod 26
def encrypt(P, K):
    C=[0,0,0]
    C[0] = (K[0][0]*P[0] + K[1][0]*P[1] + K[2][0]*P[2]) % 26
    C[1] = (K[0][1]*P[0] + K[1][1]*P[1] + K[2][1]*P[2]) % 26
    C[2] = (K[0][2]*P[0] + K[1][2]*P[1] + K[2][2]*P[2]) % 26
    return C

#Esta função divide a mensagem em blocos de três letras e, em seguida, criptografa cada bloco
def Hill(message, K):
    cipher_text = []
    #Transformando a mensagem em 3 caracteres por vez
    for i in range(0,len(message), 3):
        P=[0, 0, 0]
        #Atribua o valor inteiro correspondente a cada letra
        for j in range(3):
            P[j] = ord(message[i+j]) % 65
        #Criptografar três letras
        C = encrypt(P,K)
        #Adicione as 3 letras criptografadas ao texto cifrado final
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
        #Repita até que todos os conjuntos de três letras sejam processados.

    #retornar uma string
    return "".join(cipher_text)

#Esta função calcula a matriz inversa de K em módulo 26 usando a inversa multiplicativa modular.
def MatrixInverse(K):
    det = int(numpy.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = numpy.delete(Dji, (j), axis=0)
            Dji = numpy.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv


if __name__ == "__main__":

    message = "MYSECRETMESSAGE"
    key = "RRFVSVCCT"
    #Crie a matriz K que será usada como chave
    K = create_matrix_from(key)
    print(K)
    # C = P * K mod 26
    cipher_text = Hill(message, K)
    print ('Cipher text: ', cipher_text)


    # Decrypt
    # P = C * K^-1 mod 26
    K_inv = MatrixInverse(K)
    plain_text = Hill(cipher_text, K_inv)
    print ('Plain text: ', plain_text)

# K x K^-1 verificando se a matriz é igual à matriz identidade
    M = (numpy.dot(K,K_inv))
    for i in range(3):
        for j in range(3):
            M[i][j] = M[i][j] % 26
    print(M)