## 1. Responda os questionamentos a seguir:
### (a) Por que é importante estudar a cifra de Feistel?
Estudar a cifra de Feistel é de importância fundamental no campo da criptografia. Este modelo teórico de cifragem simétrica oferece uma compreensão profunda dos princípios criptográficos, sendo a base para muitos algoritmos amplamente utilizados, incluindo o Data Encryption Standard (DES). Sua simplicidade e eficiência computacional, aliadas a um nível adequado de segurança, destacam a cifra de Feistel como um modelo crucial para a criação e análise de algoritmos criptográficos. Ao compreender esse modelo, os profissionais podem não apenas explorar seu papel histórico, mas também adaptá-lo e evoluí-lo para atender aos desafios contemporâneos da segurança da informação.

### (b) Qual é a diferença entre uma cifra de bloco e uma cifra de fluxo?
Cifra de Bloco: Opera em blocos fixos de dados, cifrando-os independentemente. Exemplo: DES, AES.
Cifra de Fluxo: Ópera em bits ou pequenas unidades, cifrando de forma contínua. Exemplo: RC4.

### (d) O que é uma cifra de produto?
Uma cifra de produto é um tipo de cifra simétrica que opera em múltiplos blocos de dados simultaneamente, ao contrário das cifras de bloco tradicionais que processam um bloco por vez. Essa abordagem paralela permite uma eficiência superior em termos de processamento de informações, sendo exemplificada pelo modo de operação GCM (Galois/Counter Mode) usado em algoritmos como o AES.

### (e) Qual é a diferença entre difusão e confusão?
Na difusão, a estrutura estatística do texto claro é dissipada em estatísticas de longa duração do texto cifrado. A confusão procura estabelecer o relacionamento entre as estatísticas do texto cifrado e o valor da chave de encriptação o mais complexo possível, novamente para frustrar tentativas de descobrir a chave.

### (f) Que parâmetros e escolhas de projeto determinam o algoritmo real de uma cifra de Feistel?

O tamanho de bloco, o tamanho de chave e o número de rodadas.

### (g) Explique o efeito avalanche.

É uma pequena mudança no texto claro ou na chave que produza uma alteração significativa no texto cifrado.

## 2. Qual(is) dos recursos abaixo estão presentes no projeto da rede de Feistel? Explique.
### (a) Tamanho do bloco e da chave;
Tamanho do bloco e da chave: O tamanho do bloco é uma parte essencial do projeto da rede de Feistel. Define o número de bits que a cifra processa em cada rodada. A chave também é fundamental, pois determina como a cifra opera em cada rodada.
### (b) Função da rodada;
Função da rodada: A função da rodada (às vezes chamada de função de Feistel) é uma parte crítica do design da rede de Feistel. É a função não-linear que opera nos blocos de dados em cada rodada. É o coração da operação de Feistel e é responsável pela complexidade e segurança da cifra.
### (c) Gerador de sub-chaves;
Gerador de sub-chaves: O gerador de sub-chaves é uma parte integral do projeto da rede de Feistel. Ele é responsável por derivar sub-chaves a partir da chave principal, que são usadas em cada rodada. A forma como as sub-chaves são geradas é uma consideração importante na segurança e eficácia da cifra.
### (d) Todas as alternativas.
Resposta correta.

## 3. Qual é o tamanho do texto claro no Data Encryption Standard (DES)? Explique. (a) 57; (b) 48; (c) 32; (d) 64.
(d) 64
O Data Encryption Standard (DES) opera com blocos de texto claro de 64 bits. Isso significa que cada vez que o algoritmo DES é aplicado, ele cifra ou decifra 64 bits de dados de uma vez. 

## 5. A cifra de Feistel do algoritmo de encriptação utilizada no Data Encryption Standard (DES) utiliza quantos S-boxes? Explique.(a) 8; (b) 7; (c) 6; (d) 5.


(a) 8.
O algoritmo de encriptação utilizado no Data Encryption Standard (DES) utiliza um total de 8 S-boxes em cada rodada do processo de Feistel. Cada S-box é uma tabela de substituição que transforma um conjunto de bits de entrada em um conjunto de bits de saída de acordo com uma regra pré-definida. Eles desempenham um pap
