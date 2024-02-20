## 1.Quais são os principais elementos de um criptossistema de chave pública?
a. Chaves Pública e Privada: Um par de chaves, uma pública e outra privada, é gerado para cada usuário. A chave pública é compartilhada com outros usuários, enquanto a chave privada é mantida em segredo.

b. Algoritmo de Criptografia de Chave Pública: Este é o algoritmo usado para criptografar e descriptografar mensagens usando as chaves pública e privada.

c. Função de Hash Criptográfico: Utilizada para criar uma impressão digital única e fixa de uma mensagem, fornecendo integridade e autenticidade.

d. Certificados Digitais: Documentos eletrônicos que atestam a associação entre uma chave pública e a identidade de um usuário.


## 2. Quais são os papéis da chave pública e da privada? Descreva-os com detalhes e com exemplos.

a. Chave Pública: É usada para criptografar dados ou mensagens. Qualquer pessoa pode usar a chave pública para cifrar uma mensagem destinada ao proprietário da chave privada correspondente.

Exemplo: Se Alice quer enviar uma mensagem cifrada para Bob, ela usa a chave pública de Bob para criptografar a mensagem, e apenas Bob, com sua chave privada, pode descriptografar e ler a mensagem.

b. Chave Privada: É mantida em segredo e usada para descriptografar dados ou mensagens cifradas com a chave pública correspondente. Apenas o proprietário da chave privada deve ter acesso a ela.

Exemplo: Bob recebe a mensagem cifrada de Alice. Ele usa sua chave privada para descriptografar a mensagem e obter o conteúdo original.


## 3. Quais requisitos os criptossistemas de chave pública precisam cumprir para serem considerados como um algoritmo seguro?

a. Dificuldade de Fatoração: A segurança do sistema muitas vezes baseia-se na dificuldade de fatorar grandes números primos. Um algoritmo seguro deve resistir a tentativas eficientes de fatoração.

b. Complexidade do Problema Matemático: A segurança do criptossistema geralmente depende da complexidade de certos problemas matemáticos, como logaritmo discreto ou problema da raiz quadrada modular.

c. Tamanho das Chaves: Chaves maiores geralmente proporcionam maior segurança. O aumento do tamanho da chave pode tornar mais difícil a quebra do sistema por força bruta ou por métodos avançados.

d. Padrões e Certificações: A conformidade com padrões reconhecidos e certificações ajuda a garantir que o criptossistema tenha sido avaliado e considerado seguro por especialistas.

e. Resistência a Ataques Conhecidos: O algoritmo deve ser resistente a ataques conhecidos, como ataques de texto simples escolhido, ataques de texto cifrado escolhido, entre outros.

## 4. Descreva, em termos gerais, um procedimento eficiente para se escolher um número primo.

Escolher eficientemente um número primo envolve definir um intervalo, gerar números aleatórios nesse intervalo, aplicar um teste de primalidade como Miller-Rabin, realizar verificações adicionais se necessário, incrementar e repetir até encontrar um primo. Considere requisitos de segurança, atualize regularmente e utilize bibliotecas criptográficas confiáveis para implementação segura.
