## 1- Responda (de forma objetiva) as questões a seguir:
### (a) Quais são os elementos essenciais de uma cifra simétrica?
Os elementos essenciais de uma cifra simétrica são: uma chave e um algoritmo de
cifragem/decifragem. A mesma chave é usada tanto para cifrar quanto para descifrar a
mensagem.
### (b) Quais são as duas funções básicas usadas nos algoritmos de encriptação?
As duas funções básicas usadas nos algoritmos de encriptação são: a função de cifragem
(que transforma o texto claro em texto cifrado) e a função de decifragem (que transforma o
texto cifrado de volta para o texto claro).
### (c) Qual é a diferença entre uma cifra de bloco e uma cifra de fluxo?
A diferença entre uma cifra de bloco e uma cifra de fluxo é a forma como elas operam. Uma
cifra de bloco cifra os dados em blocos fixos de tamanho, enquanto uma cifra de fluxo cifra
os dados bit a bit ou byte a byte, normalmente em tempo real.
### (d) Quais são as duas técnicas gerais para atacar uma cifra?
As duas técnicas gerais para atacar uma cifra são: ataque de força bruta (tentativa
sistemática de todas as chaves possíveis) e criptoanálise (exploração de fraquezas no
algoritmo para encontrar a chave ou a mensagem sem a chave).
### (e) Quais são os dois problemas com o one-time pad?
Os dois problemas com o one-time pad são a necessidade de chaves extremamente longas
e aleatórias, o que pode ser impraticável em muitas situações, e a dificuldade de distribuir
chaves únicas e seguras para ambas as partes.

### (f) O que é uma cifra de transposição?
Uma cifra de transposição é um tipo de cifra na qual as posições dos caracteres no texto
são alteradas de acordo com um determinado sistema. Em vez de substituir os caracteres,
como nas cifras de substituição, os caracteres são rearranjados.
### (g) O que é esteganografia?
Esteganografia é a prática de ocultar informações dentro de outros dados (como imagens,
áudio, texto, etc.) de forma que a presença da informação oculta seja imperceptível para
observadores não autorizados.

## 2- Uma generalização da cifra de César, conhecida como cifra de César afim, tem a seguinte forma: a cada letra de texto claro p, substitua-a pela letra de texto cifrado C : C = E([a, b], p) = (ap + b) mod 26 um requisito básico de qualquer algoritmo de encriptação é que ele seja um para um. Ou seja, se p ̸= q, então E(k, p) ̸= E(k, q). Caso contrário, a decriptação é impossível, pois mais de um caractere de texto claro é mapeado no mesmo caractere de texto cifrado. A cifra de César afim não é um-para-um para todos os valores de a. Por exemplo, para a = 2 e b = 3, então E([a, b], 0) = E([a, b], 13) = 3.


## (a) existem limitações sobre o valor de b? explique por que sim ou por que não.
 Sim, há uma limitação sobre o valor de b na cifra de César afim. A razão para isso é que, se b for um múltiplo de 26 ou tiver um fator comum com 26, a função de encriptação não será um-para-um. Isso significa que diferentes valores de p podem resultar no mesmo valor de C, tornando a decriptação ambígua.
## (b) determine quais valores de a não são permitidos.
Os valores de 'a' que não são permitidos são aqueles que são divisíveis por 13 ou têm um fator comum com 13. Isso ocorre porque 13 é o fator comum mais alto de 26 (o tamanho do alfabeto em uma cifra de César afim).

## (c) ofereça uma afirmação geral sobre quais valores de a são e não são permitidos. Justifique-a.
 Em geral, os valores de 'a' permitidos são aqueles que são primos relativos a 26 (ou seja, não têm fatores comuns com 26, exceto 1). Isso garante que a função de encriptação seja um-para-um, pois não haverá fatores comuns que possam resultar em ambiguidade durante a decriptação. Os valores de 'b' devem ser escolhidos de maneira a evitar múltiplos de 26 para garantir a unicidade da encriptação para diferentes valores de 'p'.





