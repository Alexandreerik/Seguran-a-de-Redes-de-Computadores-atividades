## 1. Qual é a diferença entre aleatoriedades estatísticas e imprevisibilidade?

Aleatoriedades Estatísticas: Refere-se à capacidade de um processo gerar uma sequência de bits que, estatisticamente, se assemelha a uma sequência verdadeiramente aleatória. Mesmo que a sequência não seja verdadeiramente aleatória, ela deve exibir propriedades estatísticas que tornem difícil distinguir entre a sequência gerada e uma sequência aleatória. Isso está relacionado à uniformidade e independência dos bits na sequência.

Imprevisibilidade: Refere-se à dificuldade de prever o próximo bit ou conjunto de bits em uma sequência, mesmo conhecendo parte ou toda a sequência passada. A imprevisibilidade está mais relacionada à resistência a ataques de análise de padrões ou predição.

## 2. Liste considerações de projeto importantes para uma cifra de fluxo.

Geração de Chave Aleatória: O processo de geração de chave deve ser robusto e garantir uma chave inicial única e aleatória para evitar padrões previsíveis na sequência cifrada.

Não Linearidade: O algoritmo deve incluir operações não lineares para tornar a cifra resistente a ataques diferencias e lineares.

Período Longo: A cifra deve ter um período longo para evitar repetições na sequência cifrada durante um período significativo de tempo.

Distribuição Uniforme: Os bits na sequência cifrada devem ser distribuídos uniformemente para evitar viés estatístico.

Resistência a Ataques Conhecidos-Plaintext: A cifra deve ser resistente a ataques onde um adversário tem conhecimento do texto simples (plaintext) correspondente a uma parte da sequência cifrada.

## 3. Por que não é desejável reutilizar uma chave de cifra de fluxo?

Vulnerabilidade a Ataques de XOR: Se uma chave de cifra de fluxo é reutilizada, existe o risco de que partes da sequência cifrada resultante também sejam iguais, o que facilita ataques de XOR, onde o atacante pode cancelar bits correspondentes e recuperar informações sobre os textos simples.

Quebra do Segredo da Chave: Reutilizar uma chave de cifra de fluxo pode levar à quebra do segredo da chave, especialmente se parte da sequência cifrada for conhecida. Isso pode comprometer a confidencialidade do sistema.

Perda de Unicidade da Sequência Cifrada: A reutilização de chaves pode levar à repetição de partes da sequência cifrada, o que é indesejável. A unicidade da sequência cifrada é essencial para a segurança da cifra de fluxo.

## 4. Que operações primitivas são usadas no RC4?


Inicialização do Vetor de Estado:

O algoritmo inicia um vetor de estado (geralmente uma matriz S) com valores sequenciais de 0 a 255.
Permutação do Vetor de Estado (Swap):

O vetor de estado é permutado (reorganizado) com base nas chaves fornecidas. Isso envolve trocar elementos do vetor de estado para criar uma mistura inicial.
Geração de Pseudo-Random Bytes:

A partir do vetor de estado permutado, o algoritmo gera uma sequência pseudo-aleatória de bytes. Esses bytes são usados como chave stream para realizar a operação de XOR com o texto simples, produzindo o texto cifrado.
Operação de XOR (OU Exclusivo):

A operação de OU Exclusivo (XOR) é aplicada entre os bytes do texto simples e os bytes gerados pelo RC4. Isso resulta no texto cifrado.
Essas operações são repetidas para cada byte do texto simples, produzindo a sequência cifrada. 

## 6. (a) Qual é o período máximo que pode ser obtido do seguinte gerador?
Xn+1 = (aXn) mod 24

(b) Qual deverá ser o valor de a?
(c) Que restrições são exigidas na semente?

## 7. Que valor de chave RC4 deixará S inalterado durante a inicialização? Ou seja, após a permu-
tação inicial de S, as entradas de S serão quais aos valores de 0 a 255 na ordem crescente.

## 8. O algoritmo Blum Blum Shub é baseado na teoria dos resíduos quadráticos e utiliza três números inteiros para realizar os cálculos: p, q e s.

(a) Escolha dois números primos grandes p e q, onde p e q sejam congruentes a 3 mod 4 e não tenham fatores primos comuns. Por exemplo, você pode escolher p = 499 e q = 503.

(b) Calcule n = p ∗ q. Neste caso, n seria igual a 499 ∗ 503 = 250997.
(c) Escolha um número inteiro s entre 1 e n − 1 que seja co-primo com n. Por exemplo, você
pode escolher s = 17.
(d) Calcule o valor inicial x0 = (s2) mod n. Neste caso, x0 seria igual a (172) mod 250997 =289.
(e) Agora, vamos gerar uma sequência de números aleatórios usando o algoritmo Blum Blum Shub. Para gerar cada número da sequência, use a seguinte fórmula: xi = (x2i−1) mod n.
(f) Execute a fórmula várias vezes para gerar uma sequência de números aleatórios. Por
exemplo, você pode executar a fórmula 10 vezes para obter 10 números aleatórios.
Aqui está a sequência de números aleatórios gerados usando o algoritmo Blum Blum Shub comos valores do exemplo:

289, 253306, 14107, 23546, 67740, 144593, 79829, 46219, 132936, 9863

Qual foi a sua sequência?


