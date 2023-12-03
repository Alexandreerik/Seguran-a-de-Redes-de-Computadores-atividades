## 1° Qual foi o conjunto original de critérios usados pelo NIST para avaliar as cifras AES candidatas?

O conjunto original de critérios(1997) considerados pela NIST inicialmente foram:
- 1. Segurança: ela foi o fator mais importante na avaliação e abrangeu características como resistência do algoritmo à criptoanálise, solidez de sua base matemática, aleatoriedade da saída do algoritmo e segurança relativa em comparação com outros candidatos.
- 2. Custo: O custo foi uma segunda área importante de avaliação que abrangeu requisitos de licenciamento, eficiência computacional (velocidade) em diversas plataformas e requisitos de memória.
- 3. Características de algoritmo e implementação: A terceira área de avaliação foram características de algoritmo e implementação, como flexibilidade, adequação de hardware e software e simplicidade de algoritmo.

## 2° Qual foi o conjunto final de critérios usados pelo NIST para avaliar as cifras AES candidatas?

O conjunto final de critérios(2000) considerados pela NIST inicialmente foram:
- 1. Segurança geral: Para avaliar a segurança geral, o NIST baseou-se na análise de segurança pública conduzida pela comunidade criptográfica. Durante o processo de avaliação de três anos, vários criptógrafos publicaram suas análises dos pontos fortes e fracos dos vários candidatos.
- 2. Implementações de software: As principais preocupações nesta categoria são a velocidade de execução, o desempenho em diversas plataformas e a variação de velocidade com o tamanho da chave.
- 3. Ambientes de espaço restrito: Em algumas aplicações, como cartões inteligentes, quantidades relativamente pequenas de memória de acesso aleatório (RAM) e/ou memória somente leitura (ROM) estão disponíveis para fins como armazenamento de código (geralmente em ROM).
- 4. Implementações de hardware: assim como o software, as implementações de hardware podem ser otimizadas em termos de velocidade ou tamanho. 
- 5. Ataques a implementações: O critério de segurança geral, discutido no primeiro item, preocupa-se com ataques criptoanalíticos que exploram propriedades matemáticas dos algoritmos. Existe outra classe de ataques que utiliza medições físicas realizadas durante a execução do algoritmo para coletar informações sobre quantidades, como chaves.
- 6. Criptografia versus descriptografia: Este critério trata de diversas questões relacionadas a considerações de criptografia e descriptografia


## 3° Qual é a diferença entre Rijndael e AES?

Rijndael é um algoritmo mais genérico que oferece suporte a vários tamanhos de chave e bloco. Já o AES é uma implementação específica do Rijndael, com parâmetros fixos definidos pelo NIST para estabelecer um padrão de cifra simétrica.

## 4° Responda:

### (a) Qual é a finalidade do array Estado?

O array estado é responsável por salvar as operações realizadas sobre o texto claro durante as fases de encriptação e decriptação. Após a etapa final, o array estado é copiado para uma matriz de saida.

### (b) Como é construída a S-box?

A S-box (Substitution box) é uma tabela de substituição usada no AES. Ela substitui cada byte do array Estado por outro byte de acordo com uma tabela predefinida. A construção da S-box envolve uma série de operações, incluindo a aplicação de uma função de inversão, operações de campo finito e permutações. A S-box é projetada para fornecer não linearidade e confusão, contribuindo para a segurança global do algoritmo AES.

### (c) Descreva rapidamente o estágio SubBytes, ShiftRows, MixColumns, AddRoundKey, e o algoritmo de expansão de chave.

- SubBytes: utiliza uma matriz S-box para realizar uma substituição byte a byte do bloco. Onde, por exemplo, para um hexadecimal A5 iriamos encontrar o elemento que está na linha A e coluna 5 na matriz S-box.

- ShiftRows: realiza uma permutação simples e circular entre os elementos do array de estados para esquerda na encriptação e para direita na decriptação. Sendo que a linha 0 não ocorre mudanças, na linha 1 ocorre o deslocamento de 1 byte, na linha 2 ocorre o deslocamenta de 2 byte, na linha 3 ocorre o deslocamento de 3 byte.

- MixColumns:  cada byte de uma coluna é mapeado para um novo valor que é determinado em função de todos os quatro bytes nessa coluna. A transformação pode ser definida por uma multiplicação de matriz sobre o array de estado. Então, trata-se de uma substituição que utiliza aritmética sobre GF(2<sup>8</sup>).
 

- AddRoundKey: os 128 bits de Estado passam por um XOR bit a bit com os 128 bits da chave da rodada. A operação é vista como uma do tipo coluna por coluna entre os 4 bytes da coluna Estado e uma palavra da chave da rodada.

- Algoritmo de expansão de chave: utiliza como entrada uma chave de 4 words (16 bytes) e produz um array linear de 44 words (176 bytes). Isso é suficiente para oferecer uma chave da rodada de 4 words para o estágio AddRoundKey inicial e para cada uma das 10 rodadas da cifra.


## 5° Quantos bytes em Estado são afetados por ShiftRows?

Durante o ShiftRows cada linha é deslocada para esquerda resultando nos seguintes números de bytes, considerando o array de estado:

1 - Nenhuma mudança na primeira linha.
2 - Deslocamento de 1 byte na segunda linha.
3 - Deslocamento de 2 bytes na terceira linha.
4 - Deslocamento de 3 bytes na quarta linha.

Somando no total temos 6 bytes afetados.


## 7° Compare AES com DES. Para cada um dos seguintes elementos do DES, indique o elemento comparável no AES ou explique por que ele não é necessário no AES.

### (a) XOR do material da subchave com a entrada da função f.

No AES, o material da subchave é gerado por meio de um processo de expansão de chave e não é submetido a XOR com a entrada para a função f. Em vez disso, o material da subchave é usado diretamente na etapa de adição da chave redonda.


### (b) XOR da saída da função f com a metade esquerda do bloco.

No AES, não há necessidade de XOR a saída da função f com a metade esquerda do bloco porque a função f opera em todo o bloco, não apenas na metade.

### (c) função f.

A função f no DES é usada para misturar os dados de entrada com o material da subchave. No AES, uma combinação de operações de substituição, permutação e mistura é usada na função round para atingir o mesmo objetivo.

### (d) permutação P.

 A permutação P em DES é usada para embaralhar os bits da saída da função f. No AES, uma combinação de operações de substituição e permutação é usada na função round para obter um efeito semelhante.


### (e) troca de metades do bloco.

No DES, as metades do bloco são trocadas após cada rodada. No AES, o bloco não é dividido ao meio, portanto não há necessidade de troca. Em vez disso, a função round opera em todo o bloco.