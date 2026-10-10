Aula 01
TJs - Curso Regular - Matemática e
Raciocínio Lógico 
Autor:
Equipe Exatas Estratégia
Concursos
03 de Maio de 2026
95298789153 - Sibeli Maria Linhares Santos


Equipe Exatas Estratégia Concursos
Aula 01
Índice
..............................................................................................................................................................................................
1) Equivalências Lógicas
3
..............................................................................................................................................................................................
2) Álgebra de Proposições
43
..............................................................................................................................................................................................
3) Questões Comentadas - Equivalências Lógicas - Multibancas
59
..............................................................................................................................................................................................
4) Questões Comentadas - Álgebra de Proposições - Multibancas
133
..............................................................................................................................................................................................
5) Lista de Questões - Equivalências Lógicas - Multibancas
141
..............................................................................................................................................................................................
6) Lista de Questões - Álgebra de Proposições - Multibancas
163
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
2
167


 APRESENTAÇÃO DA AULA 
Fala, pessoal! 
O principal assunto da aula de hoje é equivalências lógicas.  
O entendimento da aula é muito importante, porém igualmente importante é que você DECORE as 
principais equivalências lógicas. Equivalências lógicas existem para serem usadas, e o uso delas requer que 
você tenha as principais fórmulas "no sangue". 
Em seguida, será abordado álgebra de proposições. Nesse assunto, você deve focar especialmente nas 
propriedades comutativa, associativa e distributiva. Além disso, nesse tópico, trataremos do uso de 
equivalências lógicas para a resolução de problemas de tautologia, contradição e contingência. 
Como de costume, vamos exibir um resumo logo no início de cada tópico para que você tenha uma visão 
geral do conteúdo antes mesmo de iniciar o assunto.  
 
Conte comigo nessa caminhada =) 
Prof. Eduardo Mocellin. 
@edu.mocellin 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
3
167


EQUIVALÊNCIAS LÓGICAS 
 
Duas proposições A e B são equivalentes quando todos os valores lógicos (V ou F) assumidos por elas são 
iguais para todas as combinações de valores lógicos atribuídos às proposições simples que as compõem. 
 
 
Equivalência contrapositiva 
p→q ≡ ~q→~p 
 
Transformação da condicional (se...então) em disjunção inclusiva (ou) 
p→q ≡ ~p∨q 
 
Transformação disjunção inclusiva (ou) em condicional (se...então) 
p∨q ≡ ~p→q 
 
 
 
Dupla negação da proposição simples 
 
~(~p) ≡ p 
 
Negação da conjunção e da disjunção inclusiva (Leis de De Morgan) 
Para negar "e":  negar ambas as proposições e trocar o "e" pelo "ou".  
 
~(p∧q) ≡ ~p∨~q 
 
Para negar "ou":  negar ambas as proposições e trocar o "ou" pelo "e".  
 
~(p∨q) ≡ ~p∧~q 
 
Negação da condicional (se...então) 
~(p→q) ≡ p∧~q 
 
 
Negação da conjunção (e) para a forma condicional (se...então) 
 
~(p∧q) ≡ p→~q 
 
~(p∧q) ≡ q →~p 
Conjunção de condicionais 
 
Quando o termo comum é o consequente, a equivalência apresenta uma disjunção inclusiva no 
antecedente. 
(p→r)∧(q→r) ≡ (p∨q)→r 
 
Quanto o termo comum é o antecedente, a equivalência apresenta uma conjunção no consequente. 
 
(p→q)∧(p→r) ≡ p→(q∧r) 
Equivalências lógicas 
Equivalências fundamentais 
Negações lógicas 
Outras equivalências e negações 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
4
167


 
Equivalências da disjunção exclusiva (ou...ou) 
 
p∨q ≡ (~p)∨(~q) 
 
p∨q ≡ (~p)q 
 
p∨q ≡ p(~q) 
 
 
Negações da disjunção exclusiva (ou...ou) 
~(p∨q) ≡ pq 
 
~(p∨q) ≡ (~p)∨q 
 
~(p∨q) ≡ p∨(~q) 
 
Equivalências da bicondicional (se e somente se) 
 
pq ≡ (p→q)∧(q→p) 
 
pq ≡ (~p)(~q) 
 
 pq ≡ (~p)∨q 
 
 pq ≡ p∨(~q) 
 
Negações da bicondicional (se e somente se) 
~(pq) ≡ p∨q 
 
~(pq) ≡ (~p)q 
 
~(pq) ≡ p(~ q)  
 
~(pq) ≡ (p∧~q)∨(q∧~p) 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
5
167


O que é uma equivalência lógica 
Quando duas proposições apresentam a mesma tabela-verdade, dizemos que as proposições são 
equivalentes.  
A representação da equivalência lógica é dada pelo o símbolo ⇔ ou ≡. Se A é equivalente a B, podemos 
escrever de duas maneiras: 
A ⇔ B 
A ≡ B 
Observação: o símbolo de equivalência ⇔ é diferente do conectivo bicondicional  
Informalmente, podemos dizer que duas proposições são equivalentes quando elas têm o mesmo 
significado. Exemplo: 
a: "Eu moro em Taubaté." 
b: "Não é verdade que eu não moro em Taubaté." 
O conceito de equivalência lógica pode ser melhor detalhado assim:  
 
Duas proposições A e B são equivalentes quando todos os valores lógicos (V ou F) 
assumidos por elas são iguais para todas as combinações de valores lógicos atribuídos às 
proposições simples que as compõem. 
Vejamos um exemplo: 
Mostre que as proposições (p→q)∧(q→p) e pq são equivalentes. 
Para resolver esse problema, basta construirmos a tabela-verdade de ambas proposições. Como a 
bicondicional já é conhecida por nós, precisamos simplesmente confeccionar a tabela-verdade de 
(p→q)∧(q→p) e comparar com a bicondicional pq.  
 
Passo 1: determinar o número de linhas da tabela-verdade. 
Temos duas proposições simples distintas, p e q. Logo, o número de linhas é  2𝑛= 22 = 4. 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
6
167


Passo 2: desenhar o esquema da tabela-verdade. 
Para determinar (p→q)∧(q→p), precisamos obter (p→q) e (q→p).  
Para determinar (p→q), precisamos obter p e q. 
Para determinar (q→p), precisamos obter p e q. 
 
Podemos também incluir, de imediato, na nossa tabela a condicional pq, pois vamos compará-la com a 
expressão que estamos querendo obter. 
 
 
Passo 3: atribuir V ou F às proposições simples de maneira alternada. 
 
 
Passo 4: obter o valor das demais proposições. 
A condicional p→q é falsa somente quando o antecedente p for verdadeiro e o consequente q for falso. 
 
 
A condicional q→p é falsa somente quando o antecedente q for verdadeiro e o consequente p for falso. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
7
167


A conjunção (p→q)∧(q→p) só será verdadeira quando p→q e q→p forem ambos verdadeiros.  
 
Para a bicondicional, já sabemos que ela será verdadeira quando p e q tiverem o mesmo valor lógico. 
 
 
Podemos perceber da análise da tabela-verdade acima que (p→q)∧(q→p) e pq assumem os exatos 
mesmos valores lógicos para todas as possibilidades de valores lógicos de p e q. Logo, as proposições são 
equivalentes. Veja: 
 
 
Podemos escrever: 
pq ⇔ (p→q)∧(q→p) 
ou 
pq ≡ (p→q)∧(q→p) 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
8
167


Equivalências fundamentais 
Existem três equivalências fundamentais que despencam em provas de concurso público:  
• Equivalência contrapositiva; 
• Transformação da condicional (se...então) em disjunção inclusiva (ou); e  
• Transformação da disjunção inclusiva (ou) em condicional (se...então). 
Equivalência contrapositiva 
A primeira equivalência fundamental é conhecida como contrapositiva da condicional: 
p→q ≡ ~q→~p  
A equivalência é realizada do seguinte modo: 
1. Invertem-se as posições do antecedente e do consequente; e 
2. Negam-se ambos os termos da condicional.  
Como exemplo, sejam as proposições:  
p: “Hoje choveu.” 
q: “João fez a barba.” 
Considere a seguinte condicional p→q: 
p→q: "Se [hoje choveu], então [João fez a barba]." 
A condicional a seguir é equivalente à condicional original: 
~q→~p: "Se [João não fez a barba], então [hoje não choveu]." 
 
Um erro muito explorado pelas bancas é dizer que p→q seria equivalente a ~p→~q. Isso 
porque é muito comum no dia a dia as pessoas cometerem esse erro. 
Observe o exemplo acima: "Se hoje choveu, então João fez a barba". Vamos supor que não 
choveu. O que podemos afirmar sobre a barba de João? Absolutamente nada, ele pode 
tanto ter feito quanto não ter feito a barba. Logo, não podemos dizer que "Se hoje não 
choveu, então João não fez a barba" é equivalente à condicional original. Em outras 
palavras, não podemos dizer que ~p→~q é equivalente a p→q. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
9
167


 
Por outro lado, podemos afirmar sem dúvida que ~q→~p. Em outras palavras, 
considerando a proposição original, podemos dizer que "Se João não fez a barba, então 
hoje não choveu". 
Em resumo:  
p→q é equivalente a ~q→~p 
p→q não é equivalente a ~p→~q 
Vamos resolver um exercício envolvendo essa equivalência que acabamos de aprender. 
(EPC/2023) Considere a seguinte afirmação: 
Se subir a montanha é difícil, então a paisagem compensa. 
Assinale a alternativa que contém uma equivalente lógica à afirmação apresentada. 
a) Subir a montanha é difícil e a paisagem compensa. 
b) Subir a montanha não é difícil e a paisagem não compensa. 
c) Se a paisagem não compensa, então subir a montanha não é difícil. 
d) Se subir a montanha é difícil, então a paisagem não compensa. 
e) Subir a montanha não é difícil ou a paisagem não compensa. 
Comentários: 
Sejam as proposições simples: 
m: "Subir a montanha é difícil." 
p: "A paisagem compensa." 
A sentença original pode ser descrita por m→p: 
m→p: “Se [subir a montanha é difícil], então [a paisagem compensa].” 
 
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p→q ≡ ~q→~p. Para 
aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
m→p ≡ ~p→~m 
A proposição equivalente pode ser descrita por: 
~p→~m: “Se [a paisagem não compensa], então [subir a montanha não é difícil]”. 
Gabarito: Letra C. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
10
167


Transformação da condicional (se...então) em disjunção inclusiva (ou) 
A segunda equivalência fundamental é a transformação da condicional (se...então; →) em disjunção 
inclusiva (ou; ∨): 
p→q ≡ ~p∨q 
A equivalência é realizada do seguinte modo: 
1. Nega-se o primeiro termo;  
2. Troca-se a condicional (se...então; →) pela disjunção inclusiva (ou; ∨); e 
3. Mantém-se o segundo termo. 
Como exemplo, considere novamente a seguinte condicional: 
p→q: "Se [hoje choveu], então [João fez a barba]." 
Observe que a frase seguinte é equivalente: 
~p∨q: "[Hoje não choveu] ou [João fez a barba]." 
Antes de realizar alguns exercícios sobre essa equivalência, é importante que você saiba que a condicional 
p→q apresenta somente duas possíveis equivalências: ~q→~p e ~p∨q: 
 
A condicional p→q apresenta somente duas possíveis equivalências: 
 
p→q ≡ ~q→~p 
p→q ≡ ~p∨q 
 
Portanto, uma condicional só pode ser equivalente a outra condicional ou a uma disjunção 
inclusiva. 
Vamos resolver exercícios envolvendo essa equivalência que acabamos de aprender. 
(PROCON-DF/2023) A respeito de raciocínio lógico, julgue o item. 
As proposições “Se Alice é uma estudante de medicina, então ela é inteligente” e “Alice não é uma estudante 
de medicina ou é inteligente” são equivalentes.  
Comentários: 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
11
167


Sejam as proposições simples: 
e: "Alice é uma estudante de medicina." 
i: "Alice é inteligente." 
 
A proposição original pode ser descrita por e→i: 
e→i: "Se [Alice é uma estudante de medicina], então [ela (Alice) é inteligente]." 
 
Note que a questão sugere que a proposição original é equivalente a uma disjunção inclusiva (ou; ∨). 
Devemos, portanto, usar a equivalência da transformação da condicional (se...então; →) em disjunção 
inclusiva (ou; ∨). 
p→q ≡ ~p∨q 
 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (se...então; →) pela disjunção inclusiva (ou; ∨); e 
• Mantém-se o segundo termo. 
 
Para o caso em questão, temos: 
e→i ≡ ~e∨i 
 
A proposição equivalente pode ser descrita por: 
~e∨i: "[Alice não é uma estudante de medicina] ou [(Alice) é inteligente]." 
Gabarito: CERTO. 
 
(Pref. S Parnaíba/2023) Considerando como verdadeira a sentença “Se Marcos cozinha, então ele não lava 
a louça”, assinale a alternativa que apresenta uma sentença equivalente a esta. 
a) Marcos não cozinha ou não lava a louça. 
b) Marcos não cozinha ou lava a louça. 
c) Se Marcos não lava a louça, então ele cozinha. 
d) Se Marcos lava a louça, então ele cozinha. 
Comentários: 
Sejam as proposições simples: 
c: "Marcos cozinha." 
l: "Marcos lava a louça." 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
12
167


A proposição original pode ser descrita por c→~l: 
c→~l: “Se [Marcos cozinha], então [ele não lava a louça].” 
 
As alternativas apresentam tanto condicionais (se...então; →) quanto disjunções inclusivas (ou; ∨) como 
equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p∨q (transformação da condicional em disjunção inclusiva) 
 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
 
Para o caso em questão, temos: 
c→~l ≡ ~(~l)→~c 
 
A dupla negação de l corresponde à proposição original l. Ficamos com: 
c→~l ≡ l→~c 
 
A proposição equivalente pode ser descrita por: 
l→~c: "Se [Marcos lava a louça], então [ele (Marcos) não cozinha]." 
 
Veja que essa equivalência não está nas alternativas apresentadas. 
Vamos agora utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar o seguinte 
procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (se...então; →) pela disjunção inclusiva (ou; ∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
c→~l ≡ ~c∨~l 
 
A proposição equivalente pode ser descrita por: 
~c∨~l: " [Marcos não cozinha] ou [não lava a louça]." 
Gabarito: Letra A. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
13
167


Transformação disjunção inclusiva (ou) em condicional (se...então) 
A terceira equivalência fundamental para sua prova é a transformação da disjunção inclusiva (ou; ∨) em 
condicional (se...então; →): 
p∨q ≡ ~p→q  
A equivalência é realizada do seguinte modo: 
1. Nega-se o primeiro termo;  
2. Troca-se a disjunção inclusiva (ou; ∨) pela condicional (se...então; →); e 
3. Mantém-se o segundo termo. 
Como exemplo, considere a seguinte disjunção inclusiva: 
p∨q: "[Pedro estuda] ou [Maria trabalha]." 
Observe que a frase seguinte é equivalente: 
~p→q: "Se [Pedro não estuda], então [Maria trabalha]." 
Vamos resolver um exercício envolvendo essa equivalência que acabamos de aprender. 
(EPC/2023) Posso contar com os amigos ou ficarei sozinho. Uma afirmação que é logicamente equivalente a 
afirmação anterior é: 
a) Se não posso contar com os amigos, então ficarei sozinho. 
b) Se posso contar com os amigos, então ficarei sozinho. 
c) Se não posso contar com os amigos, então não ficarei sozinho. 
d) Se ficarei sozinho, então não posso contar com os amigos. 
e) Posso contar com os amigos e ficarei sozinho. 
Comentários: 
Sejam as proposições simples: 
a: "Posso contar com os amigos." 
s: "Ficarei sozinho." 
 
A proposição original pode ser descrita por a∨s: 
a∨s: "[Posso contar com os amigos] ou [ficarei sozinho]." 
 
Sabemos que a disjunção inclusiva (ou; ∨) apresenta uma equivalência fundamental dada por p∨q ≡ ~p→q. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
14
167


• Nega-se o primeiro termo;  
• Troca-se a disjunção inclusiva (ou; ∨) pela condicional (se...então; →); e 
• Mantém-se o segundo termo. 
 
Aplicando essa equivalência para proposição em questão, ficamos com: 
a∨s ≡ ~a→s 
A equivalência obtida é descrita por: 
~a→s: "Se [não posso contar com os amigos], então [ficarei sozinho]." 
Gabarito: Letra A. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
15
167


Negações Lógicas 
Nesse tópico iremos estudar as principais negações lógicas. Antes de apresentarmos as negações, é 
importante que você entenda que uma negação lógica acaba sendo uma equivalência proveniente da 
negação de uma proposição. 
Veremos mais adiante, por exemplo, que a negação de p∧q, que pode ser representada por ~(p∧q), 
corresponde a ~p∨~q. Nesse caso: 
• Podemos dizer que a negação de p∧q é ~p∨~q; 
• Podemos dizer que ~(p∧q) é equivalente a ~p∨~q. 
Ao se construir negação de uma proposição, constrói-se uma nova proposição com valores lógicos sempre 
opostos aos da proposição original. Para o exemplo apresentado, ~p∨~q sempre terá o valor contrário da 
proposição p∧q para todas as linhas da tabela-verdade, conforme pode ser observado a seguir: 
 
Em outras palavras, ~p∨~q terá o valor lógico da negação de p∧q, dada por ~(p∧q), para todas as linhas da 
tabela-verdade: 
 
Veremos a seguir as principais negações que você precisa saber. 
Dupla negação da proposição simples 
Um resultado importante que pode ser obtido da tabela verdade é que a negação da negação de p sempre 
tem valor lógico igual a proposição p, ou seja, é equivalente a p. 
~(~p) ≡ p 
A prova dessa equivalência corresponde à tabela-verdade abaixo. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
16
167


 
Como exemplo, temos que a dupla negação "Não é verdade que [Joãozinho não comeu o chocolate]" é 
equivalente a "Joãozinho comeu o chocolate". 
 
A negação da negação de p é equivalente a p. 
 
~ (~p) ≡ p 
Negação da conjunção e da disjunção inclusiva (Leis de De Morgan) 
Nesse tópico, veremos como se nega a conjunção (e; ∧) e a disjunção inclusiva (ou; ∨). Essas negações são 
conhecidas como Leis de De Morgan. 
Negação da conjunção (e; ∧) 
Para realizar a negação conjunção p∧q, deve-se seguir o seguinte procedimento: 
1. Negam-se ambas as parcelas da conjunção (e; ∧); e 
2. Troca-se a conjunção (e; ∧) pela disjunção inclusiva (ou; ∨). 
Como resultado, podemos dizer que a negação de p∧q, também conhecida por ~(p∧q), é equivalente a 
~p∨~q: 
~(p∧q) ≡ ~p∨~q     
Como exemplo, considere as seguintes proposições simples:  
p: "Comi lasanha." 
q: "Bebi refrigerante." 
A conjunção entre dessas duas proposições pode ser descrita por: 
p∧q: "[Comi lasanha] e [bebi refrigerante]." 
A negação dessa proposição composta é: 
~(p∧q) ≡ ~p∨~q: "[Não comi lasanha] ou [não bebi refrigerante]." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
17
167


Negação da disjunção inclusiva (ou; ∨) 
De modo semelhante à negação da conjunção, para negarmos a disjunção inclusiva p∨q, devemos seguir o 
seguinte procedimento: 
1. Negam-se ambas as parcelas da disjunção inclusiva (ou; ∨); e 
2. Troca-se a disjunção inclusiva (ou; ∨) pela conjunção (e; ∧). 
Como resultado disso, podemos escrever que a negação de p∨q, também conhecida por ~(p∨q), é 
equivalente a ~p∧~q: 
~ (p∨q) ≡ ~p∧~q   
Vejamos um exemplo: 
p∨q: "[Comi lasanha] ou [bebi refrigerante]." 
A negação dessa proposição composta é: 
~(p∨q) ≡ ~p∧~q: "[Não comi lasanha] e [não bebi refrigerante]." 
A seguir temos um mnemônico que resume as duas Leis de De Morgan: 
 
 
Leis de De Morgan 
 
Para negar o "e": negar ambas as proposições e trocar o "e" pelo "ou".  
~(p∧q) ≡ ~p∨~q 
 
Para negar o "ou": negar ambas as proposições e trocar o "ou" pelo "e".  
~(p∨q) ≡ ~p∧~q                 
Vamos agora resolver exercícios envolvendo as Leis de De Morgan. 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
18
167


(AGENERSA/2023) Considere a afirmação: 
“Caminho ou não saio do lugar.” 
Assinale a opção que apresenta sua negação lógica. 
a) Não caminho ou não saio do lugar. 
b) Caminho ou saio do lugar. 
c) Não caminho ou saio do lugar. 
d) Caminho e não saio do lugar. 
e) Não caminho e saio do lugar. 
Comentários: 
Sejam as proposições simples: 
c: "Caminho." 
s: "Saio do lugar." 
 
A proposição original pode ser escrita pela disjunção inclusiva c∨~s:  
c∨~s: "[Caminho] ou [não saio do lugar]." 
 
Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(p∨q) ≡ ~p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da disjunção inclusiva (ou; ∨); e 
• Troca-se a disjunção inclusiva (ou; ∨) pela conjunção (e; ∧). 
 
Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão, 
temos: 
~(c∨~s) ≡ ~c∨~(~s) 
 
A dupla negação da proposição simples s corresponde à proposição original. Ficamos com: 
~(c∨~s) ≡ ~c∨s 
 
Logo, a negação requerida pode ser descrita por:  
~c∨s: “[Não caminho] e [saio do lugar].” 
Gabarito: Letra E. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
19
167


(PM CE/2023) Sabendo-se que não é verdade que o policial militar de serviço pode dormir e pode usar a 
viatura para fins pessoais, é correto afirmar que: 
a) O policial militar de serviço pode dormir ou pode usar a viatura para fins pessoais. 
b) O policial militar de serviço não pode dormir ou não pode usar a viatura para fins pessoais. 
c) O policial militar de serviço pode dormir ou não pode usar a viatura para fins pessoais. 
d) O policial militar de serviço não pode dormir ou pode usar a viatura para fins pessoais. 
e) O policial militar de serviço não pode dormir e não pode usar a viatura para fins pessoais. 
Comentários: 
Sejam as proposições simples: 
d: "O policial militar de serviço pode dormir." 
v: "O policial militar de serviço pode usar a viatura para fins pessoais." 
 
Note que a proposição original pode ser descrita por ~(d∧v): 
~(d∧v): "Não é verdade que [(o policial militar de serviço pode dormir) e ((o policial militar de serviço) 
pode usar a viatura para fins pessoais)]." 
 
Observe que a proposição original, ~(d∧v), é a negação da conjunção (d∧v). Como a questão pergunta por 
algo que é correto de se afirmar, devemos encontrar algo que é equivalente a ~(d∧v), ou seja, devemos 
negar (d∧v). 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção (e; ∧); e 
• Troca-se a conjunção (e; ∧) pela disjunção inclusiva (ou; ∨). 
 
Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão, 
temos: 
~(d∧v) ≡ ~d∨~v 
 
Logo, a negação requerida pode ser descrita por:  
~d∨~v: "[O policial militar de serviço não pode dormir] ou [(o policial militar de serviço) não pode usar a 
viatura para fins pessoais]." 
Gabarito: Letra B. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
20
167
==6306a==


Negação da condicional (se...então) 
A negação de p→q é realizada por meio da seguinte equivalência: 
~(p→q) ≡ p∧~q 
A negação da condicional é realizada do seguinte modo: 
1. Mantém-se o primeiro termo;  
2. Troca-se a condicional (se...então; →) pela conjunção (e; ∧); e 
3. Nega-se o segundo termo. 
Como exemplo, considere a seguinte condicional: 
p→q: "Se [eu comi lasanha], então [eu bebi refrigerante]." 
A negação dessa expressão pode ser escrita como: 
~ (p→q) ≡ p∧~q: "[Eu comi lasanha] e [eu não bebi refrigerante]." 
(DPE SP/2023) Uma afirmação que corresponde a uma negação da lógica da afirmação: 
'Se cada escultura é uma obra de arte, então a chuva é uma grande artista”, é 
a) Se a chuva não é uma grande artista, então cada escultura não é uma obra de arte. 
b) Cada escultura é uma obra de arte ou a chuva é uma grande artista. 
c) Cada escultura não é uma obra de arte ou a chuva não é uma grande artista. 
d) Cada escultura é uma obra de arte, e a chuva não é uma grande artista. 
e) Se cada escultura não é uma obra de arte, então a chuva não é uma grande artista. 
Comentários: 
Sejam as proposições simples: 
o: "Cada escultura é uma obra de arte." 
a: "A chuva é uma grande artista." 
 
A sentença original pode ser descrita por o→a:  
o→a: “Se [cada escultura é uma obra de arte], então [a chuva é uma grande artista]”. 
 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (se...então; →) pela conjunção (e; ∧); e 
• Nega-se o segundo termo. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
21
167


 
Para o caso em questão, temos: 
~(o→a) ≡ o∧~a  
Logo, a negação pode ser descrita por: 
o∧~a: "[Cada escultura é uma obra de arte] e [a chuva não é uma grande artista]." 
Gabarito: Letra D. 
 
(MPE SP/2023) Considere a proposição: 
“Se Maria não sabe Matemática, então ela erra problemas de porcentagem”. 
Assinale a opção que apresenta a negação dessa proposição. 
a) Se Maria sabe Matemática, então ela não erra problemas de porcentagem. 
b) Se Maria não sabe Matemática, então ela não erra problemas de porcentagem. 
c) Se Maria não erra problemas de porcentagem, então ela sabe Matemática. 
d) Maria não sabe Matemática e não erra problemas de porcentagem. 
e) Maria sabe Matemática e erra problemas de porcentagem. 
Comentários: 
Sejam as proposições simples: 
m: "Maria sabe Matemática." 
p: "Maria erra problemas de porcentagem." 
 
A sentença original pode ser descrita por ~m→p:  
~m→p: “Se [Maria não sabe Matemática], então [ela (Maria) erra problemas de porcentagem]”. 
 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (se...então; →) pela conjunção (e; ∧); e 
• Nega-se o segundo termo. 
 
Para o caso em questão, temos: 
~(~m→p) ≡ ~m∧~p  
Logo, a negação pode ser descrita por: 
~m∧~p: "[Maria não sabe Matemática] e [(Maria) não erra problemas de porcentagem]." 
Gabarito: Letra D. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
22
167


Questões com mais de uma equivalência 
Para fins de resolução de questões de concurso público, é importante que você se familiarize com a utilização 
de mais de uma equivalência em um mesmo problema. 
Vamos praticar com algumas questões. 
 
(SEPLAN RR/2023) Considerando os conectivos lógicos usuais, que as letras maiúsculas representam 
proposições lógicas e que o símbolo ~ representa a negação de uma proposição, julgue o item subsecutivo. 
A expressão (A∨B)→C é equivalente à expressão (~A∧~B)∨C. 
Comentários: 
Note que originalmente temos uma condicional cujo antecedente é (A∨B) e cujo consequente é C. Sabemos 
que a condicional apresenta somente duas equivalências: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p∨q (transformação da condicional em disjunção inclusiva) 
 
Como a proposição composta sugerida como equivalente não é uma condicional, vamos utilizar a segunda 
equivalência. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (se...então; →) pela disjunção inclusiva (ou; ∨); e 
• Mantém-se o segundo termo. 
 
Para o caso em questão, temos: 
(A∨B)→C ≡ ~(A∨B)∨C 
 
Note que ~(A∨B) é a negação de (A∨B), podendo ser desenvolvida por De Morgan. Para negar a disjunção 
inclusiva "ou" negam-se as duas proposições e troca-se o "ou" pelo "e". Ficamos com: 
(A∨B)→C ≡ (~A∧~B)∨C 
Gabarito: CERTO. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
23
167


(TJ SP/2023) Em uma reunião, com seus colaboradores, o chefe do atendimento diz: “Se o atendimento é 
bom, então o cliente fica satisfeito e volta”. A alternativa que contém uma afirmação equivalente à afirmação 
do chefe é: 
a) Se o cliente fica satisfeito e volta, então o atendimento é bom. 
b) Se o cliente não fica satisfeito ou não volta, então o atendimento não é bom. 
c) O cliente fica satisfeito ou volta e o atendimento é bom. 
d) Se o cliente não fica satisfeito ou volta, então o atendimento não é bom. 
e) O atendimento é bom e o cliente fica satisfeito e volta. 
Comentários: 
Sejam as proposições simples: 
b: "O atendimento é bom." 
s: "O cliente fica satisfeito." 
v: "O cliente volta." 
 
A sentença original pode ser descrita por b→(s∧v): 
b→(s∧v): “Se [o atendimento é bom], então [(o cliente fica satisfeito) e ((o cliente) volta)].” 
 
Note que originalmente temos uma condicional cujo antecedente é b e cujo consequente é (s∧v). Sabemos 
que a condicional apresenta somente duas equivalências: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p∨q (transformação da condicional em disjunção inclusiva) 
 
Vamos começar utilizando a equivalência contrapositiva: p→q ≡ ~q→~p. Para aplicar essa equivalência, 
devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
 
Para o caso em questão, temos: 
b→(s∧v) ≡ ~(s∧v)→~b: 
 
Note que ~(s∧v) é a negação de (s∧v), podendo ser desenvolvida por De Morgan. Para negar a conjunção 
"e" negam-se as duas proposições e troca-se o "e" pelo "ou". Ficamos com: 
b→(s∧v) ≡ (~s∨~v)→~b: 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
24
167


Note que a proposição obtida como equivalente corresponde à alternativa B, que é o gabarito da questão: 
(~s∨~v)→~b: "Se [(o cliente não fica satisfeito) ou ((o cliente) não volta)], então [o atendimento não é 
bom]." 
 
Para fins didáticos, vamos aplicar a segunda equivalência da condicional, dada por p∨q ≡ ~p→q. Para aplicar 
essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a disjunção inclusiva (ou; ∨) pela condicional (se...então; →); e 
• Mantém-se o segundo termo. 
 
Para o caso em questão, temos: 
b→(s∧v) ≡ ~b∨(s∧v) 
 
Ficamos com a seguinte equivalência: 
~b∨(s∧v): "[O atendimento não é bom] ou [(o cliente fica satisfeito) e ((o cliente) volta)]." 
 
Veja que não temos essa opção nas alternativas. 
Gabarito: Letra B. 
 
(CBM SC/2023) Dentre as alternativas a seguir, aquela que contém a negação lógica da proposição composta 
“Estou doente e, se o médico permite, então viajo” é: 
a) Estou doente e o médico permite e não viajo. 
b) Não estou doente e o médico permite e viajo. 
c) Estou doente ou o médico permite e não viajo. 
d) Não estou doente e o médico permite e não viajo. 
e) Não estou doente ou o médico permite e não viajo. 
Comentários: 
Sejam as proposições simples: 
d: "Estou doente." 
m: "O médico permite." 
v: "Eu viajo." 
 
A sentença original pode ser descrita por d∧(m→v): 
d∧(m→v): “[Estou doente] e, [se (o médico permite), então ((eu) viajo)]” 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
25
167


Devemos negar a sentença original. Note que temos uma conjunção (e; ∧) entre a proposição simples d e a 
condicional (m→v). 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção (e; ∧); 
• Troca-se a conjunção (e; ∧) pela disjunção inclusiva (ou; ∨). 
 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~[d∧(m→v)] ≡ ~d∨~(m→v) 
 
Note que uma das parcelas obtidas, ~(m→v), é a negação da condicional (m→v). 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (se...então; →) pela conjunção (e; ∧); e 
• Nega-se o segundo termo. 
Logo, ficamos com: 
~[d∧(m→v)] ≡ ~d∨(m∧~v) 
 
Logo, a negação requerida corresponde a: 
~d∨(m∧~v): "[Não estou doente] ou [(o médico permite) e (não viajo)]." 
Gabarito: Letra E. 
 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
26
167


Outras equivalências e negações 
Neste tópico, serão apresentadas outras equivalências e negações que, apesar de apresentarem baixa 
incidência, podem aparecer na sua prova. 
Negações da conjunção (e) para a forma condicional (se...então) 
Existem duas maneiras de se negar a conjunção de modo que ela adquira a forma condicional: 
~(p∧q) ≡ p→~q 
~(p∧q) ≡ q→~p 
Considere, por exemplo, a seguinte conjunção: 
p∧q: "[Comi lasanha] e [bebi refrigerante]." 
Além de negar por De Morgan, temos as seguintes possíveis negações de p∧q: 
~(p∧q) ≡ p→~q: "Se [comi lasanha], então [não bebi refrigerante]." 
~(p∧q) ≡ q→~p: "Se [bebi refrigerante], então [não comi lasanha]." 
(MRE/2016) Considere a sentença "Corro e não fico cansado". Uma sentença logicamente equivalente à 
negação da sentença dada é: 
a) Se corro então fico cansado. 
b) Se não corro então não fico cansado. 
c) Não corro e fico cansado. 
d) Corro e fico cansado. 
e) Não corro ou não fico cansado. 
Comentários: 
Sejam as proposições simples: 
c: "Corro." 
f: "Fico cansado." 
 
A proposição original pode ser escrita pela conjunção c∧~f:  
c∧~f: "[Corro] e [não fico cansado]." 
A questão pede pela negação da conjunção (e; ∧) considerada. Em regra, devemos utilizar De Morgan para 
negar uma conjunção. Logo, vamos testar essa possibilidade primeiro.  
 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
27
167


• Negam-se ambas as parcelas da conjunção (e; ∧); e 
• Troca-se a conjunção (e; ∧) pela disjunção inclusiva (ou; ∨). 
 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~(c∧~f) ≡ ~c∨~(~f) 
 
A dupla negação da proposição simples f corresponde à proposição original. Ficamos com: 
~(c∧~f) ≡ ~c∨f 
 
Logo, a negação requerida pode ser descrita por:  
~c∨f: “[Não corro] ou [fico cansado].” 
 
Note que essa possível negação não está presente nas alternativas. Observe, porém, que as alternativas A 
e B apresentam condicionais como a negação da conjunção original. Logo, vamos utilizar as seguintes 
negações da conjunção: 
~(p∧q) ≡ p→~q 
ou 
~(p∧q) ≡ q→~p 
 
Aplicando essas equivalências para o caso em questão, ficamos com: 
~(c∧~f) ≡ c→~(~f) 
ou 
~(c∧~f) ≡ ~f→~c 
 
A dupla negação de f corresponde à proposição original. Ficamos com: 
~(c∧~f) ≡ c→f 
ou 
~(c∧~f) ≡ ~f→~c 
 
Logo, podemos escrever a negação da conjunção c∧~f das seguintes formas: 
~(c∧~f) ≡ c→f: "Se [corro], então [fico cansado]." 
ou 
~(c∧~f) ≡ ~f→~c: "Se [não fico cansado], então [não corro]." 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
28
167


Veja que a primeira possibilidade de se negar a conjunção está presente na alternativa A, que é o gabarito 
da questão. 
Gabarito: Letra A. 
Conjunção de condicionais 
Existem duas equivalências envolvendo conjunção de condicionais que de vez em quando aparecem nas 
provas: 
(p→r)∧(q→r) ≡ (p∨q)→r  
(p→q)∧(p→r) ≡ p→(q∧r) 
 
Quando o termo comum é o consequente, a equivalência apresenta uma disjunção 
inclusiva no antecedente. 
(p→r)∧(q→r) ≡ (p∨q)→r  
Quanto o termo comum é o antecedente, a equivalência apresenta uma conjunção no 
consequente. 
(p→q)∧(p→r) ≡ p→(q∧r) 
(SEFAZ-AL/2020) Considere as proposições: 
• P1: “Se há carência de recursos tecnológicos no setor Alfa, então o trabalho dos servidores públicos que 
atuam nesse setor pode ficar prejudicado.”. 
• P2: “Se há carência de recursos tecnológicos no setor Alfa, então os beneficiários dos serviços prestados 
por esse setor podem ser mal atendidos.”. 
A proposição P1∧P2 é equivalente à proposição “Se há carência de recursos tecnológicos no setor Alfa, então 
o trabalho dos servidores públicos que atuam nesse setor pode ficar prejudicado e os beneficiários dos 
serviços prestados por esse setor podem ser mal atendidos.”. 
Comentários: 
Considere as proposições simples: 
c: "Há carência de recursos tecnológicos no setor Alfa." 
t: "O trabalho dos servidores públicos que atuam nesse setor pode ficar prejudicado." 
b: "Os beneficiários dos serviços prestados por esse setor podem ser mal atendidos." 
 
A proposição P1 pode ser descrita por c→t e a proposição P2 pode ser descrita por c→b. Logo, a proposição 
P1∧P2 pode ser descrita por: 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
29
167


(c→t)∧(c→b) 
Devemos, portanto, avaliar se (c→t)∧(c→b) é equivalente a: 
 
“Se [há carência de recursos tecnológicos no setor Alfa], então [(o trabalho dos servidores públicos que 
atuam nesse setor pode ficar prejudicado) e (os beneficiários dos serviços prestados por esse setor podem 
ser mal atendidos)].” 
 
Isto é, devemos avaliar se (c→t)∧(c→b) é equivalente a c→(t∧b).  
Sabemos que essas duas proposições compostas são equivalentes, pois correspondem à seguinte 
equivalência estudada: 
(p→q)∧(p→r) ≡ p→(q∧r) 
O gabarito, portanto, é CERTO. 
Gabarito: CERTO. 
 
(PF/2004) As proposições (P∨Q)→S e (P→S)∨(Q→S) possuem tabelas de valorações iguais. 
Comentários: 
A assertiva está ERRADA. A equivalência correta seria (P→S)∧(Q→S) ≡ (P∨Q)→S. 
Lembre-se que as equivalências mostradas nesse tópico são conjunções (e; ∧) de condicionais. Veja: 
 (p→r)∧(q→r) ≡ (p∨q)→r 
(p→q)∧(p→r) ≡ p→(q∧r) 
 
Para mostrar formalmente que (P∨Q)→S e (P→S)∨(Q→S) não possuem tabelas de valorações iguais, isto é, 
para mostrar que essas proposições não são equivalentes, podemos montar a seguinte tabela-verdade: 
 
Gabarito: ERRADO.  
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
30
167


Equivalências da disjunção exclusiva (ou...ou) 
Uma forma equivalente de se escrever a disjunção exclusiva (ou...ou; ∨) consiste em negar ambos os 
termos: 
p∨q ≡ (~p)∨(~q) 
Como exemplo, considere a disjunção exclusiva: 
p∨q: "Ou [jogo bola], ou [jogo sinuca]." 
Essa disjunção exclusiva é equivalente a: 
(~p)∨(~q): "Ou [não jogo bola], ou [não jogo sinuca]." 
 
Uma possível equivalência da disjunção exclusiva p∨q consiste em negar tanto p quanto q: 
 
p∨q ≡ (~p)∨(~q) 
Além disso, outras duas possibilidades de se obter equivalências da disjunção exclusiva  consiste em 
transformá-la em uma bicondicional (se e somente se; ) negando-se apenas um dos termos: 
p∨q ≡ (~p)q 
p∨q ≡ p(~q) 
Para fins de exemplo, considere novamente a seguinte disjunção exclusiva: 
p∨q: "Ou [jogo bola], ou [jogo sinuca]." 
Essa disjunção exclusiva também é equivalente às seguintes proposições: 
(~p)q: "[Não jogo bola] se e somente se [jogo sinuca]." 
p(~q): "[Jogo bola] se e somente se [não jogo sinuca]." 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
31
167


 
p∨q ≡ (~p)∨(~q) 
 
p∨q ≡ (~p)q 
 
p∨q ≡ p(~q) 
(TCE SP/2017) Se a afirmação “Ou Renato é o gerente da loja ou Rodrigo é o dono da loja” é verdadeira, 
então uma afirmação necessariamente verdadeira é:  
a) Renato é o gerente da loja e Rodrigo é o dono da loja.  
b) Renato é o gerente da loja se, e somente se, Rodrigo não é o dono da loja.  
c) Se Renato não é o gerente da loja, então Rodrigo não é o dono da loja.  
d) Se Renato é o gerente da loja, então Rodrigo é o dono da loja.  
e) Renato é o gerente da loja. 
Comentários: 
Sejam as proposições simples: 
g: "Renato é o gerente da loja." 
d: "Rodrigo é o dono da loja." 
 
A proposição original pode ser descrita por g∨d: 
g∨d: "Ou [Renato é o gerente da loja] ou [Rodrigo é o dono da loja]." 
 
Temos que procurar nas alternativas uma resposta equivalente a uma disjunção exclusiva. Sabemos que 
existem as seguintes equivalências: 
p∨q ≡ (~p)∨(~q) 
p∨q ≡ (~p)q 
p∨q ≡ p(~q) 
 
Como não há uma disjunção exclusiva nas respostas, devemos testar as últimas duas equivalências. Para o 
caso em questão, temos as seguintes equivalências: 
g∨d ≡ (~g)d 
g∨d ≡ g(~d) 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
32
167


Essas equivalências podem ser descritas por: 
 (~g)d: "[Renato não é o gerente da loja] se, e somente se, [Rodrigo é o dono da loja]." 
g(~d): "[Renato é o gerente da loja] se, e somente se, [Rodrigo não é o dono da loja]." 
 
Veja que g(~d) corresponde à proposição composta que está na letra B, que é o gabarito da questão. 
Gabarito: Letra B. 
Negação da disjunção exclusiva (ou...ou) 
A principal negação da disjunção exclusiva é a bicondicional: 
~(p∨q) ≡ pq 
Como exemplo, considere a seguinte disjunção exclusiva: 
p∨q: "Ou [jogo bola], ou [jogo sinuca]." 
A negação dessa disjunção exclusiva pode ser escrita da seguinte forma: 
~(p∨q) ≡ pq: "[Jogo bola] se e somente se [jogo sinuca]." 
Podemos ainda negar a disjunção exclusiva negando apenas uma das suas parcelas. Veja: 
~(p∨q) ≡ (~p)∨q 
~(p∨q) ≡ p∨(~q) 
Como exemplo, considere novamente a seguinte disjunção exclusiva: 
p∨q: "Ou [jogo bola], ou [jogo sinuca]." 
A negação dessa disjunção exclusiva também pode ser escrita das seguintes formas: 
~(p∨q) ≡ (~p)∨q: "Ou [não jogo bola], ou [jogo sinuca]." 
~(p∨q) ≡ p∨(~q): "Ou [jogo bola], ou [não jogo sinuca]." 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
33
167


 
~(p∨q) ≡ pq 
 
~(p∨q) ≡ (~p)∨q 
 
~(p∨q) ≡ p∨(~q) 
Vamos resolver alguns exercícios relativos à negação da disjunção exclusiva. 
(DPE SP/2023) Considere a seguinte afirmação: 
Ou Flávio é funcionário público ou Flávio é funcionário de empresa privada. 
Assinale a alternativa que contém uma negação lógica para a afirmação apresentada. 
a) Ou Flávio não é funcionário público ou Flávio não é funcionário de empresa privada. 
b) Flávio é funcionário de empresa privada se, e somente se, ele é funcionário público. 
c) Se Flávio é funcionário público, então ele é funcionário de empresa privada. 
d) Flávio é funcionário de empresa privada e é funcionário público. 
e) Flávio é funcionário público ou é funcionário de empresa privada. 
Comentários: 
Sejam as proposições simples: 
p: "Flávio é funcionário público." 
e: "Flávio é funcionário de empresa privada." 
 
A afirmação original é uma disjunção exclusiva (ou...ou) representada por p∨e: 
p∨e: " Ou [Flávio é funcionário público] ou [Flávio é funcionário de empresa privada]." 
 
Conhecemos as seguintes negações da disjunção exclusiva: 
~(p∨q) ≡ pq 
~(p∨q) ≡ (~p)∨q 
~(p∨q) ≡ p∨(~q) 
 
Veja que as alternativas C, D e E podem ser eliminadas, pois a negação da disjunção exclusiva não pode ser 
uma condicional, uma conjunção ou uma disjunção inclusiva. Restam apenas as alternativas A e B. 
Aplicando negações aprendidas para o caso em questão, temos: 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
34
167


~(p∨e) ≡ pe 
~(p∨e) ≡ (~p)∨e 
~(p∨e) ≡ p∨(~e) 
 
Veja que a alternativa A está errada, pois ela nega ambas as parcelas da disjunção exclusiva, apresentando 
a proposição (~p)∨(~e). Essa proposição é uma equivalência de p∨e, não uma negação de p∨e. 
Logo, a alternativa correta é a letra B, que apresenta uma possibilidade para a negação ~(p∨e), dada por 
pe: 
~(p∨e) ≡ pe: "[Flávio é funcionário de empresa privada] se, e somente se, [ele é funcionário público]." 
Gabarito: Letra B. 
 
(CMSJC/2022) Considere a afirmação: "Ou arranjo emprego ou não me caso". A negação dessa afirmação é: 
a) Se eu arranjo emprego, então eu me caso. 
b) Se eu não arranjo emprego, então eu me caso. 
c) Ou não arranjo emprego ou me caso. 
d) Ou não arranjo emprego ou não me caso. 
e) Arranjo emprego e não me caso. 
Comentários: 
Considere as proposições simples: 
a: "Arranjo emprego." 
c: "Me caso." 
 
A afirmação original é uma disjunção exclusiva (ou...ou) representada por a∨~c: 
a∨~c: " Ou [arranjo emprego] ou [não me caso]." 
 
Conhecemos as seguintes negações da disjunção exclusiva: 
~(p∨q) ≡ pq 
~(p∨q) ≡ (~p)∨q 
~(p∨q) ≡ p∨(~q) 
 
Note que nas alternativas não temos nenhuma bicondicional. Portanto, não devemos utilizar essa forma 
de se negar a disjunção exclusiva. 
Utilizando a negação ~(p∨q) ≡ (~p)∨q para o caso em questão, ficamos com: 
~(a∨~c) ≡ ~a∨~c: "Ou [não arranjo emprego] ou [não me caso]." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
35
167


 
Veja que a primeira negação está presente na alternativa D, que é o gabarito da questão. 
Note que o uso da equivalência ~(p∨q) ≡ p∨(~q) também seria possível. Ocorre que, nesse caso, não 
encontramos resposta. Vejamos: 
~(a∨~c) ≡ a∨~(~c) 
 
 A dupla negação de c corresponde à proposição original. Ficamos com: 
~(a∨~c) ≡ a∨c 
 
Logo, a negação poderia ser descrita por: 
~(a∨~c) ≡ a∨c: "Ou [arranjo emprego] ou [me caso]." 
 
Note que essa possibilidade não aparece nas possíveis alternativas. 
Gabarito: Letra D. 
Equivalências da bicondicional (se e somente se) 
Inicialmente, é importante que você saiba que a bicondicional apresenta a seguinte equivalência: 
pq ≡ (p→q)∧(q→p)  
Considere, por exemplo, a seguinte bicondicional pq: 
pq: "[Durmo] se e somente se [estou cansado]" 
Essa bicondicional é equivalente a (p→q)∧(q→p): 
(p→q)∧(q→p): "[Se (estou cansado), então (durmo)] e [se (durmo), então (estou cansado)]". 
Os alunos costumam decorar essa equivalência do seguinte modo: uma forma equivalente à bicondicional é 
ir (p→q) e (∧) voltar (q→p) com a condicional. 
 
pq ≡ (p→q)∧(q→p) 
 
Mnemônico: uma forma equivalente à bicondicional é ir e voltar com a condicional 
Outra forma equivalente de se escrever a bicondicional consiste em negar ambos os termos: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
36
167


pq ≡ (~p)(~q) 
Considere novamente a seguinte bicondicional pq: 
pq: "[Durmo] se e somente se [estou cansado]" 
Essa bicondicional é equivalente a (~p)(~q): 
(~p)(~q): "[Não durmo] se e somente se [não estou cansado]." 
Além disso, outras duas possibilidades de se obter uma equivalência da bicondicional consiste em 
transformá-la em uma disjunção exclusiva (ou...ou; ∨) negando-se apenas um dos termos: 
pq ≡ (~p)∨q 
pq ≡ p∨(~q) 
Para fins de exemplo, considere novamente a seguinte bicondicional: 
pq: "[Durmo] se e somente se [estou cansado]" 
Essa bicondicional também é equivalente às seguintes proposições: 
(~p)∨q: "Ou [não durmo], ou [estou cansado]." 
p∨(~q): " Ou [durmo], ou [não estou cansado]." 
 
pq ≡ (p→q)∧(q→p) 
 
pq ≡ (~p)(~q) 
 
pq ≡ (~p)∨q 
 
pq ≡ p∨(~q) 
Vejamos algumas questões sobre equivalências da bicondicional. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
37
167


(APPGG Pref. SP/2023) Uma proposição lógica equivalente à proposição “Adriano é pai se, e somente se, 
Giuliano é filho” está contida na alternativa: 
a) Se Giuliano não é filho, então Adriano não é pai. 
b) Adriano é pai, e Giuliano não é filho. 
c) Ou Adriano é pai, ou Giuliano é filho. 
d) Se Adriano é pai, então Giuliano é filho. 
e) Ou Giuliano é filho, ou Adriano não é pai. 
Comentários: 
Sejam as seguintes proposições simples: 
a: "Adriano é pai." 
g: "Giuliano é filho." 
 
A proposição original pode ser escrita pela bicondicional ag: 
“[Adriano é pai] se, e somente se, [Giuliano é filho].” 
 
Conhecemos as seguintes equivalências para a bicondicional: 
pq ≡ (p→q)∧(q→p) 
pq ≡ (~p)(~q) 
pq ≡ (~p)∨q 
pq ≡ p∨(~q) 
 
Note que as alternativas A e D podem ser eliminadas, pois são condicionais em que há apenas duas 
proposições simples sem uma conjunção. 
A alternativa B também pode ser eliminada, pois a bicondicional não pode ser equivalente a uma conjunção. 
Logo, restam as alternativas C e E, que são disjunções exclusivas (ou...ou; ∨). Devemos, portanto, aplicar as 
duas últimas equivalências: 
ag ≡ (~a)∨g: "Ou [Adriano não é pai], ou [Giuliano é filho]." 
ag ≡ a∨(~g): " Ou [Adriano é pai], ou [Giuliano não é filho]." 
 
Note que a alternativa C deve ser eliminada, pois ela não negou nenhuma parcela. Essa alternativa 
corresponde a a∨g: 
a∨g: "Ou [Adriano é pai], ou [Giuliano é filho]." 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
38
167


A alternativa correta é a letra E, que apresenta a proposição g∨(~a).  
Ainda nessa aula, em álgebra de proposições, veremos que na disjunção exclusiva podemos trocar 
livremente de posição ambas as parcelas, de modo que a equivalência dada por (~a)∨g corresponde a 
g∨(~a): 
g∨(~a): Ou [Giuliano é filho], ou [Adriano não é pai]. 
Gabarito: Letra E. 
 
(ISS RJ/2010) A proposição "um número inteiro é par se e somente se o seu quadrado for par" equivale 
logicamente à proposição: 
a) se um número inteiro for par, então o seu quadrado é par, e se um número inteiro não for par, então o 
seu quadrado não é par. 
b) se um número inteiro for ímpar, então o seu quadrado é ímpar. 
c) se o quadrado de um número inteiro for ímpar, então o número é ímpar. 
d) se um número inteiro for par, então o seu quadrado é par, e se o quadrado de um número inteiro não for 
par, então o número não é par. 
e) se um número inteiro for par, então o seu quadrado é par. 
Comentários: 
Sejam as proposições: 
p: "Um número inteiro é par." 
q: "O quadrado de um número inteiro é par." 
 
A proposição composta pode ser assim representada: 
pq: "[Um número inteiro é par] se e somente se [o seu quadrado for par]." 
 
Sabemos que uma possível equivalência para a bicondicional é: 
pq ≡ (p→q)∧(q→p) 
 
Não temos alternativa que corresponda a essa última equivalência. Note, porém, que se realizarmos a 
contrapositiva de (q→p), encontramos: 
pq ≡ (p→q)∧(~p→~q) 
Esse resultado pode ser lido como: 
(p→q)∧(~p→~q): "[Se (um número inteiro for par), então (o seu quadrado é par)], e [se (um número 
inteiro não for par), então (o seu quadrado não é par)]." 
Gabarito: Letra A. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
39
167


Negações da bicondicional (se e somente se) 
São quatro as maneiras mais comuns de se negar a bicondicional. A primeira que vamos apresentar é que a 
negação da bicondicional é equivalente à disjunção exclusiva.  
~(pq) ≡ p∨q 
Considere novamente a seguinte bicondicional pq: 
pq: "[Durmo] se e somente se [estou cansado]" 
A negação dessa bicondicional pode ser escrita da seguinte forma: 
~(pq) ≡ p∨q: "Ou [Durmo], ou [estou cansado]" 
Podemos ainda negar a proposição bicondicional negando apenas uma das suas parcelas. Veja: 
~(pq) ≡ (~p)q 
~(pq) ≡ p(~q) 
Como exemplo, considere novamente a seguinte bicondicional: 
pq: "[Durmo] se e somente se [estou cansado]" 
A negação dessa bicondicional também pode ser escrita das seguintes formas: 
~(pq) ≡ (~p)q: "[Não durmo] se e somente se [estou cansado]" 
~(pq) ≡ p(~q): "[Durmo] se e somente se [não estou cansado]" 
Cabe salientar que existe uma outra forma de negação da bicondicional utilizando apenas operadores de 
conjunção e de disjunção inclusiva: 
~ (pq) ≡ (p∧~q)∨(q∧~p) 
 
~ (pq) ≡ p∨q 
~ (pq) ≡ (~p)q 
~ (pq) ≡ p(~q) 
~ (pq) ≡ (p∧~q)∨(q∧~p) 
Vamos resolver alguns exercícios relativos à negação da bicondicional. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
40
167


(CAU TO/2023) Com relação a estruturas lógicas, julgue o item. 
A negação de “A Fênix é imortal se, e somente se, renasce das cinzas” é “Ou a Fênix é imortal ou renasce das 
cinzas”. 
Comentários: 
Sejam as proposições simples: 
i: "A Fênix é imortal." 
r: "A Fênix renasce das cinzas." 
 
A afirmação original é a bicondicional ir: 
ir: "[A Fênix é imortal] se, e somente se, [renasce das cinzas]." 
 
A questão sugere que a negação da bicondicional é uma disjunção exclusiva. Devemos, portanto, utilizar a 
negação ~(pq) ≡ p∨q. Para o caso em questão, temos: 
~(ir) ≡ i∨r 
Ficamos com a seguinte negação: 
~(ir) ≡ i∨r: “Ou [a Fênix é imortal] ou [renasce das cinzas].” 
Gabarito: CERTO. 
 
(Pref. Vila Lângaro/2019) A negação da proposição “João passa no concurso público se e somente se João 
estuda” é: 
a) João não passa no concurso público se e somente se João não estudou. 
b) João não passa no concurso público e João não estudou. 
c) João passa no concurso público e João estuda. 
d) Ou João passa no concurso público ou João estuda. 
e) Se João passa no concurso público, então João estuda. 
Comentários: 
Sejam as proposições simples: 
p: " João passa no concurso público." 
e: " João estuda." 
 
A afirmação original é a bicondicional pe: 
pe: "[João passa no concurso público] se, e somente se, [João estuda]." 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
41
167


As principais formas de se negar a bicondicional são: 
~ (pq) ≡ p∨q 
~ (pq) ≡ (~p)q 
~ (pq) ≡ p(~q) 
~ (pq) ≡ (p∧~q)∨(q∧~p) 
 
Note que a primeira forma de se negar a bicondicional apresentada, quando aplicada para a bicondicional 
pe, corresponde à alternativa D, que é o gabarito da questão: 
~(pe) ≡ p∨e: " Ou [João passa no concurso público] ou [João estuda]." 
 
As demais formas apresentadas nas alternativas não correspondem à negação da bicondicional. Especial 
atenção deve ser dada à alternativa A, que apresenta uma equivalência da bicondicional, não uma negação: 
pe ≡ (~p)(~e) 
Gabarito: Letra D. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
42
167


ÁLGEBRA DE PROPOSIÇÕES 
 
 
 
Todos os conectivos, exceto o condicional (se...então; →), gozam da propriedade comutativa. 
 
p∧q ≡ q∧p 
p∨q ≡ q∨p 
p∨q ≡ q∨p 
pq ≡ qp 
 
 
(p∧q)∧r ≡ p∧(q∧r) 
(p∨q)∨r ≡ p∨(q∨r) 
 
 
p∧(q∨r) ≡ (p∧q) ∨ (p∧r) 
p∨(q∧r) ≡ (p∨q) ∧ (p∨r) 
 
 
p∧t ≡ p 
p∧c ≡ c 
 
p∨t ≡ t 
p∨c ≡ p 
 
 
p∨(p∧q) ≡ p 
p∧(p∨q) ≡ p 
 
 
p∧p ≡ p 
p∨p ≡ p 
 
 
Desenvolver a proposição composta original até se chegar: 
• Em uma tautologia t; ou 
• Em uma contradição c; ou 
• Em uma contingência, que pode ser uma proposição simples p, uma conjunção p∧q, etc. 
 
Bicondicional em problemas de tautologia, contradição e contingência 
XY 
• Se X e Y forem proposições equivalentes, a bicondicional será uma tautologia. 
• Se X e Y forem proposições em que uma é a negação da outra, a bicondicional será uma contradição. 
 
 
Álgebra de proposições 
Propriedade associativa 
Propriedade distributiva 
Propriedade da identidade 
Propriedade da absorção 
Propriedade da idempotência 
Propriedade comutativa 
Álgebra de proposições × tautologia, contradição e contingência 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
43
167


Introdução 
A álgebra de proposições trata do uso sequencial de equivalências lógicas e de outras propriedades para 
simplificar expressões.  
O uso dessa ferramenta é interessante para resolver questões de um modo mais rápido. Além disso, pode 
ser muito útil em questões mais diretas de equivalências lógicas, quando a banca tenta "esconder" a 
equivalência nas alternativas. 
O mais importante é você conhecer as propriedades comutativa, associativa e distributiva e suas aplicações 
mais imediatas nas questões. Isso porque, via de regra, o conhecimento das demais propriedades não 
costuma ser cobrado e, além disso, é comum que as questões mais complexas de álgebra de proposições 
possam ser resolvidas por tabela-verdade.  
Propriedade comutativa 
Todos os conectivos, exceto o condicional (se...então; →), gozam da propriedade comutativa. Isso quer dizer 
que é possível trocar a ordem dos componentes em uma proposição composta sem afetar o resultado da 
tabela-verdade: 
p∧q ≡ q∧p 
p∨q ≡ q∨p 
p∨q ≡ q∨p 
pq ≡ qp 
A seguir temos um exemplo da utilidade da propriedade comutativa em questões de concursos públicos. 
 
Suponha que uma questão peça para você a negação da seguinte condicional: 
p→q: "Se [eu correr], então [chego a tempo]." 
 
Sabemos que essa condicional não goza da propriedade comutativa. A negação dessa condicional, pedida 
pela questão, pode ser encontrada pela seguinte equivalência: 
~ (p→q) ≡ p∧~q: "Corro e não chego a tempo." 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
44
167


Suponha agora que, dentre as alternativas da questão, você não encontre a proposição composta "Corro e 
não chego a tempo", porém encontre "Não chego a tempo e corro". Pode marcar essa alternativa sem medo! 
Isso porque, usando a propriedade comutativa, a conjunção obtida p∧~q pode ser escrita como ~q∧p: 
~ (p→q) ≡ p∧~q ≡ ~q∧p: "Não chego a tempo e corro." 
 
Todos os conectivos, exceto o condicional, comutam: 
 
p∧q ≡ q∧p 
p∨q ≡ q∨p 
p∨q ≡ q∨p 
pq ≡ qp 
 
A condicional p→q não goza da propriedade comutativa.  
p→q e q→p não são equivalentes. 
 
A equivalência correta para a condicional é a contrapositiva: 
  
p→q ≡ ~q→~p 
Propriedade associativa 
Na álgebra elementar, quando realizamos uma multiplicação, é comum ouvirmos a frase "a ordem dos 
fatores não altera o produto". Essa frase resume a propriedade associativa para a multiplicação. 
Vamos supor que queremos realizar a multiplicação 3×5×7. Ela pode ser feita de duas formas: 
• Multiplicamos 3×5 e depois multiplicamos esse resultado por 7, obtendo (3×5)×7; ou 
• Multiplicamos 3 pelo resultado da multiplicação de 5×7, obtendo 3×(5×7). 
Ou seja, na álgebra elementar, a propriedade associativa nos diz que em uma multiplicação de diversos 
termos, podemos realizar as operações de multiplicação na ordem que bem entendermos que o resultado 
será o mesmo: 
(𝟑× 𝟓) × 𝟕= 𝟑× (𝟓× 𝟕) 
O mesmo vale para a adição de termos: 
(𝟑+ 𝟓) + 𝟕= 𝟑+ (𝟓+ 𝟕) 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
45
167


Na álgebra de proposições temos algo muito semelhante. Dizemos que a conjunção (e; ∧) e a disjunção 
inclusiva (ou; ∨) gozam da propriedade associativa, sendo válidas as equivalências: 
(p∧q)∧r ≡ p∧(q∧r) 
(p∨q)∨r ≡ p∨(q∨r) 
 
Observe que a propriedade associativa não mistura em uma mesma expressão o conectivo 
"e" e o conectivo "ou" 
Vamos a um exemplo que mostra uma utilidade para a propriedade associativa. 
(Inédita) Julgue o item a seguir. 
A proposição p∨(q∨~p) é uma tautologia. 
Comentários: 
Nesse tipo de problema, é interessante tentarmos chegar em uma proposição do tipo (p∨~p). Isso porque, 
de acordo com a aula anterior, sabemos que essa proposição é uma tautologia. Originalmente, temos: 
p∨(q∨~p) 
 
Utilizando a propriedade comutativa em (q∨~p), temos: 
p∨(~p∨q) 
 
Utilizando a propriedade associativa na expressão anterior, temos: 
 (p∨~p)∨q 
 
De acordo com a aula anterior, sabemos que (p∨~p) é uma tautologia clássica. Representando a tautologia 
pela letra t, ficamos com: 
t∨q 
 
Observe que a t∨q é a disjunção inclusiva entre um termo que é sempre verdade com a proposição q. 
Sabemos que, para a disjunção inclusiva ser falsa, ambos os termos precisam ser falsos. Logo, como um dos 
termos é sempre verdadeiro, essa disjunção inclusiva é sempre verdadeira. Consequentemente, a 
expressão original é uma tautologia. Podemos escrever: 
p∨(q∨~p) ≡ t 
Gabarito: CERTO. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
46
167


Outra forma de se entender a propriedade associativa é perceber que, quando temos uma sequência só de 
conjunções (e; ∧) ou só de disjunções inclusivas (ou; ∨), podemos remover os parênteses/colchetes. 
(TRT 1/2008) Proposições compostas são denominadas equivalentes quando possuem os mesmos valores 
lógicos V ou F, para todas as possíveis valorações V ou F atribuídas às proposições simples que as compõem. 
Assinale a opção correspondente à proposição equivalente a “~[[A∧(¬B)]→C]”. 
a) A∧(~B)∧(~C) 
b) (~A)∨(~B)∨C 
c) C→[A∧(~B)] 
d) (~A)∨B∨C 
e) [(~A)∧B]→(~C) 
Comentários: 
A proposição original, dada por ~[[A∧(~B)]→C], corresponde à negação de um condicional cujo o 
antecedente é [A∧(~B)] e cujo o consequente é C. 
Para negar uma condicional, utilizamos a equivalência ~(p→q) ≡ p∧~q. Aplicando ao caso em questão, 
devemos manter [A∧(~B)], trocar a condicional pela conjunção e negar C: 
~[[A∧(~B)]→C] ≡ [A∧(~B)]∧(~C) 
Observe que, pela propriedade associativa, a ordem em que é executada a conjunção não importa. Nesse 
caso, podemos remover os colchetes da proposição obtida. Consequentemente, podemos escrever: 
~[[A∧(~B)]→C] ≡ A∧(~B)∧(~C) 
Gabarito: Letra A. 
Propriedade distributiva 
Na álgebra elementar, a propriedade distributiva da multiplicação com relação à adição consiste em realizar 
a seguinte operação: 
3×(5 + 7) = 3 × 5 + 3 × 7 
Da mesma forma, podemos partir do lado direito da equação acima chegar ao lado esquerdo "colocando o 
número 3 em evidência": 
 3 × 5 + 3 × 7 = 3 × (5 + 7) 
Na álgebra de proposições temos as seguintes propriedades distributivas:  
• Da conjunção (e; ∧) com relação à disjunção inclusiva (ou; ∨); e 
• Da disjunção inclusiva (ou; ∨) com relação à conjunção (e; ∧); 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
47
167


Propriedade distributiva da conjunção com relação à disjunção inclusiva 
A propriedade distributiva do conectivo "e" em relação ao "ou" é dada pela equivalência abaixo. Perceba 
que nela "p∧" é distribuído.   
p∧(q∨r) ≡ (p∧q) ∨ (p∧r) 
É importante também reconhecer a propriedade "de trás para frente". Isso significa que podemos colocar o 
termo "p∧" em evidência. 
(p∧q)∨(p∧r) ≡ p∧(q∨r) 
Propriedade distributiva da disjunção inclusiva com relação à conjunção 
A propriedade distributiva do conectivo "ou" em relação ao "e" é dada pela equivalência abaixo. Perceba 
que nela "p∨" é distribuído.   
 p∨(q∧r) ≡ (p∨q)∧(p∨r) 
É importante também reconhecer a propriedade "de trás para frente". Isso significa que podemos colocar o 
termo " p∨" em evidência. 
 (p∨q)∧(p∨r) ≡ p∨(q∧r) 
 
(ISS Fortaleza/2023) P: "Se a pessoa trabalha com o que gosta e está de férias, então é feliz ou está de férias." 
Considerando a proposição P precedente, julgue o item seguinte. 
A proposição P pode ser obtida pela aplicação da propriedade distributiva da conjunção sobre a condicional, 
utilizando-se as proposições "A pessoa está de férias." e "Se a pessoa trabalha com o que gosta, é feliz.". 
Comentários: 
Em lógica de proposições, temos as seguintes propriedades distributivas: 
Propriedade distributiva da conjunção com relação à disjunção inclusiva 
p∧(q∨r) ≡ (p∧q) ∨ (p∧r) 
Propriedade distributiva da disjunção inclusiva com relação à conjunção 
p∨(q∧r) ≡ (p∨q)∧(p∨r) 
 
Não há que se falar em "propriedade distributiva da conjunção sobre a condicional". 
Gabarito: ERRADO. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
48
167


(Pref. Alumínio/2016) Considere a afirmação: Sueli é professora e, pratica ginástica ou pratica corrida. Uma 
afirmação equivalente é 
A) Sueli é professora e pratica ginástica e pratica corrida. 
B) Se Sueli é professora, então ela não pratica ginástica e não pratica corrida. 
C) Sueli é professora e pratica ginástica, ou é professora e pratica corrida. 
D) Se Sueli não pratica ginástica ou não pratica corrida, então ela é professora. 
E) Sueli pratica ginástica e pratica corrida, ou é professora. 
Comentários: 
Sejam as proposições simples: 
s: "Sueli é professora." 
g: "Sueli pratica ginástica." 
k: "Sueli pratica corrida."  
 
Na afirmação do enunciado, a vírgula após o "e" indica parênteses na proposição composta: 
"[Sueli é professora] e, [(pratica ginástica) ou (pratica corrida)]." 
 
Logo, temos a seguinte representação: 
s∧(g∨k) 
 
Por meio da propriedade distributiva, podemos distribuir "s∧”: 
s∧(g∨k) ≡ (s∧g)∨(s∧k) 
 
Temos, portanto, a seguinte equivalência: 
(s∧g)∨(s∧k): "([Sueli é professora] e [pratica ginástica]), ou ([Sueli é professora] e [pratica corrida])" 
 
Essa equivalência corresponde à alternativa C. 
Gabarito: Letra C. 
Cumpre destacar que quando temos um condicional e queremos utilizar a álgebra de proposições para 
resolver alguma questão, é necessário transformar a condicional em disjunção inclusiva por meio da 
seguinte equivalência já conhecida: 
p→q ≡ ~p∨q 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
49
167


Lembre-se, também, que temos como transformar a negação da condicional em uma conjunção: 
~(p→q) ≡ p∧~q 
A seguir, apresentaremos uma questão que pode ser resolvida mais rapidamente utilizando as propriedades 
que vimos até agora. 
 
(MPE RO/2023) Assinale a opção em que é apresentada a proposição lógica equivalente à proposição lógica 
(P→Q)∧(R∨Q).  
a) Q∨(~P∧R)  
b) (P∧R)∨(~Q∨~P)  
c) P→(R∧Q)  
d) ~P→(~Q∧R)  
e) (P→R)∨(~Q→~P) 
Comentários: 
Para resolver essa questão, faz-se necessário utilizar as propriedades que aprendemos até agora de modo a 
desenvolver a proposição composta (P→Q)∧(R∨Q) até se chegar em outra mais simples. 
Veja que, caso não resolvêssemos essa questão por álgebra de proposições, seria necessário construir a 
tabela-verdade de (P→Q)∧(R∨Q) e comparar essa tabela-verdade com as tabelas das outras cinco 
alternativas. 
Feitas essas observações, vamos ao problema. 
Note que temos uma condicional na proposição composta original: (P→Q). Para desenvolver a expressão 
por álgebra de proposições, devemos transformá-la em disjunção inclusiva: ~P∨Q. Logo, a proposição 
original pode ser descrita por: 
(~P∨Q)∧(R∨Q) 
 
Observando o que acabamos de obter, note que, após algumas operações, poderemos colocar "Q∨" em 
evidência, por meio da propriedade distributiva. Antes disso, note que: 
• Aplicando a propriedade comutativa em (~P∨Q), ficamos com (Q∨~P); e 
• Aplicando a propriedade comutativa em (R∨Q), ficamos com (Q∨R). 
Logo, a proposição (~P∨Q)∧(R∨Q) pode ser descrita por: 
(Q∨~P)∧(Q∨R) 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
50
167


Por meio da propriedade distributiva, podemos colocar "Q∨" em evidência: 
Q∨(~P∧R) 
 
Note, portanto, que a proposição original corresponde à proposição apresentada na alternativa A. 
Gabarito: Letra A. 
Propriedade da identidade, da absorção e da idempotência 
 
Trate as propriedades da identidade, da absorção e da idempotência como um "bônus" 
que pode te ajudar em algumas questões mais difíceis. Não se apegue muito a essas 
propriedades, pois elas não costumam aparecer em prova. 
Propriedade da identidade 
Propriedade da identidade para a conjunção 
Sendo t uma tautologia e c uma contradição, temos as seguintes equivalências: 
p∧t ≡ p 
p∧c ≡ c 
Note que p∧t é equivalente a p porque se trata de uma conjunção em que um termo é sempre verdadeiro. 
Isso significa que o valor de p∧t depende somente do valor de p:  
• Se p for verdadeiro, teremos V∧V, que é uma conjunção verdadeira; e 
• Se p for falso, teremos F∧V, que é uma conjunção falsa. 
 
Além disso, p∧c é equivalente a c porque se trata de uma conjunção em que temos um termo sempre falso. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
51
167


 
Propriedade da identidade para a disjunção inclusiva 
Sendo t uma tautologia e c uma contradição, temos as seguintes equivalências: 
p∨t ≡ t 
p∨c ≡ p 
Note que p∨t é uma tautologia t porque se trata de uma disjunção inclusiva em que temos um termo sempre 
verdadeiro: 
 
Além disso, p∨c é equivalente a p porque se trata de uma disjunção inclusiva em que um termo é sempre 
falso. Isso significa que o valor de p∨c depende somente do valor de p:  
• Se p for verdadeiro, teremos V∨F, que é uma disjunção inclusiva verdadeira; e 
• Se p for falso, teremos F∨F, que é uma disjunção inclusiva falsa. 
        
 
(ANPAD/2014) A proposição composta p∧(q∨(~p)) é logicamente equivalente à proposição 
a) q 
b) p∧q 
c) p∨q 
d) p∧(~q) 
e) p∨(~q) 
Comentários: 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
52
167


Aplicado a propriedade distributiva em "p∧", temos: 
p∧(q∨~p) ≡ (p∧q)∨(p∧~p) 
 
Conforme visto na aula anterior, (p∧~p) é uma contradição. Logo, ficamos com: 
(p∧q)∨c 
 
Veja que temos uma disjunção inclusiva entre (p∧q) e uma contradição c. Essa disjunção inclusiva é 
equivalente a (p∧q), pois se trata de uma disjunção inclusiva em que um termo é sempre falso (propriedade 
da identidade para a disjunção inclusiva). Logo, ficamos com: 
(p∧q) 
Gabarito: Letra B.           
Propriedade da absorção 
A propriedade da absorção é representada por duas equivalências: 
p∨(p∧q) ≡ p 
p∧(p∨q) ≡ p 
Essas equivalências são demonstráveis por tabela-verdade: 
           
           
(SEFAZ-MS/2006) Representando por ~r a negação de uma proposição r, a negação de p∧(p∨q) é 
equivalente a:  
a) ~p.   
b) ~q.  
c) ~(p∨q).  
d) ~(p∧q).  
e) uma contradição. 
Comentários: 
Pela propriedade da absorção, sabemos que p∧(p∨q) ≡ p. Logo, a negação pedida é ~p. 
Gabarito: Letra A. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
53
167


Propriedade da idempotência 
A propriedade da idempotência é representada por duas equivalências: 
p∧p ≡ p 
p∨p ≡ p 
 Note que o valor lógico da conjunção p∧p depende exclusivamente da proposição p, pois: 
• Se p for verdadeiro, p∧p será verdadeiro, pois será uma conjunção entre dois termos verdadeiros; e 
• Se p for falso, p∧p será falso, pois será uma conjunção entre dois termos falsos 
Além disso, o valor lógico da disjunção inclusiva p∨p também depende exclusivamente da proposição p, pois: 
• Se p for verdadeiro, p∨p será verdadeiro, pois será uma disjunção inclusiva entre dois termos 
verdadeiros; e 
• Se p for falso, p∨p será falso, pois será uma disjunção inclusiva entre dois termos falsos. 
Para que não reste dúvidas, as equivalências são demonstráveis por tabela-verdade:  
                  
 
(DPEN/2013) Considerando que, P, Q e R são proposições conhecidas, julgue o próximo item. 
A proposição ¬[(P → Q)∨Q] é equivalente à proposição P∧(¬Q), em que ¬P é a negação de P. 
Comentários: 
Primeiramente, vale perceber que essa questão pode ser resolvida por tabela-verdade. Isso porque, para 
duas proposições serem equivalentes, basta que elas apresentem a mesma tabela-verdade. 
Dito isso, vamos resolver a questão por álgebra de proposições. A nossa estratégia será partir de 
~[(P→Q)∨Q] para chegar em P∧(~Q). 
 
Veja que ~[(P→Q)∨Q] é a negação da disjunção inclusiva entre (P→Q)  e Q. Vamos desenvolver essa negação 
por De Morgan, negando ambas as parcelas e trocando "ou" por "e". Ficamos com: 
~(P→Q)∧~Q 
 
Para negar uma condicional, utilizamos a seguinte equivalência: ~(p→ q) ≡ p∧~ q. Ficamos com: 
[P∧~Q]∧~Q 
 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
54
167


Pela propriedade associativa, podemos escrever: 
P∧[~Q∧~Q] 
 
Observe que, pela propriedade idempotente, [~Q∧~Q] apresenta sempre o valor lógico de ~Q. Isso porque 
quando ~Q é V, [~Q∧~Q] é V, e quando ~Q é F, [~Q∧~Q] é F. Logo, nossa conjunção fica assim: 
P∧(~Q) 
Gabarito: CERTO. 
Álgebra de proposições × tautologia, contradição e contingência  
Você se lembra que um dos métodos para descobrirmos se uma proposição composta é uma tautologia, 
uma contradição ou uma contingência é utilizar equivalências lógicas ou álgebra de proposições? 
Esse método costuma ser o mais rápido, porém requer o domínio das equivalências lógicas e das 
propriedades da álgebra de proposições.  
A ideia consiste basicamente em desenvolver a proposição composta original até se chegar: 
• 
Em uma tautologia t; ou 
• 
Em uma contradição c; ou 
• 
Em uma contingência, que pode ser uma proposição simples p, uma conjunção p∧q, etc. 
 
(STJ/2018) A proposição ¬P→(P→Q), em que ¬P denota a negação da proposição P, é uma tautologia, isto é, 
todos os elementos de sua tabela-verdade são V (verdadeiro). 
Comentários: 
Note que originalmente temos a condicional ~P→ (P→Q), cujo antecedente é ~P e cujo consequente é outra 
condicional, dada por (P→Q).  
Utilizando a equivalência p→q ≡ ~p∨q, ficamos com: 
~(~P)∨(P→Q) 
 
A dupla negação de P corresponde à proposição simples P. Ficamos com: 
P∨(P→Q) 
 
Utilizando novamente a equivalência p→q ≡ ~p∨q para a condicional (P→Q), ficamos com: 
P∨(~P∨Q) 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
55
167


Utilizando a propriedade associativa, temos: 
(P∨~P)∨Q 
 
P∨~P é uma tautologia. Ficamos com: 
t∨Q 
 
Veja que temos uma disjunção inclusiva entre uma tautologia t e uma proposição simples Q. Essa disjunção 
inclusiva é sempre verdadeira, pois um dos termos dela (tautologia t) sempre será verdadeiro (propriedade 
da identidade para a disjunção inclusiva). Logo, a proposição original corresponde a uma tautologia: 
t 
Gabarito: CERTO. 
 
(CBM AL/2017) A respeito de proposições lógicas, julgue o item a seguir. 
Se P e Q forem proposições simples, então a proposição composta Q∨(Q→P) é uma tautologia. 
Comentários: 
Temos a seguinte proposição composta: 
Q∨(Q → P)  
 
Utilizando a equivalência p→q ≡ ~p∨q para a condicional (Q→P), ficamos com: 
Q∨(~Q∨P) 
 
Utilizando a propriedade associativa, temos: 
(Q∨~Q)∨P  
 
Q∨~Q é uma tautologia. Ficamos com: 
t∨P 
 
Veja que temos uma disjunção inclusiva entre uma tautologia t e uma proposição simples P. Essa disjunção 
inclusiva é sempre verdadeira, pois um dos termos dela (tautologia t) sempre será verdadeiro (propriedade 
da identidade para a disjunção inclusiva). Logo, a proposição original corresponde a uma tautologia: 
t 
Gabarito: CERTO. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
56
167


Bicondicional em problemas de tautologia, contradição e contingência 
Um problema muito explorado pelas bancas de concurso público consiste em perguntar se uma determinada 
bicondicional é uma tautologia ou uma contradição. 
Quanto ao conectivo bicondicional, sabemos que: 
• A bicondicional é verdadeira quando ambas as parcelas tiverem o mesmo valor lógico; e 
• A bicondicional é falsa quando ambas as parcelas tiverem valores lógicos contrários. 
Considere a seguinte bicondicional cujas parcelas são duas proposições compostas X e Y: 
XY 
Note que: 
• Se X e Y forem proposições equivalentes, ambas as parcelas terão sempre o mesmo valor lógico. 
Nesse caso, a bicondicional será sempre verdadeira, ou seja, a bicondicional será uma tautologia. 
• Se X e Y forem proposições em que uma é a negação da outra, ambas as parcelas terão sempre 
valores lógicos contrários. Nesse caso, a bicondicional será sempre falsa, ou seja, a bicondicional será 
uma contradição. 
 
(POLC AL/2023) Considere os conectivos lógicos usuais e assuma que as letras maiúsculas representam 
proposições lógicas simples. Com base nessas informações, julgue o item seguinte relativo à lógica 
proposicional. 
A proposição lógica (P→Q)((~P)∨Q) é uma tautologia. 
Comentários: 
Originalmente, temos a seguinte bicondicional: 
(P→Q)((~P)∨Q) 
 
Utilizando a equivalência p→q ≡ ~p∨q para a condicional (P→Q), obtemos ((~P)∨Q). Logo, a bicondicional 
original pode ser descrita por: 
 ((~P)∨Q)((~P)∨Q) 
 
Veja que a bicondicional original corresponde a uma bicondicional em que as duas parcelas são iguais. Logo, 
ambas as parcelas da bicondicional sempre vão apresentar o mesmo valor lógico. Consequentemente, a 
bicondicional sempre será verdadeira. Trata-se, portanto, de uma tautologia. 
Gabarito: CERTO 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
57
167
==6306a==


(Pref Acrelândia/2022) A proposição (P∧Q)(∼P∨∼Q) representa uma afirmativa que podemos chamar de: 
a) contingência. 
b) tautologia. 
c) implicação lógica. 
d) contradição. 
e) paradoxo. 
Comentários: 
Originalmente, temos a seguinte bicondicional: 
(P∧Q)(∼P∨∼Q) 
 
Note que o segundo termo da bicondicional, (~P∨~Q), é a negação do primeiro termo (P∧Q). Isso porque, 
por De Morgan, temos: 
(P∧Q) ≡ (~P∨~Q) 
 
Logo, a bicondicional em questão pode ser escrita do seguinte modo: 
(P∧Q)~(P∧Q) 
 
Veja que a bicondicional original corresponde a uma bicondicional em que as duas parcelas são uma a 
negação da outra. Logo, ambas as parcelas da bicondicional sempre vão apresentar valores lógicos distintos. 
Consequentemente, a bicondicional sempre será falsa. Trata-se, portanto, de uma contradição. 
Gabarito: Letra D. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
58
167


 
QUESTÕES COMENTADAS - MULTIBANCAS 
Equivalências Lógicas 
 
As questões estão divididas por banca: 
• Outras Bancas 
• FGV 
• CEBRASPE 
• FCC 
• VUNESP 
Dentro de cada banca, caso seja aplicável para ela, podemos ter os seguintes tópicos, 
conforme a teoria da aula: 
• Equivalências fundamentais 
• Negações lógicas 
• Questões com mais de uma equivalência 
• Outras equivalências e negações 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
59
167


 
Outras Bancas 
Outras Bancas - Equivalências Fundamentais 
(QUADRIX/Novacap/2024) As proposições “Se Gabriela cantou, então Jacqueline não cantou” e “Ou 
Gabriela cantou ou Jacqueline cantou” são equivalentes.  
Comentários: 
Sabemos que uma condicional só pode ser equivalente a outra condicional ou a uma disjunção inclusiva, 
por meio das seguintes equivalências: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Como a questão apresenta uma disjunção exclusiva (ou...ou) como possível equivalência, o gabarito do 
item é ERRADO. 
Para fins didáticos, vamos mostrar as possíveis equivalências da condicional. Considere as seguintes 
proposições simples: 
g: "Gabriela cantou." 
j: "Jaqueline cantou." 
Note que a condicional presente na questão pode ser descrita por g→~j: 
g→~j: "Se [Gabriela cantou], então [Jacqueline não cantou]." 
Utilizando a equivalência contrapositiva, ficamos com: 
g→~j ≡ ~(~j)→~g 
A dupla negação de j corresponde à proposição original. Ficamos com: 
g→~j ≡ j→~g 
Logo, temos a seguinte equivalência: 
j→~g: "Se [Jaqueline cantou], então [Gabriela não cantou]." 
Vamos agora utilizar a transformação da condicional em disjunção inclusiva. Para aplicar essa 
equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
60
167


 
Para o caso em questão, temos: 
g→~j ≡ ~g∨~j 
Logo, temos a seguinte equivalência: 
~g∨~j: "[Gabriela não cantou] ou [Jacqueline não cantou]." 
Observe, portanto, que as equivalências obtidas, j→~g e ~g∨~j, não correspondem à disjunção exclusiva 
sugerida na questão, que pode ser descrita por g∨j: 
g∨j:" Ou [Gabriela cantou] ou [Jacqueline cantou]." 
Gabarito: ERRADO. 
 
(Instituto AOCP/PM PE/2024) Se Carlos mentiu sobre sua aprovação no concurso para a Polícia Militar 
de Pernambuco, então será criticado por sua família nas festas de final de ano. Logo, para a lógica, 
a) Carlos será criticado por sua família nas festas de final de ano. 
b) se Carlos não mentiu sobre sua aprovação no concurso para a Polícia Militar de Pernambuco, então não 
será criticado por sua família nas festas de final de ano. 
c) Carlos mentiu sobre sua aprovação no concurso para a Polícia Militar de Pernambuco. 
d) se Carlos não foi criticado por sua família nas festas de final de ano, então não mentiu sobre sua 
aprovação no concurso para a Polícia Militar de Pernambuco. 
e) se Carlos foi criticado por sua família nas festas de final de ano, então mentiu sobre sua aprovação no 
concurso para a Polícia Militar de Pernambuco. 
Comentário: 
Sejam as proposições simples: 
m: "Carlos mentiu sobre sua aprovação no concurso para a Polícia Militar de Pernambuco." 
f: "Carlos será criticado por sua família nas festas de final de ano." 
A proposição original pode ser descrita por m→f: 
m→f: "Se [Carlos mentiu sobre sua aprovação no concurso para a Polícia Militar de Pernambuco], então 
[(Carlos) será criticado por sua família nas festas de final de ano]." 
Existem duas possíveis equivalências para a condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
61
167


 
Veja que em nenhuma alternativa temos uma disjunção inclusiva "ou". Logo, devemos utilizar a 
equivalência contrapositiva. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
m→f ≡ ~f→~m 
Logo, a proposição equivalente pode ser escrita por: 
~f→~m: "Se [Carlos não foi criticado por sua família nas festas de final de ano], então [(Carlos) não mentiu 
sobre sua aprovação no concurso para a Polícia Militar de Pernambuco]." 
Gabarito: Letra D. 
 
(Instituto Verbena/IFS/2024) Considere a proposição P referente aos números naturais. 
P: se n2 é par, então n é par. 
Sua contrapositiva é: 
a) se n não é par, então n2 é ímpar. 
b) se n não é par, então n2 é par. 
c) se n é par, então n2 não é ímpar. 
d) se n2 não é par, então n2 é ímpar. 
Comentários: 
Sejam as sentenças: 
p: "n2 é par." 
q: "n é par." 
Note que P pode ser descrita pela condicional p→q: 
p→q: "Se [n2 é par], então [n é par]." 
Devemos utilizar a equivalência contrapositiva, que é representada do seguinte modo: p→q ≡ ~q→~p. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
62
167


 
Logo, a equivalência pode ser descrita por: 
~q→~p: "Se [n não é par], então [n2 não é par]." 
Note que um número natural só pode ser ou par ou ímpar, de modo que "é ímpar" corresponde ao termo 
"não é par". Em outras palavras, "par" é negado corretamente pelo seu antônimo "ímpar". Portanto, 
podemos escrever: 
~q→~p: "Se [n não é par], então [n2 é impar]." 
Gabarito: Letra A.  
 
 (IBFC/IBGE/2022) De acordo com a proposição lógica a frase “Se o coordenador realizou a previsão 
orçamentária, então o trabalho foi realizado com sucesso” é equivalente a frase: 
a) Se o coordenador não realizou a previsão orçamentária, então o trabalho não foi realizado com sucesso 
b) O coordenador realizou a previsão orçamentária e o trabalho foi realizado com sucesso 
c) O coordenador realizou a previsão orçamentária ou o trabalho foi realizado com sucesso 
d) Se o trabalho não foi realizado com sucesso, então o coordenador não realizou a previsão orçamentária 
e) Se o trabalho foi realizado com sucesso, então o coordenador realizou a previsão orçamentária 
Comentários: 
Sejam as proposições simples: 
p: "O coordenador realizou a previsão orçamentária." 
s: "O trabalho foi realizado com sucesso." 
A proposição original pode ser descrita por p→s: 
p→s: "Se [o coordenador realizou a previsão orçamentária], então [o trabalho foi realizado com sucesso]." 
As alternativas apresentam tanto condicionais (→) quanto uma disjunção inclusiva ("ou", ∨) como 
equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
63
167


 
p→s ≡ ~s→~p 
A proposição equivalente pode ser descrita por: 
~s→~p: "Se [o trabalho não foi realizado com sucesso], então [o coordenador não realizou a previsão 
orçamentária]." 
O gabarito, portanto, é a alternativa D. 
Para fins didáticos, vamos utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar 
o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
p→s ≡ ~p∨s 
A proposição equivalente pode ser descrita por: 
~p∨s: "[O coordenador não realizou a previsão orçamentária] ou [o trabalho foi realizado com sucesso]." 
Veja que essa equivalência não aparece nas alternativas. 
Gabarito: Letra D. 
 
(QUADRIX/CRT MG/2022) A proposição “Quem tem boca vai a Roma” é equivalente à proposição “Não 
tem boca ou vai a Roma”. 
Comentários: 
Sejam as proposições simples: 
b: "Alguém tem boca." 
r: "Alguém vai a Roma." 
Note que a proposição "Quem [tem boca], [vai a Roma]" apresenta o mesmo sentido da condicional b→r: 
b→r: "Se [alguém tem boca], então [esse alguém vai a Roma]." 
A equivalência sugerida pelo item é uma disjunção inclusiva "ou". Devemos, portanto, utilizar a 
equivalência da transformação da condicional em disjunção inclusiva, dada por p→q ≡ ~p∨q. Para o caso 
em questão, temos: 
b→r ≡ ~b∨r 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
64
167


 
Logo, a proposição original é equivalente a: 
~b∨r: "(Alguém não tem boca) ou (esse alguém vai a Roma)." 
Essa proposição equivalente pode ser entendida por “(Não tem boca) ou (vai a Roma)”. O gabarito, 
portanto, é CERTO. 
Gabarito: CERTO. 
 
(Instituto AOCP/PC PA/2021) Considere a seguinte sentença: “O circuito A não possui escala de 
integração SSI ou o circuito B possui escala de integração LSI”. Uma afirmação logicamente equivalente a 
essa sentença dada é: 
a) “Se o circuito A não possui escala de integração SSI, então o circuito B possui escala de integração LSI”. 
b) ”Se o circuito A possui escala de integração SSI, então o circuito B possui escala de integração LSI”. 
c) ”Se o circuito A possui escala de integração SSI, então o circuito B não possui escala de integração LSI”. 
d) ”Se o circuito A não possui escala de integração SSI, então o circuito B não possui escala de integração 
LSI”. 
e) “Se o circuito B possui escala de integração LSI, então o circuito A possui escala de integração SSI”. 
Comentários: 
Sejam as proposições simples: 
a: "O circuito A possui escala de integração SSI." 
b: "O circuito B possui escala de integração LSI." 
A proposição composta original pode ser descrita por ~a∨b:  
~a∨b: "[O circuito A não possui escala de integração SSI] ou [o circuito B possui escala de integração LSI]." 
Uma equivalência fundamental que envolve a disjunção inclusiva é a transformação da disjunção inclusiva 
em condicional, dada por p∨q ≡ ~p→q. Essa equivalência é aplicada do seguinte modo: 
• Nega-se o primeiro termo; 
• Troca se a disjunção inclusiva (∨) pela condicional (→); 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
~a∨b ≡ ~(~a)→b 
A dupla negação da proposição simples a corresponde à proposição original. Ficamos com: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
65
167


 
~a∨b ≡ a→b 
Logo, temos a seguinte equivalência: 
a→b: "Se [o circuito A possui escala de integração SSI], então [o circuito B possui escala de integração LSI]." 
Gabarito: Letra B. 
 
Outras Bancas - Negações Lógicas 
(QUADRIX/Novacap/2024) A negação da proposição “Se Carolina dançou, Ana cantou” é “Se Ana não 
cantou, então Carolina não dançou”.  
Comentários: 
Sejam as proposições simples: 
c: "Carolina dançou." 
a: "Ana cantou." 
A proposição original pode ser descrita por c→a:  
c→a: “Se [Carolina dançou], então [Ana cantou]”. 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(c→a) ≡ c∧~a 
Logo, a negação pode ser descrita por: 
c∧~a: "[Carolina dançou] e [Ana não cantou]." 
O gabarito, portanto, é ERRADO. 
Cumpre destacar que a negação de uma condicional nunca corresponderá a outra condicional. Note que 
a questão apresenta a equivalência contrapositiva da condicional original como se fosse a negação: 
c→a ≡ ~a→~c: "Se [Ana não cantou], então [Carolina não dançou]." 
Gabarito: ERRADO. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
66
167


 
(CONSULPLAM/ISS BH/2024) Uma acareação de um desvio de conduta em uma empresa chegou a um 
suspeito que, em um primeiro momento, deu a seguinte declaração: “O computador estava sem internet 
ou a porta emperrou”. Pela fala, identificou-se que o suspeito estava mentindo. Isto é, 
a) O computador estava sem internet e a porta emperrou. 
b) O computador estava com internet ou a porta não emperrou. 
c) O computador estava com internet e a porta não emperrou. 
d) O computador estava sem internet ou a porta não emperrou. 
e) O computador estava com internet e a porta emperrou. 
Comentários: 
Sejam as proposições simples: 
c: "O computador estava com internet." 
p: "A porta emperrou." 
Para resolver o problema, consideraremos que o computador pode estar ou com internet ou sem internet, 
sem haver meio termo. Logo, a negação da proposição c pode ser descrita por: 
~c: "O computador estava sem internet." 
Note que a declaração original pode ser descrita por ~c∨p: 
~c∨p:“[O computador estava sem internet] ou [a porta emperrou].” 
Note que, como o suspeito estava mentindo, é correto concluir a negação da declaração dele. Devemos, 
portanto, negar ~c∨p. 
Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(p∨q) ≡ ~p∧~q. Para aplicar 
essa equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da disjunção inclusiva; 
• Troca-se a disjunção inclusiva (∨) pela conjunção (∧). 
Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão, 
temos: 
 
 
~c∨p ≡ ~(~c)∧~p 
A dupla negação de c corresponde à proposição original c. Ficamos com: 
~c∨p ≡ c∧~p 
Logo, a negação procurada é: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
67
167


 
c∧~p: “[O computador estava com internet] e [a porta não emperrou]”. 
Gabarito: Letra C. 
 
(CONSULPLAM/ISS BH/2024) Sabe-se que a negação de uma sentença r é denotada por ¬r. Uma 
proposição equivalente a (¬p) ∧ (¬q) é:  
a) ¬p→¬q 
b) pq 
c) q↛p 
d) p∨q 
e) ¬(p∨q) 
Comentários: 
Queremos obter uma proposição equivalente a ~p∧~q.  
Por meio de De Morgan, sabemos que a negação da disjunção inclusiva p∨q, ou seja, ~(p∨q), é 
equivalente a ~p∧~q: 
~(p∨q) ≡ ~p∧~q 
Em outras palavras, ~p∧~q é equivalente a ~(p∨q). 
Gabarito: Letra E. 
 
(AOCP/SEAP PR/2024) Considere a proposição P: “Se Marlene é economista, então Marlene avalia 
pesquisas na área econômica do Poder Executivo Estadual”. Se Orlando tem conhecimentos apurados de 
raciocínio lógico e afirma que a proposição P é falsa, então, para Orlando, é correto afirmar que 
a) Marlene não é economista e Marlene não avalia pesquisas na área econômica do Poder Executivo 
Estadual. 
b) se Marlene não avalia pesquisas na área econômica do Poder Executivo Estadual, então Marlene não é 
economista. 
c) Marlene é economista e Marlene não avalia pesquisas na área econômica do Poder Executivo Estadual. 
d) Marlene não é economista ou Marlene avalia pesquisas na área econômica do Poder Executivo Estadual. 
e) Marlene avalia pesquisas na área econômica do Poder Executivo Estadual. 
Comentários: 
Sejam as proposições simples: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
68
167


 
e: “Marlene é economista.” 
a: “Marlene avalia pesquisas na área econômica do Poder Executivo Estadual.” 
Note que a proposição P pode ser descrita pela condicional e→a: 
e→a: “Se [Marlene é economista], então [Marlene avalia pesquisas na área econômica do Poder Executivo 
Estadual]” 
A questão informa que a proposição e→a é falsa. Logo, a sua negação é verdadeira. Devemos, portanto, 
negar a condicional e→a. 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(e→a) ≡ e∧~a 
Logo, a negação pode ser descrita por: 
e∧~a: "[Marlene é economista] e [Marlene não avalia pesquisas na área econômica do Poder Executivo 
Estadual]." 
Gabarito: Letra C. 
 
(FUNDATEC/ALE RS/2024) Considere a proposição lógica dada por: 
“Antônio é profissional de Tecnologia da Informação ou de Jornalismo”. 
 A negação desta proposição é: 
a) Antônio não é profissional de Tecnologia da Informação. 
b) Antônio não é profissional de Tecnologia da Informação, mas é de Jornalismo 
c) Antônio é profissional de Tecnologia da Informação, mas não é de Jornalismo. 
d) Antônio não é profissional de Tecnologia da Informação nem de Jornalismo. 
e) Antônio não é profissional de Jornalismo. 
Comentários: 
Sejam as proposições simples: 
t: "Antônio é profissional de Tecnologia da Informação." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
69
167


 
j: "Antônio é profissional de Jornalismo." 
A proposição original pode ser descrita por t∨j: 
t∨j: "[Antônio é profissional de Tecnologia da Informação] ou [(Antônio é profissional) de Jornalismo]." 
Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(p∨q) ≡ ~p∧~q. Para aplicar 
essa equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da disjunção inclusiva; 
• Troca-se a disjunção inclusiva (∨) pela conjunção (∧). 
Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão, 
temos: 
~(t∨j) ≡ ~t∧~j 
Logo, a negação requerida pode ser descrita por: 
~t∧~j: "[Antônio não é profissional de Tecnologia da Informação] e [Antônio não é profissional de 
Jornalismo]". 
Substituindo "e não" pelo termo "nem" e omitindo redundâncias da linguagem escrita, temos: 
~t∧~j: "[Antônio não é profissional de Tecnologia da Informação] nem [de Jornalismo]". 
Gabarito: Letra D. 
 
 (FUNDATEC/ALE RS/2024) Considere a proposição abaixo. 
“Jairo não é formado em exatas e Marcia é formada em humanas”. 
A negação lógica da proposição acima é dada por: 
a) Jairo é formado em exatas e Márcia também. 
b) Jairo é formado em exatas ou Márcia não é formada em humanas. 
c) Jairo é formado em exatas ou Márcia também. 
d) Jairo não é formado em humanas ou Márcia é. 
e) Jairo é formado em exatas e Márcia não é formada em humanas. 
Comentários: 
Sejam as proposições simples: 
j: "Jairo é formado em exatas." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
70
167


 
m: "Marcia é formada em humanas." 
A proposição original pode ser escrita pela conjunção ~j∧m:  
~j∧m: “[Jairo não é formado em exatas] e [Marcia é formada em humanas].” 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~(~j∧m) ≡ ~(~j)∨~m 
A dupla negação de j corresponde à proposição original j. Ficamos com: 
~(~j∧m) ≡ j∨~m 
Logo, a negação requerida pode ser descrita por:  
j∨~m: "[Jairo é formado em exatas] ou [Márcia não é formada em humanas]." 
Gabarito: Letra B. 
 
(IBFC/PCP PR/2024) A negação lógica da frase “Hoje é domingo e não trabalharei” é dada por: 
a) hoje é domingo e trabalharei 
b) hoje não é domingo e trabalharei 
c) hoje não é domingo e não trabalharei 
d) hoje não é domingo ou trabalharei 
e) hoje é domingo ou trabalharei 
Comentários: 
Sejam as proposições simples: 
d: "Hoje é domingo." 
t: "Trabalharei." 
A proposição original pode ser escrita pela conjunção d∧~t:  
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
71
167


 
d∧~t: “[Hoje é domingo] e [não trabalharei].” 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~(d∧~t) ≡ ~d∨~(~t) 
A dupla negação de t corresponde à proposição original t. Ficamos com: 
~(d∧~t) ≡ ~d∨t 
Logo, a negação requerida pode ser descrita por:  
~d∨t: "[Hoje não é domingo] ou [trabalharei]." 
Gabarito: Letra D. 
 
Outras Bancas - Questões com mais de uma equivalência 
(IBFC/IBGE/2022) De acordo com a proposição lógica a frase “O agente censitário não transcreveu o 
texto em planilha eletrônica ou o trabalho foi realizado com sucesso” é equivalente a frase: 
a) Se o agente censitário não transcreveu o texto em planilha eletrônica, então o trabalho não foi realizado 
com sucesso 
b) O agente censitário transcreveu o texto em planilha eletrônica e o trabalho não foi realizado com 
sucesso 
c) O agente censitário transcreveu o texto em planilha eletrônica ou o trabalho não foi realizado com 
sucesso 
d) Se o trabalho foi realizado com sucesso, então o coordenador não realizou a previsão orçamentária 
e) Se o trabalho não foi realizado com sucesso, então o agente censitário não transcreveu o texto em 
planilha eletrônica 
Comentários: 
Sejam as proposições simples: 
p: "O agente censitário transcreveu o texto em planilha eletrônica." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
72
167


 
s: "O trabalho foi realizado com sucesso." 
A proposição composta original pode ser descrita por ~p∨s:  
~p∨s: "[O agente censitário não transcreveu o texto em planilha eletrônica] ou [o trabalho foi realizado 
com sucesso]." 
Uma equivalência fundamental que envolve a disjunção inclusiva é a transformação da disjunção inclusiva 
em condicional, dada por p∨q ≡ ~p→q. Essa equivalência é aplicada do seguinte modo: 
• Nega-se o primeiro termo; 
• Troca se a disjunção inclusiva (∨) pela condicional (→); 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
~p∨s ≡ ~(~p)→s 
A dupla negação da proposição simples p corresponde à proposição original. Ficamos com: 
~p∨s ≡ p→s 
Logo, temos a seguinte equivalência: 
p→s: "Se [o agente censitário transcreveu o texto em planilha eletrônica], então [o trabalho foi realizado 
com sucesso]." 
Veja que não temos a proposição p→s nas alternativas. Note, porém, que essa condicional é equivalente à 
sua contrapositiva ~s→~p. 
~s→~p: "Se [O trabalho não foi realizado com sucesso], então [o agente censitário não transcreveu o 
texto em planilha eletrônica]." 
Veja que essa proposição está presente na alternativa E. 
Gabarito: Letra E. 
 
Outras Bancas - Outras equivalências e negações 
(AOCP/DEPEN PR/2024) Em relação à proposição “João nunca foi privado de liberdade, e o relatório 
policial é inconclusivo”, pode-se afirmar que sua negação lógica é corretamente representada em 
a) João sempre foi privado de liberdade, e o relatório policial não é inconclusivo. 
b) João nunca será privado de liberdade, então o relatório policial nunca será inconclusivo. 
c) Se João nunca for privado de liberdade, então o relatório policial nunca é inconclusivo. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
73
167


 
d) Se o relatório policial sempre é inconclusivo, então João sempre é privado de liberdade. 
e) Se o relatório policial é inconclusivo, então ao menos uma vez João foi privado de liberdade. 
Comentários: 
Sejam as proposições simples: 
j: "João nunca foi privado de liberdade." 
r: "O relatório policial é inconclusivo." 
Observe que a negação da proposição j não é “João sempre foi privado de liberdade”. Isso porque o 
antônimo “sempre” não nega corretamente a palavra “nunca”. 
Veja que, para que "João nunca foi privado de liberdade" seja falsa, basta que ao menos uma vez João 
tenha sido privado de liberdade. Logo, a negação da proposição j pode ser descrita da seguinte maneira: 
~j: "Ao menos uma vez João foi privado de liberdade." 
Feita essa consideração, note que a proposição original pode ser escrita pela conjunção j∧r: 
j∧r:"[João nunca foi privado de liberdade] e [o relatório policial é inconclusivo]." 
Em regra, devemos utilizar De Morgan para negar uma conjunção. Logo, vamos testar essa possibilidade 
primeiro.  
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~ (j∧r) ≡ ~j∨~r 
Logo, a negação requerida pode ser descrita por:  
~j∨~r: “[Ao menos uma vez João foi privado de liberdade], e [o relatório policial não é inconclusivo].” 
Note que essa possível negação não está presente nas alternativas.  
Observe que alternativas B, C, D e E apresentam condicionais como a negação da conjunção original. Logo, 
vamos utilizar as seguintes negações da conjunção: 
~(p∧q) ≡ p→~q 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
74
167


 
ou 
~(p∧q) ≡ q→~p 
Aplicando essas equivalências para o caso em questão, ficamos com: 
~(j∧r) ≡ j→~r 
ou 
~(j∧r) ≡ r→~j 
Logo, podemos escrever a negação da conjunção j∧r das seguintes formas: 
~(j∧r) ≡ j→~r: "Se [João nunca foi privado de liberdade], então [o relatório policial não é inconclusivo]." 
ou 
~(j∧r) ≡ r→~j: "Se [o relatório policial é inconclusivo], então [ao menos uma vez João foi privado de 
liberdade]." 
Veja que a segunda possibilidade de se negar a conjunção está presente na alternativa E, que é o gabarito 
da questão. 
Gabarito: Letra E. 
 
(IDECAN/Pref SCS/2023)  Uma bicondicional equivale a uma conjunção de duas condicionais. Em 
termos simbólicos, teremos 
a)  pq = (p∨q) e (q∨p) 
b)  pq = (p→q) e (q→p) 
c)  p∨q = (p∨q) e (q→p) 
d)  p←q = (p→~q) e (q→p) 
Comentários: 
Conforme visto na teoria da aula de Equivalências Lógicas, a bicondicional () apresenta a seguinte 
equivalência: 
pq ≡ (p→q)∧(q→p) 
Utilizando a letra "e" para representar a conjunção "∧", temos: 
pq ≡ (p→q) e (q→p) 
Gabarito: Letra B. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
75
167


 
(IDECAN/IF PA/2022) Assinale a alternativa que apresenta uma proposição equivalente a “todos os 
empresários conseguirão sucesso no ramo do empreendedorismo se, e somente se, investirem tempo 
com muito estudo e pesquisa". 
a) Se todos os empresários conseguirem sucesso no ramo do empreendedorismo, então investiram tempo 
com muito estudo e pesquisa ou se investiram tempo com muito estudo e pesquisa, então todos os 
empresários conseguirão sucesso no ramo do empreendedorismo. 
b) Se todos os empresários conseguirem sucesso no ramo do empreendedorismo, então investiram tempo 
com muito estudo e pesquisa e investiram tempo com muito estudo e pesquisa se, e somente se, todos os 
empresários conseguirem sucesso no ramo do empreendedorismo. 
c) Se todos os empresários conseguirem sucesso no ramo do empreendedorismo, então investiram tempo 
com muito estudo e pesquisa e se investiram tempo com muito estudo e pesquisa, então todos os 
empresários conseguirão sucesso no ramo do empreendedorismo. 
d) Se não investirem tempo com muito estudo e pesquisa, então nem todos os empresários conseguirão 
sucesso no ramo do empreendedorismo. 
Comentários: 
Sejam as proposições simples: 
s: "Todos os empresários conseguem sucesso no ramo do empreendedorismo" 
i: "Todos os empresários investem tempo com muito estudo e pesquisa." 
A proposição original pode ser descrita por si: 
si: "[Todos os empresários conseguirão sucesso no ramo do empreendedorismo] se, e somente se, 
[(todos os empresários) investirem tempo com muito estudo e pesquisa]." 
Note que em todas as alternativas temos ao menos um conectivo condicional "se...então". Logo, devemos 
transformar essa bicondicional em condicionais. 
Conforme visto na teoria, temos a seguinte equivalência: pq ≡ (p→q)∧(q→p). Aplicando essa 
equivalência para o caso em questão temos: 
si ≡ (s→i)∧(i→s) 
Portanto, a proposição original pode ser descrita por: 
(s→i)∧(i→s): "[Se (todos os empresários conseguirem sucesso no ramo do empreendedorismo), então 
(investiram tempo com muito estudo e pesquisa)] e [se (investiram tempo com muito estudo e pesquisa), 
então (todos os empresários conseguirão sucesso no ramo do empreendedorismo)]." 
Gabarito: Letra C. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
76
167


 
FGV 
FGV - Equivalências Fundamentais 
(FGV/ALESC/2024) Considere a afirmação: 
“Se tenho namorada então não fico sozinho” 
 Uma afirmação logicamente equivalente à afirmação dada é: 
a) Se não fico sozinho então tenho namorada. 
b) Se fico sozinho então não tenho namorada. 
c) Se não tenho namorada então fico sozinho. 
d) Tenho namorada e não fico sozinho. 
e) Tenho namorada ou não fico sozinho. 
Comentários: 
Sejam as proposições simples: 
t: "Tenho namorada." 
f: "Fico sozinho." 
A afirmação original corresponde a t→~f: 
t→~f: “Se [tenho namorada], então [não fico sozinho].” 
As alternativas apresentam tanto condicionais (se...então; →) quanto uma disjunção inclusiva (ou; ∨) 
como equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a 
condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
t→~f ≡ ~(~f)→~t 
A dupla negação de f corresponde à proposição original f. Ficamos com: 
t→~f ≡ f→~t 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
77
167


 
A proposição equivalente pode ser descrita por: 
f→~t: “Se [fico sozinho], então [não tenho namorada].” 
Veja que essa equivalência está na alternativa B, que é o gabarito da questão. 
Para fins didáticos, vamos utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar 
o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
t→~f ≡ ≡ ~t∨~f 
A proposição equivalente pode ser descrita por: 
~t∨~f: “[Não tenho namorada] ou [não fico sozinho].” 
Veja que essa possível equivalência não aparece nas alternativas. 
Gabarito: Letra B. 
 
(FGV/SEFAZ-MG/2023) É dada a afirmativa:  
“Se o cliente pagou então não é devedor.” 
Para cada uma das três afirmativas a seguir, assinale “V” se a afirmativa for logicamente equivalente à 
afirmativa dada e “F” se a afirmativa não for logicamente equivalente à afirmativa dada.  
I. Se o cliente não pagou então é devedor.  
II. Se o cliente não é devedor então pagou.  
III. Se o cliente é devedor então não pagou.  
As afirmativas I, II e III são, respectivamente, 
a) V, V e F.  
b) F, V e F.  
c) F, F e V.  
d) F, V e V.  
e) V, V e V.  
Comentários: 
Sejam as proposições simples: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
78
167


 
p: "O cliente pagou." 
d: "O cliente é devedor." 
A proposição original pode ser descrita por p→~d: 
p→~d: "Se [o cliente pagou], então [não é devedor]." 
Veja que estamos partindo de uma condicional e a questão pergunta quais das três condicionais são 
equivalentes. Para avaliá-las, devemos utilizar somente a equivalência contrapositiva, pois ela é a única 
que transforma uma condicional em outra condicional. 
A equivalência contrapositiva é dada por p→q ≡ ~q→~p. Para aplicar essa equivalência, devemos realizar 
o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
p→~d ≡ ~(~d)→~p 
A dupla negação de uma proposição corresponde à proposição original. Ficamos com: 
p→~d ≡ d→~p 
A proposição equivalente pode ser descrita por: 
d→~p: "Se [o cliente é devedor], então [não pagou]." 
Somente a afirmação III apresenta uma condicional equivalente. As demais condicionais não são 
equivalentes, pois não decorrem da equivalência contrapositiva. O gabarito, portanto, é letra C: F, F e V. 
Gabarito: Letra C. 
 
 (FGV/AGENERSA/2023) Considere a afirmativa a seguir. 
“Se não durmo, então tenho dor de cabeça.” 
Analise, a seguir, três novas afirmativas: 
I. Se durmo, então não tenho dor de cabeça. 
II. Se tenho dor de cabeça, então não durmo. 
III. Se não tenho dor de cabeça, então durmo. 
Assinale a opção que indica a(s) afirmativa(s) que é(são) equivalente(s) à inicial. 
a) I, apenas. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
79
167


 
b) II, apenas. 
c) III, apenas. 
d) I e II, apenas. 
e) I, II e III. 
Comentários: 
Sejam as proposições simples: 
d: "Durmo." 
t: "Tenho dor de cabeça." 
A proposição original pode ser descrita por ~d→t: 
~d→t: "Se [não durmo], então [tenho dor de cabeça]." 
Veja que estamos partindo de uma condicional e a questão pergunta quais das três condicionais são 
equivalentes. Para avaliá-las, devemos utilizar somente a equivalência contrapositiva, pois ela é a única 
que transforma uma condicional em outra condicional. 
A equivalência contrapositiva é dada por p→q ≡ ~q→~p. Para aplicar essa equivalência, devemos realizar 
o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
~d→t ≡ ~t→~(~d) 
A dupla negação de uma proposição corresponde à proposição original. Ficamos com: 
~d→t ≡ ~t→d 
A proposição equivalente pode ser descrita por: 
~t→d: "Se [não tenho dor de cabeça], então [durmo]." 
Somente a afirmação III apresenta uma condicional equivalente. As demais condicionais não são 
equivalentes, pois não decorrem da equivalência contrapositiva. O gabarito, portanto, é letra C. 
Gabarito: Letra C. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
80
167


 
(FGV/CM Taubaté/2022) Considere a sentença: “Se Antônio é baiano, então Carlos não é 
amapaense”. Uma sentença logicamente equivalente à sentença dada é:  
a) Se Carlos não é amapaense, então Antônio é baiano.  
b) Se Antônio não é baiano, então Carlos é amapaense.  
c) Se Carlos é amapaense, então Antônio é baiano.  
d) Antônio não é baiano ou Carlos não é amapaense.  
e) Antônio é baiano e Carlos é amapaense. 
Comentários: 
Sejam as proposições simples: 
a: "Antônio é baiano." 
c: "Carlos é amapaense." 
A proposição original pode ser descrita por a→~c: 
a→~c: "Se [Antônio é baiano], então [Carlos não é amapaense]." 
As alternativas apresentam tanto condicionais (se...então; →) quanto uma disjunção inclusiva (ou; ∨) 
como equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a 
condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
a→~c ≡ ~(~c)→~a 
A dupla negação de uma proposição corresponde à proposição original. Ficamos com: 
a→~c ≡ c→~a 
A proposição equivalente pode ser escrita por: 
c→~a: "Se [Carlos é amapaense], então [Antônio não é baiano]." 
Veja que essa equivalência não está nas alternativas apresentadas. 
Vamos agora utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar o seguinte 
procedimento: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
81
167


 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
a→~c ≡ ~a∨~c 
A proposição equivalente pode ser descrita por: 
~a∨~c: “[Antônio não é baiano] ou [Carlos não é amapaense].” 
Note que essa proposição equivalente está presente na alternativa D. 
Gabarito: Letra D. 
 
FGV - Negações Lógicas  
(FGV/MPE SP/2023) Considere a proposição: 
“Se estamos em fevereiro, então eu pago o IPVA”. 
Assinale a opção que apresenta uma negação dessa proposição. 
a) Estamos em fevereiro e eu não pago o IPVA. 
b) Não estamos em fevereiro e eu não pago o IPVA. 
c) Se estamos em fevereiro, então eu não pago o IPVA. 
d) Se não estamos em fevereiro, então eu não pago o IPVA. 
e) Se não estamos em fevereiro, então eu pago o IPVA. 
Comentários: 
Sejam as proposições simples: 
e: "Estamos em fevereiro." 
p: "Eu pago o IPVA." 
A sentença original pode ser descrita por e→p:  
e→p: “Se [estamos em fevereiro], então [eu pago o IPVA]”. 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
82
167


 
Para o caso em questão, temos: 
~(e→p) ≡ e∧~p 
Logo, a negação pode ser descrita por: 
e∧~p: "[Estamos em fevereiro] e [eu não pago o IPVA]." 
Gabarito: Letra A. 
 
 (FGV/PGM Niterói/2023) Considere a sentença: “Se o chapéu é branco, então o sapato é bicolor”. 
A negação lógica da sentença dada é: 
a) se o chapéu é branco, então o sapato não é bicolor; 
b) se o chapéu não é branco, então o sapato é bicolor; 
c) se o sapato não é bicolor, então o chapéu não é branco; 
d) o chapéu não é branco ou o sapato é bicolor; 
e) o chapéu é branco e o sapato não é bicolor. 
Comentários: 
Sejam as proposições simples: 
c: "O chapéu é branco." 
s: "O sapato é bicolor." 
A sentença original pode ser descrita por c→s:  
c→s: “Se [o chapéu é branco], então [o sapato é bicolor]”. 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(c→s) ≡ c∧~s 
Logo, a negação pode ser descrita por: 
c∧~s: "[O chapéu é branco] e [o sapato não é bicolor]." 
Gabarito: Letra E. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
83
167


 
(FGV/Pref Niterói/2023) Houve um problema na construção de uma casa e o arquiteto que elaborou o 
projeto disse: 
“O projeto está certo e eu fiscalizei a obra.” 
Considerando que essa frase é falsa, é correto concluir que 
a) “O projeto não está certo e o arquiteto fiscalizou a obra.” 
b) “O projeto está certo e o arquiteto não fiscalizou a obra.” 
c) “O projeto não está certo e o arquiteto não fiscalizou a obra.” 
d) “O projeto está certo ou o arquiteto fiscalizou a obra.” 
e) “O projeto não está certo ou o arquiteto não fiscalizou a obra.” 
Comentários: 
Sejam as proposições simples: 
p: "O projeto está certo." 
f: "O arquiteto fiscalizou a obra." 
Note que a frase original foi dita pelo arquiteto. Nesse caso, podemos escrever a frase como uma 
conjunção da forma p∧f:  
p∧f: "[O projeto está certo] e [o arquiteto fiscalizou a obra]." 
Como o enunciado diz que a frase original é falsa, é correto concluir a negação dessa proposição. 
Devemos, portanto, negar a conjunção p∧f. 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~ (p∧f) ≡ ~p∨~f 
Logo, a negação requerida pode ser descrita por:  
~p∨~f: “[O projeto não está certo] ou [o arquiteto não fiscalizou a obra].” 
Gabarito: Letra E. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
84
167


 
  (FGV/Câmara dos Deputados/2023) Na canção “Se você jurar”, de Ismael Silva, encontramos a 
afirmação: 
Se você jurar que me tem amor, eu posso me regenerar. 
A negação dessa proposição é 
a) você jura que me tem amor e eu não me regenero. 
b) você não jura que me tem amor e eu não me regenero. 
c) você não jura que me tem amor e eu me regenero. 
d) você jura que me tem amor e eu posso me regenerar. 
e) você não jura que me tem amor e eu não posso me regenerar. 
Comentários: 
Sejam as proposições simples: 
j: "Você jura que me tem amor." 
r: "Eu posso me regenerar." 
Observação: Em "Você jura que me tem amor.", apesar de termos dois verbos (jurar e ter), temos uma 
proposição simples, pois há apenas uma oração principal: 
"Você jura que me tem amor." 
"Você jura ISSO." 
 
O mesmo ocorre com a proposição "Eu posso me regenerar.", que apresenta apenas uma oração principal: 
"Eu posso me regenerar." 
"Eu posso ISSO." 
Note que a afirmação original pode ser descrita por j→r: 
j→r: "Se [você jurar que me tem amor], [eu posso me regenerar]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(j→r) ≡ j∧~r 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
85
167


 
Ficamos com a seguinte negação: 
j∧~r: "[Você jura que me tem amor] e [eu não posso me regenerar]." 
A alternativa que mais se aproxima da negação obtida corresponde à letra A, em que a proposição ~r, 
dada por "eu não posso me regenerar", é reescrita como "eu não me regenero". 
j∧~r: "[Você jura que me tem amor] e [eu não me regenero]." 
Gabarito: Letra A. 
 
FGV - Questões com mais de uma equivalência 
(FGV/ALESC/2024) Considere a sentença: 
“Se x ≤ 6 e x > 4, então −x ≤ 2”. Uma sentença logicamente equivalente à sentença dada é 
a) Se x > 6 e x ≤ 4, então  −x > 2. 
b) Se  −x ≤ 2, então x ≤ 6 e x > 4. 
c) Se x > 6 ou x ≤ 4, então  − x > 2. 
d) x > 6 ou x ≤ 4 ou  −x ≤ 2. 
e) x > 6 e x ≤ 4 ou  −x ≤ 2. 
Comentários: 
Pessoal, nessa questão temos sentenças abertas, não proposições. Isso porque as sentenças que vamos 
definir a seguir dependem de uma variável. Apesar disso, podemos utilizar nossos conhecimentos de 
equivalências lógicas para resolver o problema. 
Cumpre destacar também que a resolução da questão requer um conhecimento básico sobre inequações. 
Considere as seguintes sentenças: 
p: “x ≤ 6” 
q: “x > 4” 
r: “−x ≤ 2” 
Observe que as negações dessas sentenças são: 
~p: “x > 6” 
~q: “x ≤ 4” 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
86
167


 
~r: “−x > 2” 
Observação: note que, se “𝒙 é menor ou igual (≤) a um número”, a negação dessa sentença corresponde a 
“𝒙 maior do que (>) esse número”. 
Por exemplo, considerando x ≤ 6, os números 6, 5, 4 satisfazem essa inequação e os números 7, 8 e 9 não 
satisfazem. Na negação é o contrário: em x > 6, os números 7, 8  e 9 satisfazem essa inequação e os 
números 6, 5 e 4 não satisfazem. 
Além disso, se “𝒙 é maior do que (>) um número”, a negação dessa sentença corresponde a  “𝒙 é menor 
ou igual (≤) a esse número”. 
Por exemplo, se x > 4, os números 5, 6  e 7 satisfazem essa inequação e os números 4, 3 e 2 não satisfazem. 
Na negação é o contrário: em x ≤ 4, os números 4, 3 e 2 satisfazem essa inequação e os números 5, 6 e 7 
não satisfazem.  
Voltando ao problema, note que a sentença original pode ser descrita por p∧q→r: 
p∧q→r: “Se [(x ≤ 6) e (x > 4)], então [−x ≤ 2].” 
As alternativas apresentam tanto condicionais (se...então; →) quanto uma disjunção inclusiva (ou; ∨) 
como equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a 
condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
p∧q→r ≡ ~r→~(p∧q) 
Observe que ~(p∧q) é a negação da conjunção p∧q. Desenvolvendo por De Morgan, obtemos ~p∨~q. 
Ficamos com: 
p∧q→r ≡ ~r→(~p∨~q) 
Logo, uma possível sentença equivalente corresponde a: 
~r→(~p∨~q): “Se [−x > 2], então [(x > 6) ou (x ≤ 4)].” 
Note que não temos essa equivalência nas alternativas. 
Nesse momento, vamos utilizar a segunda equivalência possível. Para aplicar essa equivalência, devemos 
realizar o seguinte procedimento: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
87
167


 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
p∧q→r ≡ ≡ ~(p∧q)∨r 
Observe que ~(p∧q) é a negação da conjunção p∧q. Desenvolvendo por De Morgan, obtemos ~p∨~q. 
Ficamos com: 
p∧q→r ≡ ≡ (~p∨~q)∨r 
A proposição equivalente pode ser descrita por: 
(~p∨~q)∨r: “[(x > 6) ou (x ≤ 4)] ou [−x ≤ 2].” 
 Gabarito: Letra D. 
 
(FGV/ALE TO/2024) A negação da proposição: 
Se 𝑦 ≠ 0, então 𝑥 > 2 e 𝑥 ≤ 5 
é dada por 
a) Se 𝑦 = 0, então 𝑥 > 2 e 𝑥 ≤ 5 
b) Se 𝑦 = 0, então 𝑥 < 2 ou 𝑥 ≥ 5 
c) 𝑦 = 0 e 𝑥 ≤ 2 ou 𝑥 > 5 
d) 𝑦 ≠ 0 e 𝑥 ≤ 2 ou 𝑥 > 5 
e) 𝑦 ≠ 0 e 𝑥 ≤ 2 e 𝑥 > 5 
Comentários: 
Antes de resolvermos o problema, cumpre destacar que a sentença apresentada não é uma proposição. 
Trata-se de uma sentença aberta, pois dependemos das variáveis 𝑥 e 𝑦 para determinar os possíveis 
valores lógicos dela. 
Considere as seguintes sentenças: 
p: "𝑦 ≠ 0” 
q: "𝑥 > 2" 
r: "𝑥 ≤ 5" 
Observe que a negação dessas sentenças corresponde a: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
88
167


 
~p: "𝑦 = 0” 
~q: "𝑥 ≤ 2" 
~r: "𝑥 > 5" 
Observação: note que a negação de q:"𝑥 > 2" é ~q:"𝑥 ≤ 2". Para o caso em que 𝑥 é igual a 2, q é falso, 
porque 2 não é "maior do que dois". Nesse caso, ~q deve ser verdadeiro. Consequentemente, o caso em 
que 𝑥 é exatamente igual a 2 deve ser incluído na sentença ~q. 
Além disso, note que a negação de r: "𝑥 ≤ 5" é ~r: "𝑥 > 5". Para o caso em que 𝑥 é igual a 5, r é verdadeiro, 
porque 5 é "menor ou igual a 5". Nesse caso, ~r deve ser falso. Consequentemente, o caso em que 𝑥 é 
exatamente igual a 5 não deve ser incluído na sentença ~r. 
Note que a sentença original corresponde a p→(q∧r): 
p→(q∧r): "Se [𝑦 ≠ 0], então [(𝑥 > 2) e (𝑥 ≤ 5)]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~[p→(q∧r)] ≡ p∧~(q∧r) 
Note que a parcela ~(q∧r) pode ser desenvolvida por De Morgan, correspondendo a ~q∨~r. Ficamos com: 
~[p→(q∧r)] ≡ p∧(~q∨~r) 
Ficamos com a seguinte negação: 
p∧(~q∨~r): "[𝑦 ≠ 0] e [(𝑥 ≤ 2) ou (𝑥 > 5)]." 
Gabarito: Letra D. 
 
(FGV/MPE SP/2023) “Se a TV não está ligada, então eu estou dormindo ou estou lendo”. 
Assinale a opção que descreve uma sentença logicamente equivalente à afirmação acima. 
a) A TV não está ligada e eu estou acordado e não estou lendo. 
b) Se eu não estou dormindo e não estou lendo, então a TV está ligada. 
c) Se eu estou acordado ou não estou lendo, então a TV está ligada. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
89
167


 
d) Eu estou acordado e lendo se, e somente se, a TV está desligada. 
e) A TV está ligada e eu estou acordado ou não estou lendo. 
Comentários: 
Sejam as proposições simples: 
t: "A TV está ligada." 
d: "Eu estou dormindo." 
l: "Eu estou lendo." 
A proposição original pode ser descrita pela condicional entre ~t e (d∨l), isto é, pode ser descrita por 
~t→(d∨l): 
~t→(d∨l): “Se [a TV não está ligada], então [(eu estou dormindo) ou (estou lendo)].” 
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p→q ≡ ~q→~p. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
~t→(d∨l) ≡ ~(d∨l)→~(~t) 
A dupla negação de uma proposição corresponde à proposição original. Ficamos com: 
~t→(d∨l) ≡ ~(d∨l)→t 
Note que a parcela ~(d∨l) também pode ser desenvolvida por De Morgan, e corresponde a ~d∧~l. 
Portanto, temos a seguinte equivalência: 
~t→(d∨l) ≡ (~d∧~l)→t 
Logo, a proposição equivalente pode ser descrita por: 
(~d∧~l)→t: "Se [(eu não estou dormindo) e (não estou lendo)], então [a TV está ligada]." 
Gabarito: Letra B. 
  
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
90
167


 
CEBRASPE 
CEBRASPE - Equivalências Fundamentais 
(CEBRASPE/SEFAZ AC/2024) Assinale a opção em que é corretamente apresentada uma proposição 
que é logicamente equivalente à proposição “Se não há débito fiscal, então não há cobrança”.  
a) Há débito fiscal e há cobrança.  
b) Não há débito fiscal ou não há cobrança.  
c) Há débito fiscal ou não há cobrança.  
d) Não há débito fiscal ou há cobrança.  
e) Não há débito fiscal e não há cobrança.  
Comentários: 
 Sejam as proposições simples: 
d: "Há débito fiscal." 
c: "Há cobrança." 
A proposição original pode ser descrita pela condicional ~d→~c: 
~d→~c: “Se [não há débito fiscal], então [não há cobrança]”  
Veja que as alternativas não apresentam uma condicional como possível equivalência. Logo, não se deve 
utilizar a equivalência contrapositiva, dada por p→q ≡ ~q→~p. 
Outra equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte: p→q ≡ 
~p∨q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
Mantém-se o segundo termo. 
Para o caso em questão, temos: 
~d→~c ≡ ~(~d)∨~c 
A dupla negação de d corresponde à proposição original. Logo, ficamos com: 
~d→~c ≡ d∨~c 
Essa proposição equivalente pode ser descrita por: 
d∨~c: "[Há débito fiscal] ou [não há cobrança]." 
Gabarito: Letra C. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
91
167


 
 (CEBRASPE/SEFAZ AC/2024) Uma criança deseja ficar brincando no parquinho. A mãe diz ao filho: 
 — “Filho, não quero que se molhe. Quando começar a chover ou chegar uma criança grande, vamos 
embora. Não pise na água ou vamos embora.” 
Após alguns minutos, a mãe tomou a criança pela mão e eles foram embora. 
Ainda considerando o texto, assinale a opção em que está apresentada uma exortação que, sob o ponto 
de vista lógico, tenha o mesmo significado daquela feita pela mãe em “Não pise na água ou vamos 
embora”. 
a) Se não pisar na água, não vamos embora. 
b) Não pise na água e não vamos embora. 
c) Pise na água e vamos embora. 
d) Não pise na água e vamos embora. 
e) Se pisar na água, vamos embora.    
Comentários:  
Sejam as proposições simples: 
p: "Pise na água." 
v: "Vamos embora." 
Note que a proposição “não pise na água ou vamos embora” pode ser descrita por ~p∨v: 
~p∨v: "[Não pise na água] ou [vamos embora]." 
A questão pergunta por uma opção que tenha o mesmo significado de ~p∨v. Queremos, portanto, uma 
equivalência de ~p∨v. 
Sabemos que existe uma equivalência fundamental que transforma a disjunção inclusiva em uma 
condicional. Para transformar a disjunção inclusiva em uma condicional, podemos usar a equivalência p∨q 
≡~p→q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a disjunção inclusiva (∨) pela condicional (→); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
~p∨v ≡ ~(~p)→v 
Observe que a equivalência obtida pode ser descrita por: 
p→v: “Se [pisar na água], então [vamos embora].” 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
92
167


 
A alternativa E apresenta essa condicional na forma em que se omite o "então". O gabarito, portanto, é 
letra E. 
Gabarito: letra E. 
 
(CESPE/ANA/2024) P5: Se o habitador artificial se romper antes de chegar o socorro, eu implodo. 
P5 é equivalente a “Se eu não implodi, o habitador artificial não se rompeu antes de chegar o socorro”. 
Comentários: 
Sejam as proposições simples: 
r: "O habitador artificial se rompeu antes de chegar o socorro." 
i: "Eu implodi." 
A proposição P5 pode ser descrita pela condicional r→i: 
r→i: "Se [o habitador artificial se romper antes de chegar o socorro], [eu implodo]." 
Existem duas possíveis equivalências para a condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Note que a questão apresenta uma condicional como possível equivalência para P5. Logo, devemos utilizar 
a equivalência contrapositiva. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
r→i ≡ ~i→~r 
Logo, a proposição equivalente pode ser escrita por: 
~i→~r: "Se [eu não implodi], [o habitador artificial não se rompeu antes de chegar o socorro]." 
Gabarito: CERTO. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
93
167


 
(CESPE/PC PE/2024) P: “Se não preciso tentar roubá-lo, não cometi esse crime.” 
Assinale a opção em que está apresentada uma proposição equivalente a P. 
a) “Preciso tentar roubá-lo, mas não cometi esse crime.” 
b) “Precisava tentar roubá-lo e cometi esse crime.” 
c) “Se não cometi esse crime, não preciso tentar roubá-lo.” 
d) “Preciso tentar roubá-lo ou não cometi esse crime.” 
e) “Se preciso tentar roubá-lo, cometi esse crime.” 
Comentários 
Sejam as proposições simples: 
r: "Preciso tentar roubá-lo." 
c: "Cometi esse crime." 
A proposição P original corresponde a ~r→~c: 
~r→~c: “Se [não preciso tentar roubá-lo], [não cometi esse crime].” 
As alternativas apresentam tanto condicionais (se...então; →) quanto uma disjunção inclusiva (ou; ∨) 
como equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a 
condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
~r→~c ≡ ~(~c)→~(~r) 
A dupla negação de c corresponde à proposição original c, e a dupla negação de r corresponde à 
proposição original r. Ficamos com: 
~r→~c ≡ c→r 
A proposição equivalente pode ser descrita por: 
c→r: “Se [cometi esse crime], [preciso tentar roubá-lo].” 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
94
167


 
Veja que essa equivalência não está nas alternativas apresentadas. 
Vamos agora utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar o seguinte 
procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
~r→~c ≡ ~(~r)∨~c 
A dupla negação de r corresponde à proposição original r. Ficamos com: 
~r→~c ≡ r∨~c 
A proposição equivalente pode ser descrita por: 
r∨~c: “[Preciso tentar roubá-lo] ou [não cometi esse crime].” 
Note que essa proposição equivalente está presente na alternativa D. 
Gabarito: Letra D. 
 
(CESPE/SERPRO/2023) P4: Se não há prova sem nome nos arquivos do professor, então o aluno não 
se esqueceu de colocar seu nome na prova. 
A proposição P4 é equivalente a “Se o aluno não se esqueceu de colocar seu nome na prova, então não 
há prova sem nome nos arquivos do professor”. 
Comentários: 
Sejam as proposições simples: 
p: "Há prova sem nome nos arquivos do professor." 
a: "O aluno se esqueceu de colocar seu nome na prova." 
A proposição P4 original pode ser descrita por ~p→~a: 
~p→~a: "Se [não há prova sem nome nos arquivos do professor], então [o aluno não se esqueceu de 
colocar seu nome na prova]." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
95
167


 
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p→q ≡ ~q→~p. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
~p→~a ≡ ~(~a)→~(~p) 
A dupla negação de uma proposição simples corresponde à proposição original. Logo, temos: 
~p→~a ≡ a→p 
A proposição equivalente pode ser descrita por: 
a→p: "Se [o aluno se esqueceu de colocar seu nome na prova], então [há prova sem nome nos arquivos do 
professor]." 
Note que a questão nos trouxe o condicional ~a→~p, isto é, inverteu a ordem do antecedente e do 
consequente de ~p→~a sem negar ambos os termos. O gabarito, portanto, é ERRADO. 
Gabarito: ERRADO.  
 
CEBRASPE - Negações Lógicas  
(CESPE/ANA/2024) P4: Se o reciclador de água estragar antes de chegar o socorro, eu morro de sede. 
A negação de P4 pode ser corretamente expressa por “O reciclador de água estragou antes de chegar o 
socorro, mas eu não morri de sede”. 
Comentários: 
Sejam as proposições simples: 
e: “O reciclador de água estraga antes de chegar o socorro.” 
m: “Eu morro de sede.” 
Note que a proposição P4 pode ser descrita pela condicional e→m: 
e→m: “Se [o reciclador de água estragar antes de chegar o socorro], [eu morro de sede]” 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
96
167
==6306a==


 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(e→m) ≡ e∧~m 
Logo, a negação pode ser descrita por: 
e∧~m: "[O reciclador de água estragou antes de chegar o socorro] e [eu não morri de sede]." 
Sabemos que o conectivo “e” pode ser representado por “mas”. Logo, outra forma de se representar a 
negação procurada é: 
e∧~m: "[O reciclador de água estragou antes de chegar o socorro], mas [eu não morri de sede]." 
Gabarito: CERTO. 
 
(CESPE/FINEP/2024) Assinale a opção que apresenta a negação da proposição: Paguei o café da 
manhã com o cartão de débito e o almoço com o cartão de crédito. 
a) Paguei o café da manhã com o cartão de crédito e não paguei o almoço com o cartão de débito. 
b) Paguei o almoço com o cartão de débito e o café da manhã com o cartão de crédito. 
c) Não paguei o café da manhã com o cartão de débito nem o almoço com o cartão de crédito. 
d) Não paguei o café da manhã com o cartão de débito e o almoço com o cartão de crédito. 
e) Não paguei o café da manhã com o cartão de débito ou o almoço com o cartão de crédito. 
Comentários: 
Sejam as proposições simples: 
c: "Paguei o café da manhã com o cartão de débito." 
a: "Paguei o almoço com o cartão de crédito." 
A proposição original do enunciado corresponde a c∧a: 
c∧a: "[Paguei o café da manhã com o cartão de débito] e [(paguei) o almoço com o cartão de crédito]." 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
97
167


 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~(c∧a) ≡ ~c∨~a 
Logo, ficamos com a seguinte negação: 
~c∨~a: "[Não paguei o café da manhã com o cartão de débito] ou [não paguei o almoço com o cartão de 
crédito]." 
Veja que as alternativas de A até D apresentam o conectivo "e" como parte na negação da proposição 
original. Por esse motivo, essas alternativas podem ser eliminadas. Especial atenção pode ser dada à 
alternativa C, que apresenta o termo "nem", que corresponde ao conectivo "e" seguido da negação "não". 
Portanto, resta a alternativa E como gabarito, que é a única que apresenta o conectivo "ou" como 
possível negação da proposição original. Nessa alternativa, note que a banca examinadora omitiu o 
segundo termo "não paguei": 
~c∨~a: "[Não paguei o café da manhã com o cartão de débito] ou [não paguei o almoço com o cartão de 
crédito]." 
Esse tipo de omissão de termos repetidos ocorre na Língua Portuguesa, e a banca utilizou desse artifício 
para "desestabilizar" o concurseiro, que poderia pensar que a alternativa E representa a disjunção inclusiva 
~c∨a. Felizmente, a banca acabou sendo "gente fina" ao inserir o conectivo "e" nas alternativas de A até D, 
restando apenas a alternativa E como possível resposta. 
Gabarito: Letra E. 
 
 (CESPE/POLC AL/2023) Considerando os conectivos lógicos usuais e assumindo que as letras 
maiúsculas representam proposições lógicas, julgue o item seguinte, relativo à lógica proposicional. 
A negação da sentença "Se eu me alimento de forma saudável, então terei uma boa qualidade de vida no 
período da terceira idade" corresponde à sentença "Se eu não me alimento de forma saudável, então 
não terei uma boa qualidade de vida no período da terceira idade". 
Comentários: 
Observe que originalmente temos uma condicional (se...então; →) e a questão informa que a sua negação 
é outra condicional. Conforme visto na teoria, a negação da condicional é uma conjunção (e; ∧). Nesse 
caso, já poderíamos marcar o item como ERRADO. 
Para fins didáticos, vamos obter a negação da condicional em questão. 
Sejam as proposições simples: 
a: "Eu me alimento de forma saudável." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
98
167


 
q: "Terei uma boa qualidade de vida no período da terceira idade." 
A proposição composta original pode ser definida pela condicional a→q: 
a→q: "Se [eu me alimento de forma saudável], então [terei uma boa qualidade de vida no período da 
terceira idade]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(a→q) ≡ a∧~q 
Logo, a negação pode ser descrita por:  
a∧~q: "[Eu me alimento de forma saudável] e [não terei uma boa qualidade de vida no período da terceira 
idade]." 
Gabarito: ERRADO. 
 
(CESPE/SERPRO/2023) P6: Se a assinatura do aluno não consta da lista de presença do dia da prova, 
então o aluno não fez a prova. 
A negação da proposição P6 pode ser corretamente expressa por “a assinatura do aluno não consta da 
lista de presença do dia da prova, mas o aluno não deixou de fazer a prova”. 
Comentários: 
Sejam as proposições simples: 
a: "A assinatura do aluno consta da lista de presença do dia da prova." 
f: "O aluno fez a prova." 
A proposição P6 original pode ser escrita pela conjunção ~a→~f:  
~a→~f: "Se [a assinatura do aluno não consta da lista de presença do dia da prova], então [o aluno não 
fez a prova]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
99
167


 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~a→~f ≡ ~a∧~(~f) 
A dupla negação de f corresponde à proposição original. Logo, ficamos com: 
~a→~f ≡ ~a∧f 
Logo, a negação requerida pode ser descrita por:  
~a∧f: "[A assinatura do aluno não consta da lista de presença do dia da prova] e [o aluno fez a prova]." 
Sabemos que o conectivo conjunção, tradicionalmente representado por "e", pode também ser 
representado por "mas". Além disso, podemos entender que "o aluno não deixou de fazer a prova" tem o 
mesmo sentido de "o aluno fez a prova". Logo, a negação da condicional, ~a∧f, também pode ser descrita 
por: 
~a∧f: "[A assinatura do aluno não consta da lista de presença do dia da prova], mas [o aluno não deixou de 
fazer a prova]." 
Gabarito: CERTO. 
 
CEBRASPE - Questões com mais de uma equivalência 
(CEBRASPE/SEFAZ AC/2024) P6: “Se houver incerteza sobre os impactos nos planos de longo prazo da 
empresa, o investidor ficará receoso e a ação da empresa ficará volátil.” 
Assinale a opção que corresponde a uma proposição equivalente, sob o ponto de vista lógico, à 
proposição P6. 
a) Se o investidor ficou receoso e a ação da empresa ficou volátil, houve incerteza sobre os impactos nos 
planos de longo prazo da empresa. 
b) Se o investidor não ficou receoso ou a ação da empresa não ficou volátil, não houve incerteza sobre os 
impactos nos planos de longo prazo. 
c) Se o investidor ficou receoso ou a ação da empresa ficou volátil, houve incerteza sobre os impactos nos 
planos de longo prazo da empresa. 
d) Se não houver incerteza sobre os impactos nos planos de longo prazo da empresa, o investidor não 
ficará receoso e a ação da empresa não ficará volátil. 
e) Houve incerteza sobre os impactos nos planos de longo prazo da empresa, o investidor ficou receoso e a 
ação da empresa ficou volátil. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
100
167


 
Comentários: 
 Sejam as proposições simples: 
i: “Há incerteza sobre os impactos nos planos de longo prazo da empresa.” 
r: “O investidor ficou receoso.” 
v: “A ação da empresa é volátil.” 
A proposição original pode ser descrita por i→(r∧v): 
i→(r∧v): “Se [houver incerteza sobre os impactos nos planos de longo prazo da empresa], [(o investidor 
ficará receoso) e (a ação da empresa ficará volátil)].” 
Existem duas possíveis equivalências para a condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Veja que nas quatro primeiras alternativas temos condicionais, e na última alternativa não temos uma 
disjunção inclusiva “ou”. Logo, devemos utilizar a equivalência contrapositiva, que é a única equivalência 
que transforma uma condicional em outra. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
i→(r∧v) ≡ ~(r∧v)→~i 
O termo ~(r∧v) é a negação da conjunção r∧v. Desenvolvendo por De Morgan, obtemos ~r∨~v. Ficamos 
com: 
i→(r∧v) ≡ (~r∨~v)→~i 
Logo, a proposição equivalente pode ser escrita por: 
(~r∨~v)→~i: "Se [(o investidor não ficou receoso) ou (a ação da empresa não ficou volátil)], [não houve 
incerteza sobre os impactos nos planos de longo prazo].” 
Gabarito: Letra B. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
101
167


 
(CEBRASPE/SEFAZ AC/2024) P2: “Se a demanda pelo produto vendido pela companhia sofre retração, 
no novo equilíbrio de mercado, diminuem seu preço e sua quantidade demandada.” 
Assinale a opção em que é apresentada uma proposição que, sob o ponto de vista lógico, expressa o 
exato significado da proposição P2. 
a) “Se, no novo equilíbrio de mercado, diminuem o preço e a quantidade demandada do produto vendido 
pela companhia, sua demanda sofre retração.” 
b) “Se, no novo equilíbrio de mercado, diminui o preço ou a quantidade demandada do produto vendido 
pela companhia, sua demanda sofre retração.” 
c) “Se a demanda pelo produto vendido pela companhia não sofre retração, no novo equilíbrio de 
mercado, não diminuem seu preço nem sua quantidade demandada.” 
d) “A demanda pelo produto vendido pela companhia sofre retração e, no novo equilíbrio de mercado, 
diminuem seu preço e sua quantidade demandada.” 
e) “A demanda pelo produto vendido pela companhia não sofre retração ou, no novo equilíbrio de 
mercado, diminuem seu preço e sua quantidade demandada.” 
Comentários: 
Sejam as proposições simples: 
r: "A demanda pelo produto vendido pela companhia sofre retração." 
d: "No novo equilíbrio de mercado, diminuem o preço do produto." 
q: "No novo equilíbrio de mercado, diminuem a quantidade demandada do produto." 
Observação: note que “no novo equilíbrio de mercado” é uma circunstância que se refere tanto à 
proposição d quanto à posição q. Essa circunstância poderia ser eliminada da questão sem prejuízo à 
resolução do problema. 
Note que a proposição P2 pode ser descrita por r→(d∨q): 
r→(d∨q): “Se [a demanda pelo produto vendido pela companhia sofre retração], [no novo equilíbrio de 
mercado, (diminuem seu preço) e ((diminuem) sua quantidade demandada)].” 
As alternativas apresentam tanto condicionais (se...então; →) quanto uma disjunção inclusiva (ou; ∨) 
como equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a 
condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
102
167


 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
r→(d∨q) ≡ ~(d∨q)→~r 
O termo ~(d∨q) é a negação da disjunção inclusiva d∨q. Desenvolvendo por De Morgan, obtemos ~d∧~q. 
Ficamos com: 
r→(d∨q) ≡ (~d∧~q)→~r 
A proposição equivalente pode ser descrita por: 
(~d∧~q)→~r: “Se [, no novo equilíbrio de mercado, (não diminuem o preço) e (não diminuem a 
quantidade demandada do produto (vendido pela companhia))], então [sua demanda não sofre retração].” 
Veja que essa equivalência não está nas alternativas apresentadas. 
Vamos agora utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar o seguinte 
procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
r→(d∨q) ≡ ~r∨(d∨q) 
A proposição equivalente pode ser descrita por: 
~r∨(d∨q): “[A demanda pelo produto vendido pela companhia não sofre retração] ou, [no novo equilíbrio 
de mercado, (diminuem seu preço) e ((diminuem) sua quantidade demandada)].” 
Note que essa proposição equivalente está presente na alternativa E. 
Gabarito: Letra E. 
 
(CESPE/FINEP/2024) Assinale a opção que é equivalente a "Se a inflação não reflete o aumento do 
custo de vida do cidadão e os juros básicos da economia caem, a rentabilidade da renda fixa fica 
prejudicada." 
a) Se a rentabilidade da renda fixa fica prejudicada, a inflação não reflete o aumento do custo de vida do 
cidadão e os juros básicos da economia caem. 
b) Quando a rentabilidade da renda fixa fica prejudicada, a inflação não reflete o aumento do custo de vida 
do cidadão e os juros básicos da economia caem. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
103
167


 
c) Se a inflação reflete o aumento do custo de vida do cidadão ou os juros básicos da economia não caem, a 
rentabilidade da renda fixa não fica prejudicada. 
d) A inflação reflete o aumento do custo de vida do cidadão, os juros básicos da economia não caem ou a 
rentabilidade da renda fixa fica prejudicada. 
e) A inflação não reflete o aumento do custo de vida do cidadão e os juros básicos da economia caem, mas 
a rentabilidade da renda fixa não fica prejudicada. 
Comentários: 
Sejam as proposições simples: 
i: "A inflação reflete o aumento do custo de vida do cidadão." 
j: "Os juros básicos da economia caem" 
r: "A rentabilidade da renda fixa fica prejudicada" 
A proposição do enunciado corresponde a (~i∧j)→r: 
(~i∧j)→r: "Se [(a inflação não reflete o aumento do custo de vida do cidadão) e (os juros básicos da 
economia caem)], (então) [a rentabilidade da renda fixa fica prejudicada]." 
As alternativas apresentam tanto condicionais (se...então; →) quanto uma disjunção inclusiva (ou; ∨) 
como equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a 
condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
(~i∧j)→r ≡ ~r→~(~i∧j) 
A negação da conjunção (~i∧j), dada por ~(~i∧j), pode ser desenvolvida por De Morgan, obtendo-se i∨~j. 
Ficamos com: 
(~i∧j)→r ≡ ~r→(i∨~j) 
Logo, uma possível equivalência é: 
~r→(i∨~j): "Se [a rentabilidade da renda fixa não fica prejudicada], então [(a inflação reflete o aumento 
do custo de vida do cidadão) ou (os juros básicos da economia não caem)]." 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
104
167


 
Veja que essa equivalência não está nas alternativas apresentadas. 
Vamos agora utilizar a segunda equivalência. Para aplicar essa equivalência, devemos realizar o seguinte 
procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
(~i∧j)→r ≡ ~(~i∧j)∨r 
A negação da conjunção (~i∧j), dada por ~(~i∧j), pode ser desenvolvida por De Morgan, obtendo-se i∨~j. 
Ficamos com: 
(~i∧j)→r ≡ (i∨~j)∨r 
Logo, a proposição equivalente pode ser descrita por: 
(i∨~j)∨r: "(A inflação reflete o aumento do custo de vida do cidadão) ou (os juros básicos da economia não 
caem) ou (a rentabilidade da renda fixa fica prejudicada)." 
A alternativa D apresenta essa proposição omitindo o primeiro "ou". Na redação da alternativa, devemos 
entender que temos um conectivo "ou" implícito. Esse recurso de se omitir o conectivo foi utilizado para 
evitar a repetição excessiva do conectivo "ou". 
(i∨~j)∨r: "(A inflação reflete o aumento do custo de vida do cidadão), (ou) (os juros básicos da economia 
não caem) ou (a rentabilidade da renda fixa fica prejudicada)." 
Gabarito: Letra D. 
 
(CESPE/Itaipu Binacional/2024) “O chefe não me falou sobre isso, mas, se eu for convidado, aceitarei 
a tarefa.” 
Assinale a opção que apresenta uma negação da proposição anterior. 
a) O chefe me falou sobre isso, ou serei convidado, mas não aceitarei a tarefa. 
b) O chefe me falou sobre isso, mas, se eu não for convidado, não aceitarei a tarefa. 
c) O chefe me falou sobre isso, mas não fui convidado ou não aceitei a tarefa. 
d) O chefe me falou sobre isso, serei convidado, mas não aceitarei a tarefa. 
e) O chefe me falou sobre isso ou eu não serei convidado ou não aceitarei a tarefa. 
Comentários: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
105
167


 
Sejam as proposições simples: 
f: "O chefe me falou sobre isso." 
c: "Eu fui convidado." 
a: "Aceitarei a tarefa". 
Sabemos que o conectivo "mas" corresponde à conjunção "e". Logo, a proposição original pode ser 
descrita por ~f∧(c→a): 
~f∧(c→a): “[O chefe não me falou sobre isso], mas, [se (eu for convidado), (então) (aceitarei a tarefa)].” 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~[~f∧(c→a)] ≡ ~(~f)∨~(c→a) 
Note que: 
• A dupla negação de f, dada por ~(~f), corresponde à proposição f; e 
• A negação da condicional (c→a), dada por ~(c→a), corresponde a c∧~a. 
Logo, ficamos com: 
~[~f∧(c→a)] ≡ f∨(c∧~a) 
 
Portanto, a negação da proposição original pode ser descrita por: 
f∨(c∧~a): "[O chefe me falou sobre isso], ou [(serei convidado), mas (não aceitarei a tarefa)]." 
Gabarito: Letra A. 
 
(CESPE/CGE RJ/2024) A negação do trecho ‘se você acredita, não precisa de explicação; se você não 
acredita, não adianta explicação’ pode ser expressa corretamente por ‘você acredita, mas precisa de 
explicação, ou você não acredita, mas adianta explicação’. 
Comentários: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
106
167


 
Sejam as proposições simples: 
𝒂𝒄: "Você acredita." 
𝒑𝒆: "Precisa de explicação." 
𝒂𝒆: "Adianta explicação." 
Note que a proposição composta do enunciado pode ser descrita por (𝒂𝒄→~𝒑𝒆) ∧(~𝒂𝒄→~𝒂𝒆): 
(𝒂𝒄→~𝒑𝒆) ∧(~𝒂𝒄→~𝒂𝒆): "[Se (você acredita), (não precisa de explicação)]; (e) [se (você não acredita), 
(não adianta explicação)]." 
Para negar a conjunção entre os termos (𝒂𝒄→~𝒑𝒆) e (~𝒂𝒄→~𝒂𝒆), podemos utilizar De Morgan: 
negam-se ambas as parcelas e troca-se o "e" pelo "ou". Ficamos com: 
~[(𝒂𝒄→~𝒑𝒆) ∧(~𝒂𝒄→~𝒂𝒆)] ≡ ~(𝒂𝒄→~𝒑𝒆)∨~(~𝒂𝒄→~𝒂𝒆) 
Note que obtivemos a negação da condicional (𝒂𝒄→~𝒑𝒆) e a negação da condicional (~𝒂𝒄→~𝒂𝒆). 
Para negar a condicional, utiliza-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa equivalência, devemos 
realizar o seguinte procedimento: 
• Mantém-se o primeiro termo; 
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Logo: 
• 
~(𝒂𝒄→~𝒑𝒆) ≡ 𝒂𝒄∧~(~𝒑𝒆) 
• 
~(~𝒂𝒄→~𝒂𝒆) ≡ ~𝒂𝒄∧~(~𝒂𝒆) 
A dupla negação de 𝒑𝒆 corresponde à proposição 𝒑𝒆, e a dupla negação de 𝒂𝒄 corresponde à proposição 
𝒂𝒄. Ficamos com: 
• 
~(𝒂𝒄→~𝒑𝒆) ≡ 𝒂𝒄∧𝒑𝒆 
• 
~(~𝒂𝒄→~𝒂𝒆) ≡ ~𝒂𝒄∧𝒂𝒆 
Logo, temos a seguinte negação: 
~[(𝒂𝒄→~𝒑𝒆) ∧(~𝒂𝒄→~𝒂𝒆)] ≡ (𝒂𝒄∧𝒑𝒆)∨(~𝒂𝒄∧𝒂𝒆) 
Logo, a negação procurada é: 
(𝒂𝒄∧𝒑𝒆)∨(~𝒂𝒄∧𝒂𝒆): "[(Você acredita) e (precisa de explicação)], ou [(você não acredita) e (adianta 
explicação)]". 
Note que o item apresenta essa negação trocando o "e" pela palavra "mas". Trata-se de outra forma 
correta de se representar a conjunção: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
107
167


 
(𝒂𝒄∧𝒑𝒆)∨(~𝒂𝒄∧𝒂𝒆): "[(Você acredita), mas (precisa de explicação)], ou [(você não acredita), mas 
(adianta explicação)]". 
Gabarito: CERTO. 
 
(CESPE/TCDF/2023) São logicamente equivalentes as sentenças I e II, a seguir. 
I. “Se o governador do DF indicou o presidente do TCDF e a Câmara Legislativa indicou o corregedor, 
então o ouvidor é apreciador de música clássica.” 
II. “Ou o presidente do TCDF não foi indicado pelo governador ou o corregedor não foi indicado pela 
Câmara Legislativa ou o ouvidor é apreciador de música clássica.” 
Comentários: 
Sejam as proposições simples: 
g: "O governador do DF indicou o presidente do TCDF." 
c: "A Câmara Legislativa indicou o corregedor." 
o: "O ouvidor é apreciador de música clássica." 
Note que a sentença I pode ser descrita por (g∧c)→o: 
(g∧c)→o: "Se [(o governador do DF indicou o presidente do TCDF) e (a Câmara Legislativa indicou o 
corregedor)], então [o ouvidor é apreciador de música clássica]." 
Queremos identificar se essa condicional é equivalente à sentença II.  
Veja que a sentença II não apresenta uma condicional como possível equivalente. Logo, não se deve 
utilizar a equivalência contrapositiva, dada por p→q ≡ ~q→~p. 
Outra equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte:              
p→q ≡ ~p∨q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
(g∧c)→o ≡ ~(g∧c)∨o 
Note que ~(g∧c) é uma negação pode ser desenvolvida por De Morgan, correspondendo a ~g∨~c. 
Ficamos com: 
(g∧c)→o ≡ ~g∨~c∨o 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
108
167


 
Logo, a condicional original é equivalente a: 
~g∨~c∨o: "[O governador do DF não indicou o presidente do TCDF] ou [a Câmara Legislativa não indicou o 
corregedor] ou [o ouvidor é apreciador de música clássica]." 
Observe, ainda, que: 
• "O presidente do TCDF foi indicado pelo governador" é uma proposição simples que apresenta o 
mesmo sentido de "O governador do DF indicou o presidente do TCDF." Logo, essa proposição 
pode ser representada pela letra g. 
• "O corregedor foi indicado pela Câmara Legislativa" é uma proposição simples que apresenta o 
mesmo sentido de "A Câmara Legislativa indicou o corregedor." Logo, essa proposição pode ser 
representada pela letra c. 
Consequentemente, a equivalência da condicional original pode ser escrita assim: 
~g∨~c∨o: "[O presidente do TCDF não foi indicado pelo governador] ou [o corregedor não foi indicado 
pela Câmara Legislativa] ou [o ouvidor é apreciador de música clássica]." 
Note que a sentença II se assemelha muito à equivalência obtida, exceto pelo fato de haver um "ou" extra 
no início dela: 
"Ou [o presidente do TCDF não foi indicado pelo governador] ou [o corregedor não foi indicado pela 
Câmara Legislativa] ou [o ouvidor é apreciador de música clássica]." 
Apesar do "ou" extra no início da sentença, a banca CEBRASPE deu o gabarito como CERTO, indicando que 
as sentenças I e II são equivalentes.  
Entendo que o primeiro "ou" prejudica o julgamento da questão, pois poderia ser interpretado uma 
disjunção exclusiva (ou...ou) entre ~g e ~c ou entre ~c e o. Consequentemente, poderíamos entender 
que a sentença II se trata da proposição ~g∨~c∨o ou da proposição ~g∨~c∨o, que não são equivalentes à 
sentença I. 
Gabarito: CERTO. 
 
CEBRASPE - Outras equivalências e negações  
(CESPE/PETROBRAS/2022) Acerca de lógica matemática, julgue o item a seguir. 
Dadas três proposições p, q e r, tem-se que p∨q→r é equivalente a (p→r)∨(q→r). 
Comentários: 
Na teoria da aula, aprendemos duas equivalências relacionadas à conjunção de condicionais. Para resolver 
essa questão, teríamos que conhecer a seguinte equivalência: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
109
167


 
(p→r)∧(q→r) ≡ (p∨q)→r 
Note que a questão sugere que (p∨q)→r é equivalente a (p→r)∨(q→r). O gabarito, portanto, é ERRADO. 
Outra forma de resolver o problema sem conhecer a equivalência supracitada é desenhar as tabelas-
verdade de p∨q→r e de (p→r)∨(q→r). Como as tabelas-verdade não são iguais, as proposições compostas 
não são equivalentes. 
 
Gabarito: ERRADO. 
 
 (CESPE/TCE-RS/2013) Com base na proposição P: “Quando o cliente vai ao banco solicitar um 
empréstimo, ou ele aceita as regras ditadas pelo banco, ou ele não obtém o dinheiro”, julgue o item que 
se segue. 
A negação da proposição “Ou o cliente aceita as regras ditadas pelo banco, ou o cliente não obtém o 
dinheiro” é logicamente equivalente a “O cliente aceita as regras ditadas pelo banco se, e somente se, o 
cliente não obtém o dinheiro” 
Comentários: 
Sejam as proposições simples: 
p: "O cliente aceita as regras ditadas pelo banco." 
q: "O cliente não obtém o dinheiro." 
A proposição a ser negada é p∨q. Sabemos que a negação da disjunção exclusiva é a bicondicional: 
~ (p∨q) ≡ pq 
A bicondicional pode ser descrita por: 
"[O cliente aceita as regras ditadas pelo banco] se, e somente se, [o cliente não obtém o dinheiro].” 
Gabarito: CERTO. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
110
167


 
FCC 
FCC - Equivalências Fundamentais 
(FCC/SEFAZ BA/2019) Em seu discurso de posse, determinado prefeito afirmou: “Se há incentivos 
fiscais, então as empresas não deixam essa cidade”. Considerando a afirmação do prefeito como 
verdadeira, então também é verdadeiro afirmar: 
a) Se não há incentivos fiscais, então as empresas deixam essa cidade. 
b) Se as empresas não deixam essa cidade, então há incentivos fiscais. 
c) Se as empresas deixam essa cidade, então não há incentivos fiscais. 
d) As empresas deixam essa cidade se há incentivos fiscais. 
e) As empresas não deixam essa cidade se não há incentivos fiscais. 
Comentários: 
Sejam as proposições simples: 
h: "Há incentivos fiscais." 
d: "As empresas deixam essa cidade." 
A afirmação do enunciado é a condicional h→~d: 
h→~d: "Se [há incentivos fiscais], então [as empresas não deixam essa cidade]." 
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p→q ≡ ~q→~p. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
h→~d ≡ ~(~d)→~h 
A dupla negação corresponde à proposição original. Ficamos com: 
h→~d ≡ d→~h 
A proposição equivalente pode ser escrita por: 
d→~h: "Se [as empresas deixam essa cidade], então [não há incentivos fiscais]." 
Gabarito: Letra C. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
111
167


 
(FCC/SEFAZ BA/2019) Suponha que a negação da proposição “Você é a favor da ideologia X” seja 
“Você é contra a ideologia X”. A proposição condicional “Se você é contra a ideologia A, então você é a 
favor da ideologia C” é equivalente a 
a) Você é a favor da ideologia A e você é a favor da ideologia C. 
b) Ou você é a favor da ideologia A ou você é a favor da ideologia C, mas não de ambas. 
c) Você é a favor da ideologia A ou você é contra a ideologia C. 
d) Você é a favor da ideologia A ou você é a favor da ideologia C. 
e) Você é contra a ideologia A e você é contra a ideologia C. 
Comentários: 
Sejam as proposições simples: 
A: "Você é a favor da ideologia A." 
C: "Você é a favor da ideologia C." 
Segundo o enunciado, "você é contra a ideologia A" é a negação da nossa proposição A. Logo, a frase 
original pode ser representada pelo seguinte condicional: 
~A→ C: "Se [você é contra a ideologia A], então [você é a favor da ideologia C]." 
Veja que as alternativas não apresentam uma condicional como equivalente. Logo, não se deve utilizar a 
equivalência contrapositiva, dada por p→q ≡ ~q→~p. 
Uma outra equivalência fundamental que se pode utilizar com o conectivo condicional é a seguinte:              
p→q ≡ ~p∨q. Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
~A→ C ≡ ~(~A) ∨ C 
A dupla negação de uma proposição simples corresponde à proposição original. Logo, a equivalência é 
dada por A∨C: 
A∨C: "Você é a favor da ideologia A ou você é a favor da ideologia C." 
Gabarito: Letra D. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
112
167


 
FCC - Negações Lógicas  
(FCC/TRT 9/2022) A negação da afirmação: “não ficou doente e vai ficar em casa” é: 
a) Ficou doente e não vai ficar em casa. 
b) Não ficou doente ou vai ficar em casa. 
c) Ficou doente ou não vai ficar em casa. 
d) Ficou doente ou vai ficar em casa. 
e) Não ficou doente ou não vai ficar em casa. 
Comentários: 
Sejam as proposições simples: 
d: "Ficou doente." 
c: "Vai ficar em casa." 
A proposição original pode ser escrita pela conjunção ~d∧c:  
~d∧c:"[Não ficou doente] e [vai ficar em casa]." 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~ (~d∧c) ≡ ~(~d)∨~c 
A dupla negação de c corresponde à proposição original. Ficamos com: 
~ (~d∧c) ≡ d∨~c 
Logo, a negação requerida pode ser descrita por:  
d∨~c: “[Ficou doente] ou [não vai ficar em casa].” 
Gabarito: Letra C. 
 
(FCC/IBMEC/2019) Dadas duas proposições lógicas P e Q, então a negação da sentença P ∧ Q é 
equivalente a 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
113
167


 
a) (- P) ∨ (- Q) 
b) (- P) ∧ (- Q) 
c) - (P ∨ Q) 
d) (- P) ∧ Q 
e) P ∧ (- Q) 
Comentários: 
Originalmente, temos a conjunção de P com Q: P∧Q. 
Para negar uma conjunção, devemos utilizar De Morgan: negam-se as duas proposições e troca-se o "e" 
pelo "ou". Logo: 
~(P∧Q) ≡ ~P ∨ ~Q 
Gabarito: Letra A. 
 
(FCC/AFAP/2019) A negação da afirmação condicional “Se Carlos não foi bem no exame, vai ficar em 
casa” é: 
a) Se Carlos for bem no exame, vai ficar em casa. 
b) Carlos foi bem no exame e não vai ficar em casa. 
c) Carlos não foi bem no exame e vai ficar em casa. 
d) Carlos não foi bem no exame e não vai ficar em casa. 
e) Se Carlos não foi bem no exame então não vai ficar em casa. 
Comentários: 
Vamos definir as proposições simples: 
e: "Carlos foi bem no exame." 
c: "Carlos vai ficar em casa." 
A frase original pode ser descrita pelo condicional ~e→c: 
~e→c: "Se [Carlos não foi bem no exame], então [vai ficar em casa]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
114
167


 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(~e→c)  ≡ ~e∧~c 
Logo, a negação pode ser descrita por:  
~e∧~c: "[Carlos não foi bem no exame] e [não vai ficar em casa]." 
Gabarito: Letra D. 
 
 (FCC/SEFAZ-SC/2018) A negação da proposição “se eu estudo, eu cresço” pode ser escrita como: 
a) “se eu não estudo, eu não cresço”.  
b) “se eu não cresço, eu não estudo”.  
c) “cresço e não estudo”.  
d) “estudo e não cresço”.  
e) “se eu cresço, eu não estudo”. 
Comentários: 
Sejam as proposições simples: 
e: "Eu estudo." 
c: "Eu cresço." 
A proposição apresentada é a condicional e→c na forma em que se omite o "então": 
e→c: "Se [eu estudo], [eu cresço]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(e→c) ≡ e∧~c 
Logo, a negação pode ser descrita por:  
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
115
167


 
e∧~c: "[Eu estudo] e [eu não cresço]." 
A alternativa D apresenta essa negação omitindo a palavra "eu". 
Gabarito: Letra D. 
 
FCC - Questões com mais de uma equivalência 
(FCC/Pref. SJRP/2019) Considere a proposição: “Se Alberto está estudando, então é véspera de prova 
ou é dia 29 de fevereiro”. Uma proposição equivalente a essa é 
a) Se Alberto não está estudando, então não é véspera de prova ou não é dia 29 de fevereiro. 
b) Se Alberto não está estudando, então não é véspera de prova e não é dia 29 de fevereiro. 
c) Se é véspera de prova ou é dia 29 de fevereiro, então Alberto está estudando. 
d) Se Alberto está estudando, então é véspera de prova e é dia 29 de fevereiro. 
e) Se não é véspera de prova e não é dia 29 de fevereiro, então Alberto não está estudando. 
Comentários: 
Sejam as proposições simples: 
a: "Alberto está estudando." 
v: "É véspera de prova." 
f: "É dia 29 de fevereiro." 
A proposição do enunciado pode ser descrita por a→ v ∨ f. 
a→ v ∨ f : "Se [Alberto está estudando], então [(é véspera de prova) ou (é dia 29 de fevereiro)]." 
Observe que a proposição do enunciado é uma condicional e as alternativas apresentam condicionais. Isso 
significa que devemos utilizar a contrapositiva p→q ≡ ~q→~p. Para aplicar essa equivalência, devemos 
realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
a→ v ∨ f ≡ ~(v ∨ f ) → ~a 
O antecedente obtido, ~(v∨f), pode ainda ser desenvolvido por De Morgan. Nesse caso, negam-se as duas 
parcelas e troca-se o "ou" pelo "e". Temos: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
116
167


 
a→(v ∨ f ) ≡ ~v ∧~f  → ~a 
A condicional acima pode ser expressa por:  
~v ∧~f → ~a: "Se [(não é véspera de prova) e (não é dia 29 de fevereiro)], então [Alberto não está 
estudando]." 
Gabarito: Letra E. 
 
(FCC/COPERGÁS/2016) Considere a afirmação a seguir: 
Se eu paguei o aluguel ou comprei comida, então o meu salário entrou na conta. 
Uma afirmação equivalente a afirmação anterior é 
a) Se o meu salário não entrou na conta, então eu não paguei o aluguel e não comprei comida. 
b) Se eu paguei o aluguel e comprei comida, então o meu salário entrou na conta. 
c) O meu salário entrou na conta e eu comprei comida e paguei o aluguel. 
d) Se o meu salário não entrou na conta, então eu não paguei o aluguel ou não comprei comida. 
e) Se eu não paguei o aluguel e não comprei comida, então o meu salário não entrou na conta. 
Comentários: 
  Sejam as proposições simples: 
p: "Eu paguei o aluguel." 
c: "Eu comprei comida." 
s: "O meu salário entrou na conta." 
A proposição do enunciado pode ser descrita por p∨c → s. 
p∨c → s: "Se [(eu paguei o aluguel) ou (comprei comida)], então [o meu salário entrou na conta]." 
As duas equivalências fundamentais que envolvem a condicional são: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p ∨ q (transformação da condicional em disjunção inclusiva) 
Note que a alternativa C não apresenta o conectivo "ou" e também não apresenta o conectivo "se... 
então". Portanto, podemos eliminá-la.  
Entre as alternativas que restaram, todas elas apresentam o conectivo "se...então". Nesse caso, devemos 
aplicar a primeira equivalência (contrapositiva). 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
117
167


 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
p∨c → s ≡ ~s→~(p∨c) 
O consequente obtido, ~( p∨c), pode ainda ser desenvolvido por De Morgan. Nesse caso, negam-se as 
duas parcelas e troca-se o "ou" pelo "e". Temos: 
p∨c → s ≡ ~s → ~p∧~c 
A proposição equivalente pode ser descrita por: 
~s → ~p∧~c: "Se [o meu salário não entrou na conta], então [(eu não paguei o aluguel) e (não comprei 
comida)]." 
Gabarito: Letra A. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
118
167


 
VUNESP 
VUNESP - Equivalências Fundamentais 
(VUNESP/Pref Marília/2023) Uma afirmação logicamente equivalente à afirmação: ‘Se você começa, 
então a repetição faz você continuar’, está contida na afirmação 
a) Se você não começa, então a repetição não faz você continuar. 
b) Se a repetição não faz você continuar, então você não começa. 
c) Você começa e a repetição faz você continuar. 
d) Ou você começa ou a repetição faz você continuar. 
e) Se a repetição faz você continuar, então você começa. 
Comentários: 
Sejam as proposições simples: 
c: "Você começa." 
r: "A repetição faz você continuar." 
A proposição original pode ser descrita por c→r: 
c→r: "Se [você começa], então [a repetição faz você continuar]." 
A equivalência contrapositiva é representada do seguinte modo: p→q ≡ ~q→~p. Para aplicar essa 
equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
c→r ≡ ~r→~c 
A proposição equivalente pode ser descrita por: 
~r→~c: "Se [a repetição não faz você continuar], então [você não começa]." 
Gabarito: Letra B. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
119
167


 
(VUNESP/TCM SP/2023) Considere a seguinte afirmação: Hélio é casado ou Luana é solteira. 
Uma equivalência lógica para a proposição apresentada está contida na alternativa: 
a) Se Hélio não é casado, então Luana é solteira. 
b) Hélio e Luana são solteiros. 
c) Se Hélio é solteiro, então Luana é casada. 
d) Hélio e Luana são casados. 
e) Se Hélio é casado, então Luana não é solteira. 
Comentários: 
Sejam as proposições simples: 
h: "Hélio é casado." 
l: "Luana é solteira." 
A afirmação do enunciado pode ser escrita por: h∨l:  
h∨l: "[Hélio é casado] ou [Luana é solteira]." 
Para transformar a disjunção inclusiva em uma condicional, podemos usar a equivalência p∨q ≡~p→q. Para 
aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a disjunção inclusiva (∨) pela condicional (→); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
h∨l ≡ ~h→l 
A condicional obtida pode ser descrita por: 
~h→l: "Se [Hélio não é casado], então [Luana é solteira]." 
Gabarito: Letra A. 
 
(VUNESP/TJ SP/2022) Uma equivalente lógica para a proposição “Se eu me cuido, então sou 
saudável” está contida na alternativa: 
a) Eu não me cuido e não sou saudável. 
b) Se sou saudável, então eu me cuido. 
c) Eu não me cuido ou sou saudável. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
120
167


 
d) Sou saudável e eu não me cuido. 
e) Eu me cuido e sou saudável. 
Comentários: 
Sejam as proposições simples: 
c: "Eu me cuido." 
s: "Sou saudável." 
A proposição original pode ser descrita por c→s: 
c→s: "Se [eu me cuido], então [sou saudável]." 
As alternativas apresentam tanto uma condicional (→) quanto uma disjunção inclusiva ("ou", ∨) como 
equivalentes. Devemos, portanto, testar as duas equivalências fundamentais que envolvem a condicional: 
• p→q ≡ ~q→~p (contrapositiva) 
• p→q ≡ ~p∨q (transformação da condicional em disjunção inclusiva) 
Para aplicar a primeira equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
c→s ≡ ~s→~c 
A proposição equivalente pode ser descrita por: 
~s→~c: "Se [não sou saudável], então [não me cuido]." 
Veja que não temos essa equivalência nas alternativas. Portanto, vamos utilizar a segunda equivalência.  
Para aplicar a segunda equivalência, devemos realizar o seguinte procedimento: 
• Nega-se o primeiro termo;  
• Troca-se a condicional (→) pela disjunção inclusiva (∨); e 
• Mantém-se o segundo termo. 
Para o caso em questão, temos: 
c→s ≡ ~c∨s 
A proposição equivalente pode ser descrita por: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
121
167


 
~c∨s: "[Eu não me cuido] ou [sou saudável]." 
Veja que essa equivalência está presente na alternativa C. 
Gabarito: Letra C. 
 
VUNESP - Negações Lógicas  
(VUNESP/TCM SP/2023) Considere a seguinte afirmação: Se Júnior é auxiliar técnico de controle 
externo, então ele prestou um concurso. 
Assinale a alternativa que contém uma correta negação lógica para a afirmação apresentada. 
a) Júnior é auxiliar técnico de controle externo e ele não prestou um concurso. 
b) Se Júnior não é auxiliar técnico de controle externo, então ele não prestou um concurso. 
c) Júnior não é auxiliar técnico de controle externo, mas ele prestou um concurso. 
d) Se Júnior não prestou um concurso, então ele não é auxiliar técnico de controle externo. 
e) Júnior não é auxiliar técnico de controle externo e não prestou um concurso. 
Comentários: 
Sejam as proposições simples: 
a: "Júnior é auxiliar técnico de controle externo." 
p: "Júnior prestou um concurso." 
A proposição original é dada por a→p:  
a→p: "Se [Júnior é auxiliar técnico de controle externo], então [ele prestou um concurso]." 
Para realizar a negação de uma condicional, usa-se a equivalência ~(p→q) ≡ p∧~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Mantém-se o primeiro termo;  
• Troca-se a condicional (→) pela conjunção (∧); e 
• Nega-se o segundo termo. 
Para o caso em questão, temos: 
~(a→p) ≡ a∧~p 
Logo, a negação pode ser descrita por:  
a∧~p: "[Júnior é auxiliar técnico de controle externo] e [ele não prestou um concurso]." 
Gabarito: Letra A. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
122
167


 
(VUNESP/PC SP/2022) Considere a afirmação: 
‘As camisas estão passadas e os sapatos não estão engraxados’. 
Uma afirmação que corresponde à negação lógica desta, é: 
a) As camisas estão passadas ou os sapatos estão engraxados. 
b) Ou as camisas estão passadas ou os sapatos não estão engraxados. 
c) As camisas não estão passadas e os sapatos estão engraxados. 
d) As camisas não estão passadas e os sapatos não estão engraxados. 
e) As camisas não estão passadas ou os sapatos estão engraxados. 
Comentários: 
Sejam as proposições simples: 
c: "As camisas estão passadas." 
s: "Os sapatos estão engraxados." 
A proposição original pode ser escrita pela conjunção c∧~s:  
c∧~s: “[As camisas estão passadas] e [os sapatos não estão engraxados].” 
Para realizar a negação de uma conjunção, usa-se a equivalência ~(p∧q) ≡ ~p∨~q. Para aplicar essa 
equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da conjunção; 
• Troca-se a conjunção (∧) pela disjunção inclusiva (∨). 
Em outras palavras, negam-se as duas proposições e troca-se o "e" pelo "ou". Para o caso em questão, 
temos: 
~(c∧~s) ≡ ~c∨~(~s) 
A dupla negação de s corresponde à proposição original. Ficamos com: 
~(c∧~s) ≡ ~c∨s 
Logo, a negação requerida pode ser descrita por:  
~c∨s: "[As camisas não estão passadas] ou [os sapatos estão engraxados]." 
Gabarito: Letra E. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
123
167


 
(VUNESP/PC SP/2022) Em certo dia, Estela afirmou para sua mãe, Marília: 
– Eu não estou doente ou eu fiz a lição de casa. 
Marília sabe que essa afirmação é falsa, logo conclui-se que Estela 
a) está doente se e somente se fez a lição de casa. 
b) se não está doente, então fez a lição de casa. 
c) está doente ou não fez a lição de casa. 
d) está doente e não fez a lição de casa. 
e) está doente se e somente se não fez a lição de casa. 
Comentários: 
Sejam as proposições simples: 
d: "Eu estou doente." 
f: "Eu fiz a lição de casa." 
A fala de Estela pode ser descrita por ~d∨f: 
~d∨f: "[Eu não estou doente] ou [eu fiz a lição de casa]." 
Como a afirmação é falsa, pode-se concluir corretamente a negação de ~d∨f. Devemos, portanto, negar 
~d∨f. 
Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(p∨q) ≡ ~p∧~q. Para aplicar 
essa equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da disjunção inclusiva; 
• Troca-se a disjunção inclusiva (∨) pela conjunção (∧). 
Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão, 
temos: 
~(~d∨f) ≡ ~(~d)∧~f 
A dupla negação de d corresponde à proposição original. Ficamos com: 
~(~d∨f) ≡ d∧~f 
Logo, a negação requerida pode ser descrita por: 
d∧~f: "[Eu estou doente] e [não fiz a lição de casa]". 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
124
167


 
Portanto, conclui-se corretamente que Estela está doente e não fez a lição de casa. 
Gabarito: Letra D. 
 
VUNESP - Questões com mais de uma equivalência 
(VUNESP/TCM SP/2023) Considere a seguinte afirmação: Se Carlos é médico, então Selma é auditora 
de controle externo e André é auxiliar técnico de controle externo. 
Assinale a alternativa que contém uma equivalência lógica para a afirmação apresentada. 
a) Se Selma não é auditora de controle externo e André não é auxiliar técnico de controle externo, então 
Carlos não é médico. 
b) Se André não é auxiliar técnico de controle externo ou Selma não é auditora de controle externo, então 
Carlos não é médico. 
c) Carlos é médico e Selma é auditora de controle externo, e André é auxiliar técnico de controle externo. 
d) Carlos é médico, mas André não é auxiliar técnico de controle externo ou Selma não é auditora de 
controle externo. 
e) Carlos é médico, mas Selma não é auditora de controle externo e André não é auxiliar técnico de 
controle externo. 
Comentários: 
Considere as seguintes proposições simples: 
c: "Carlos é médico." 
s: "Selma é auditora de controle externo." 
a: "André é auxiliar técnico de controle externo." 
A afirmação do enunciado pode ser modelada por c→(s∧a).  
c→(s∧a): "Se [Carlos é médico], então [(Selma é auditora de controle externo) e (André é auxiliar técnico 
de controle externo)]." 
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p→q ≡ ~q→~p. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
c→(s∧a) ≡ ~(s∧a)→~c 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
125
167


 
O antecedente obtido, ~(s∧a), pode ainda ser desenvolvido por De Morgan. Nesse caso, negam-se as duas 
parcelas e troca-se o "e" pelo "ou". Temos: 
c→(s∧a) ≡ (~s∨~a)→~c 
A proposição equivalente pode ser escrita por: 
(~s∨~a)→~c: "Se [(André não é auxiliar técnico de controle externo) ou (Selma não é auditora de controle 
externo)], então [Carlos não é médico]." 
Gabarito: Letra B. 
 
(VUNESP/ALESP/2022) Uma afirmação que corresponde à negação lógica da afirmação: “Troveja e 
chove muito, ou o dia está lindo”, é: 
a) Não troveja e não chove muito, ou o dia não está lindo. 
b) Não troveja ou chove muito, ou o dia está lindo. 
c) Não troveja ou não chove muito, e o dia não está lindo. 
d) Troveja ou chove muito, e o dia não está lindo. 
e) Troveja ou não chove muito, e o dia está lindo. 
Comentários: 
Considere as seguintes proposições simples: 
t: "Troveja" 
c: "Chove muito." 
d: "O dia está lindo." 
A afirmação do enunciado pode ser modelada por (t∧c)∨d: 
(t∧c)∨d: “[(Troveja) e (chove muito)], ou [o dia está lindo].” 
Note que temos uma disjunção inclusiva "ou" entre a proposição composta (t∧c) e a proposição simples d. 
Para realizar a negação de uma disjunção inclusiva, usa-se a equivalência ~(p∨q) ≡ ~p∧~q. Para aplicar 
essa equivalência, devemos seguir o seguinte procedimento: 
• Negam-se ambas as parcelas da disjunção inclusiva; 
• Troca-se a disjunção inclusiva (∨) pela conjunção (∧). 
Em outras palavras, negam-se as duas proposições e troca-se o "ou" pelo "e". Para o caso em questão, 
temos: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
126
167


 
~[(t∧c)∨d] ≡ ~(t∧c)∧~d 
Note que ~(t∧c) é a negação da conjunção t∧c. Para negar a conjunção, negam-se as duas proposições e 
troca-se o "e" pelo "ou", obtendo-se ~t∨~c. Logo, a negação da nossa proposição original fica assim: 
~[(t∧c)∨d] ≡ (~t∨~c)∧~d 
Portanto, a negação procurada é: 
(~t∨~c)∧~d: "[(Não troveja) ou (não chove muito)], e [o dia não está lindo]." 
Gabarito: Letra C. 
 
(VUNESP/PC SP/2022) Assinale a alternativa que apresenta uma afirmação logicamente equivalente à 
seguinte afirmação: 
‘Se os catadores coletaram todas as latinhas, então a sacola arrebenta ou fica pesada’ 
a) Os catadores coletaram todas as latinhas e a sacola arrebenta e fica pesada. 
b) A sacola arrebenta ou fica pesada e os catadores coletaram todas as latinhas. 
c) Se a sacola não arrebenta e fica pesada, então os catadores não coletaram todas as latinhas. 
d) Se a sacola arrebenta e não fica pesada, então os catadores coletaram todas as latinhas. 
e) Se a sacola não arrebenta e não fica pesada, então os catadores não coletaram todas as latinhas. 
Comentários: 
Sejam as proposições simples: 
c: "Os catadores coletaram todas as latinhas." 
a: "A sacola arrebenta." 
p: "A sacola fica pesada." 
A afirmação do enunciado pode ser modelada por c→(a∨p).  
c→(a∨p): "Se [os catadores coletaram todas as latinhas], então [(a sacola arrebenta) ou ((a sacola) fica 
pesada)]." 
Uma equivalência fundamental envolvendo o conectivo condicional é a contrapositiva: p→q ≡ ~q→~p. 
Para aplicar essa equivalência, devemos realizar o seguinte procedimento: 
• Invertem-se as posições do antecedente e do consequente; e 
• Negam-se ambos os termos da condicional. 
Para o caso em questão, temos: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
127
167


 
c→(a∨p) ≡ ~(a∨p)→~c 
O antecedente obtido, ~(a∨p), pode ainda ser desenvolvido por De Morgan. Nesse caso, negam-se as duas 
parcelas e troca-se o "ou" pelo "e". Temos: 
c→(a∨p) ≡ (~a∧~p)→~c 
Logo, a proposição equivalente pode ser escrita por: 
(~a∧~p)→~c: "Se [(a sacola não arrebenta) e ((a sacola) não fica pesada)], então [os catadores não 
coletaram todas as latinhas]." 
Gabarito: Letra E. 
 
VUNESP - Outras equivalências e negações  
(VUNESP/TCM SP/2023) Uma negação lógica para a afirmação “Sou feliz se, e somente se, você é 
feliz” está contida na alternativa: 
a) Não sou feliz se, e somente se, você não é feliz. 
b) Se eu não sou feliz, então você não é feliz. 
c) Se você não é feliz, então eu não sou feliz. 
d) Sou feliz e você não é feliz. 
e) Ou eu sou feliz, ou você é feliz. 
Comentários: 
Considere as seguintes proposições simples: 
s: "Eu sou feliz." 
v: "Você é feliz." 
A proposição original é dada pela bicondicional sv: 
sv: "[Sou feliz] se, e somente se, [você é feliz]." 
Queremos a negação lógica da bicondicional. Uma das formas de se negar a bicondicional é por meio da 
disjunção exclusiva: ~(pq) ≡ p∨q. Para o caso em questão, temos: 
~(sv) ≡ s∨v 
Logo, a negação procurada é: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
128
167


 
s∨v: "Ou [eu sou feliz], ou [você é feliz]." 
Gabarito: Letra E. 
  
(VUNESP/CMSJC/2022) Considere a afirmação: "Ou arranjo emprego ou não me caso". A negação 
dessa afirmação é: 
a) Se eu arranjo emprego, então eu me caso. 
b) Se eu não arranjo emprego, então eu me caso. 
c) Ou não arranjo emprego ou me caso. 
d) Ou não arranjo emprego ou não me caso. 
e) Arranjo emprego e não me caso. 
Comentários: 
Considere as proposições simples: 
a: "Arranjo emprego." 
c: "Me caso." 
A afirmação original é uma disjunção exclusiva (ou...ou) representada por a∨~c: 
a∨~c: " Ou [arranjo emprego] ou [não me caso]." 
Para a questão em tela, devemos negar a disjunção exclusiva a∨~c. A principal forma de se negar uma 
disjunção exclusiva é por meio da bicondicional, fazendo uso da seguinte equivalência: 
~(p∨q) ≡ pq 
Note que nas alternativas não temos nenhuma bicondicional. Portanto, não devemos utilizar essa forma 
de se negar. 
Para a bicondicional, sabemos que ao negar apenas um dos termos, temos uma negação. Por exemplo, 
temos as seguintes negações de pq: 
~(pq) ≡ ~pq 
~(pq) ≡ p~q 
Para a disjunção exclusiva, temos a mesma ideia: ao negar um dos termos da disjunção exclusiva, temos a 
negação dela. Por exemplo, temos as seguintes negações de p∨q: 
~(p∨q) ≡ ~p∨q 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
129
167


 
~(p∨q) ≡ p∨~q 
Portanto, para negar a∨~c, temos também as seguintes possibilidades: 
~(a∨~c) ≡ ~a∨~c 
~(a∨~c) ≡ a∨~(~c) 
Para a segunda possibilidade, como temos a dupla negação de c, ficamos com: 
~(a∨~c) ≡ a∨c 
Vamos expressar as duas negações de a∨~c: 
~a∨~c: "Ou [não arranjo emprego] ou [não me caso]." 
a∨c: "Ou [arranjo emprego] ou [me caso]." 
Veja que a primeira negação está presente na alternativa D, que é o gabarito da questão. 
Gabarito: Letra D. 
 
(VUNESP/ISS Mogi das Cruzes/2021) Sabe-se que não é verdade que, ou José é rico ou Paula é pobre. 
Sendo assim, é correto afirmar que 
a) José é rico se, e somente se, Paula é pobre. 
b) Se José é rico, então Paula é pobre. 
c) Se Paula é pobre, então José é rico. 
d) José e Paula são ricos. 
e) Paula e José são pobres. 
Comentários: 
Considere as seguintes proposições simples: 
j: "José é rico." 
p: "Paula é pobre." 
Note que a proposição original é a negação da disjunção exclusiva j∨p: 
~(j∨p): "Não é verdade que, [ou (José é rico) ou (Paula é pobre)]" 
Em resumo, queremos uma proposição equivalente a ~(j∨p), ou seja, queremos a negação de j∨p. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
130
167


 
Podemos negar a disjunção exclusiva por meio da bicondicional: ~(p∨q) ≡ pq. Para o caso em questão, 
temos: 
~(j∨p) ≡ jp 
Ficamos com: 
jp: "[José é rico] se, e somente se, [Paula é pobre]." 
Portanto, é correto afirmar que José é rico se, e somente se, Paula é pobre. 
Gabarito: Letra A. 
 
(VUNESP/TJ SP/2021) Uma afirmação equivalente à afirmação “Se Alice estuda, então ela faz uma boa 
prova, e se Alice estuda, então ela não fica triste” é 
a) Se Alice estuda, então ela não faz uma boa prova ou ela fica triste. 
b) Se Alice fica triste e não faz uma boa prova, então ela não estuda. 
c) Se Alice estuda, então ela faz uma boa prova e ela não fica triste. 
d) Alice estuda e ela faz uma boa prova e não fica triste. 
e) Alice não estuda, e ela faz uma boa prova ou não fica triste. 
Comentários: 
Considere as seguintes proposições simples: 
e: "Alice estuda." 
p: "Alice faz uma boa prova." 
t: "Alice fica triste." 
A afirmação presente no enunciado é dada por (e→p)∧(e→~t): 
(e→p)∧(e→~t): “(Se [Alice estuda], então [ela faz uma boa prova]), e (se [Alice estuda], então [ela não fica 
triste]).” 
Note que temos uma conjunção de condicionais em que o termo comum é o antecedente e. Logo, 
devemos utilizar a seguinte equivalência: 
(p→q)∧(p→r) ≡ p→(q∧r) 
Aplicando essa equivalência para o caso em questão, temos: 
(e→p)∧(e→~t) ≡ e→(p∧~t) 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
131
167


 
Portanto, temos a seguinte proposição equivalente: 
e→(p∧~t): "Se [Alice estuda], então [(ela faz uma boa prova) e (ela não fica triste)]." 
Gabarito: Letra C. 
  
 (VUNESP/EBSERH/2020) Uma correta negação lógica para a afirmação “Rosana é vulnerável ou 
necessitada, mas não ambos” está contida na alternativa: 
a) Rosana é vulnerável se, e somente se, ela é necessitada. 
b) Rosana não é vulnerável se, e somente se, ela é necessitada. 
c) Rosana é vulnerável e necessitada. 
d) Rosana não é vulnerável e, tampouco, necessitada. 
e) Se Rosana não é necessitada, então ela não é vulnerável. 
Comentários: 
Vamos definir as proposições simples: 
p: "Rosana é vulnerável." 
q: "Rosana é necessitada." 
Nesse caso, a afirmação é uma disjunção exclusiva dada por p∨q. 
"[Rosana é vulnerável] ou [necessitada], mas não ambos." 
Sabemos que a negação da disjunção exclusiva é a bicondicional, isto é: 
~(p∨q) ≡ pq 
Logo, a negação requerida é: 
pq: "[Rosana é vulnerável] se, e somente se, [ela é necessitada]." 
Gabarito: Letra A. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
132
167


 
QUESTÕES COMENTADAS - MULTIBANCAS 
Álgebra de proposições 
(FUNATEC/Pref. V do Mearim/2026) Assinale corretamente a negação da seguinte proposição lógica. 
“João é bom em matemática se, e somente se, Maria é boa em português.” 
a) João é bom em matemática e Maria não é boa em português ou João não é bom em matemática e Maria 
é boa em português. 
b) João é bom em matemática e Maria é boa em português ou João não é bom em matemática e Maria é 
boa em português. 
c) João não é bom em matemática e Maria não é boa em português ou João é bom em matemática e Maria 
não é boa em português. 
d) João não é bom em matemática se, e somente se, Maria não é boa em português. 
Comentários: 
Sejam as proposições simples: 
j: "João é bom em matemática." 
m: "Maria é boa em português." 
A proposição original pode ser descrita pela bicondicional j↔m: 
j↔m: "[João é bom em matemática] se, e somente se, [Maria é boa em português]". 
Para realizar a negação de uma bicondicional, podemos utilizar a seguinte equivalência: 
~(p↔q) ≡ (p∧~q)∨(q∧~p) 
Aplicando essa equivalência à proposição original, ficamos com: 
~(j↔m) ≡ (j∧~m)∨(m∧~j) 
Aplicando a propriedade comutativa para a conjunção, podemos escrever m∧~j como ~j∧m. Ficamos com: 
~(j↔m) ≡ (j∧~m)∨(~j∧m) 
Logo, a negação pode ser descrita por: 
(j∧~m)∨(~j∧m): "[João é bom em matemática] e [Maria não é boa em português] ou [João não é bom em 
matemática] e [Maria é boa em português]". 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
133
167


 
Veja que essa negação coincide com a alternativa A. 
Gabarito: Letra A. 
(COPS UEL/CM Londrina/2026) Considere as proposições simples e a proposição composta a seguir. 
• p: O computador foi atualizado. 
• q: A impressora imprimiu corretamente. 
• Proposição composta: ~p→(p∨q) 
Sobre essas condições, assinale a alternativa que apresenta, corretamente, uma proposição logicamente 
equivalente a essa, em língua portuguesa. 
a) O computador não foi atualizado ou a impressora imprimiu corretamente. 
b) O computador não foi atualizado e a impressora imprimiu corretamente. 
c) O computador não foi atualizado e a impressora não imprimiu corretamente. 
d) O computador foi atualizado ou a impressora imprimiu corretamente. 
e) O computador foi atualizado e a impressora não imprimiu corretamente. 
Comentários: 
A proposição composta é a condicional ~p→(p∨q). 
Para encontrar a proposição equivalente em linguagem natural, vamos transformar essa condicional em 
uma disjunção inclusiva, utilizando a equivalência p→q ≡ ~p∨q. Para aplicar essa equivalência, devemos: 
• Negar o primeiro termo; 
• Trocar a condicional (→) pela disjunção inclusiva (∨); e 
• Manter o segundo termo. 
Para o caso em questão, temos: 
~p→(p∨q) ≡ ~(~p)∨(p∨q) 
Pela dupla negação, ~(~p) ≡ p. Ficamos com: 
~p→(p∨q) ≡ p∨(p∨q) 
Pela propriedade associativa, podemos alterar a posição dos parênteses da sequência de disjunções: 
~p→(p∨q) ≡ (p∨p)∨q 
Pela propriedade de idempotência da disjunção inclusiva (p∨p ≡ p), ficamos com: 
~p→(p∨q) ≡ p∨q 
Logo, a proposição equivalente em linguagem natural é: 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
134
167


 
p∨q: "[O computador foi atualizado] ou [a impressora imprimiu corretamente]". 
Veja que essa equivalência coincide com a alternativa D. 
Gabarito: Letra D. 
(FEPESE/Pref. Campos Novos/2026) Em um sistema de controle de acesso, utiliza-se a seguinte regra: 
“Se o funcionário não apresentou identificação, então o acesso é bloqueado.” 
O gestor deseja substituir essa frase por outra logicamente equivalente, mantendo exatamente o mesmo 
sentido lógico, mas escrita de forma direta e sem a estrutura de “se… então”. 
Qual das alternativas abaixo expressa uma frase logicamente equivalente à regra original? 
a) O acesso é bloqueado somente quando o funcionário apresenta identificação. 
b) O acesso nunca é bloqueado quando o funcionário não apresenta identificação. 
c) O acesso é sempre bloqueado, independentemente da apresentação de identificação. 
d) Somente funcionários com identificação têm acesso bloqueado. 
e) O acesso é bloqueado quando o funcionário não apresenta identificação, ou o funcionário apresenta 
identificação. 
Comentários: 
Sejam as proposições simples: 
i: "O funcionário apresenta identificação." 
b: "O acesso é bloqueado." 
A regra original é a condicional ~i→b: 
~i→b: "Se [o funcionário não apresenta identificação], então [o acesso é bloqueado]". 
Vamos analisar a alternativa E. 
e) O acesso é bloqueado quando o funcionário não apresenta identificação, ou o funcionário apresenta 
identificação. 
A primeira parcela, "(O acesso é bloqueado) quando (o funcionário não apresenta identificação)", segue a 
estrutura "q, quando p", que equivale à condicional p→q. Logo, essa parcela corresponde à condicional 
~i→b, ou seja, à própria regra original. 
A segunda parcela, "o funcionário apresenta identificação", corresponde à proposição simples i. 
Portanto, a alternativa E pode ser descrita por (~i→b)∨i:  
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
135
167


 
(~i→b)∨i: [(O acesso é bloqueado) quando (o funcionário não apresenta identificação)], ou [o funcionário 
apresenta identificação]. 
Ao transformar a condicional (~i→b) em uma disjunção inclusiva utilizando a equivalência p→q ≡ ~p∨q, 
obtemos ~(~i)∨b, ou seja, i∨b. Logo, a proposição original corresponde a: 
(~i→b)∨i ≡ (i∨b)∨i 
Pela propriedade associativa, podemos remover os parênteses da sequência de disjunções: 
(~i→b)∨i ≡ i∨b∨i 
Pela propriedade comutativa, podemos escrever b∨i como i∨b. Ficamos com: 
(~i→b)∨i ≡ i∨i∨b 
Pela propriedade de idempotência da disjunção inclusiva (p∨p ≡ p), a parcela i∨i corresponde a i. Ficamos 
com: 
(~i→b)∨i ≡ i∨b 
Portanto, a alternativa E corresponde a i∨b. 
Por outro lado, note que i∨b também equivale à regra original ~i→b, pois, pela equivalência da 
transformação disjunção inclusiva em condicional, temos p∨q ≡ ~p→q. Logo, a alternativa E é equivalente 
à regra original. 
Gabarito: Letra E. 
(FAUEL/Pref. Cândido Abreu/2024) Assinale a alternativa CORRETA em relação à proposição 
~(p∧q)↔(~p∨~q). 
a) A proposição é uma tautologia. 
b) A proposição é uma contradição. 
c) A proposição é uma contingência. 
d) A proposição é simples. 
Comentários: 
Em uma bicondicional X↔Y, sabemos que, se X e Y forem proposições equivalentes, a bicondicional será 
uma tautologia. 
Note que, por De Morgan, a negação de (p∧q), ou seja, ~(p∧q), é equivalente a (~p∨~q): 
~(p∧q) ≡ (~p∨~q) 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
136
167
==6306a==


 
Como as duas parcelas da bicondicional ~(p∧q)(~p∨~q) são equivalentes, a bicondicional é uma 
tautologia. 
Gabarito: Letra A. 
(FAUEL/Pref. Cândido Abreu/2024) Assinale a alternativa CORRETA em relação à proposição 
(~p∨~q)↔(q∧p). 
a) A proposição é uma tautologia. 
b) A proposição é uma contradição. 
c) A proposição é uma contingência. 
d) A proposição é simples. 
Comentários: 
Em uma bicondicional X↔Y, sabemos que, se X for a negação de Y, a bicondicional será uma contradição. 
Vamos verificar essa relação na bicondicional em questão:  
(~p∨~q) ↔ (q∧p) 
Por De Morgan, sabemos a negação da conjunção, ~(p∧q), corresponde a (~p∨~q). Portanto, podemos 
escrever a primeira parcela da bicondicional como ~(p∧q). Ficamos com: 
~(p∧q) ↔ (q∧p) 
Vamos, agora, verificar a segunda parcela da bicondicional. Aplicando a propriedade comutativa em q∧p, 
obtemos p∧q. Substituindo na bicondicional, temos: 
~(p∧q) ↔ (p∧q) 
Note que a primeira parcela, ~(p∧q), é a negação direta da segunda parcela, (p∧q). Consequentemente, a 
bicondicional é uma contradição. 
Gabarito: Letra B. 
(CPCON UEPB/Pref. Nazarezinho/2025) Analise as seguintes expressões lógicas, referentes às 
proposições compostas R, S, T e U, respectivamente. 
• R(p, q) = ~(p ∧ q) 
• S(p, q) = ~(p ∧ q) ∨ (~p) 
• T(p, q) = (~p ∨ ~q) 
• U(p, q) = (~(p ∧ q) ∨ (~p)) → (~p ∨ ~q) 
Assinale a alternativa CORRETA. 
a) As proposições R(p, q), S(p, q), T(p, q) e U(p, q) são individualmente Contingentes. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
137
167


 
b) As proposições S(p, q) e T(p, q) são equivalentes entre si e a proposição U(p, q) é uma Contradição. 
c) As proposições R(p, q) e U(p, q) são equivalentes entre si. 
d) As proposições R(p, q) e T(p, q) são individualmente Contingentes e a proposição U(p, q) é uma 
Contradição. 
e) As proposições R(p, q), S(p, q) e T(p, q) são equivalentes entre si e individualmente Contingentes. Além 
disso, a proposição U(p, q) é uma Tautologia. 
Comentários: 
Vamos analisar cada uma das proposições compostas usando álgebra de proposições. 
  
•   R(p, q) = ~(p∧q) 
Aplicando De Morgan, para negar a conjunção, negam-se ambas as parcelas e troca-se o “e” pelo “ou”. 
Logo: 
R(p, q) ≡ ~p∨~q 
Note que R(p, q) corresponde exatamente a T(p, q). 
•   S(p, q) = ~(p∧q)∨(~p) 
Aplicando De Morgan no primeiro termo (~(p∧q) ≡ ~p∨~q), temos: 
S(p, q) ≡ (~p∨~q)∨~p 
Pela propriedade associativa, podemos remover os parênteses da sequência de disjunções: 
S(p, q) ≡ ~p∨~q∨~p 
Pela propriedade comutativa, podemos escrever ~q∨~p como ~p∨~q. Ficamos com: 
S(p, q) ≡ ~p∨~p∨~q 
Pela propriedade de idempotência da disjunção inclusiva (p∨p ≡ p), a parcela ~p∨~p corresponde a ~p. 
Ficamos com: 
S(p, q) ≡ ~p∨~q 
Logo, S(p, q) também corresponde a T(p, q). 
Portanto, R, S e T são equivalentes entre si, todas correspondendo a ~p∨~q. Como essa expressão pode 
ser V ou F dependendo dos valores de p e q, trata-se de uma proposição contingente. 
•  U(p, q) = (~(p∧q)∨(~p)) → (~p∨~q) 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
138
167


 
Note que o antecedente da condicional é S(p, q) e o consequente é T(p, q). Como S é equivalente a T, 
podemos reescrever: 
U(p, q) ≡ T → T 
Observe que: 
• Quando a proposição composta T for verdadeira (V), a condicional será da forma V→V, que é 
verdadeira (V). 
• Quando a proposição composta T for falsa (F), a condicional será da forma F→F, que também é 
verdadeira (V). 
Note, portanto, que a condicional U(p, q) ≡ T → T será sempre verdadeira, qualquer que seja o valor lógico 
de T. Portanto, U é uma tautologia. 
Em síntese: 
• R, S e T são equivalentes entre si e individualmente contingentes; 
• U é uma tautologia. 
Gabarito: Letra E. 
(FUNDATEC/Pref. Criciúma/2024) Utilizando a argumentação lógica, uma proposição equivalente à 
afirmativa “o cavalo é forte e veloz” é: 
a) Se o cavalo é veloz, então é forte. 
b) Se o cavalo não é forte, então não é veloz. 
c) O cavalo é forte ou veloz. 
d) O cavalo é veloz e forte. 
e) O cavalo é lento e fraco. 
Comentários: 
Sejam as proposições simples: 
f: "O cavalo é forte." 
v: "O cavalo é veloz." 
Note que a proposição composta apresentada pode ser descrita pela conjunção f∧v: 
f∧v: “[O cavalo é forte] e [(o cavalo é) veloz]” 
Aplicando a propriedade comutativa para a conjunção, podemos trocar as parcelas de posição: 
f∧v ≡ v∧f 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
139
167


 
Logo, a afirmação original é equivalente a: 
v∧f: "[O cavalo é veloz] e [(o cavalo é) forte]." 
Gabarito: Letra D. 
(INSTITUTO MAIS/CM Santo André/2024) Dadas as proposições compostas abaixo, assinale a alternativa 
que representa uma contradição. 
a) (~q → ~p) ∧ (p ∧ ~q) 
b) (~q → ~p) ∧ (p ∨ ~q) 
c) (~q → ~p) ∨ (p ∧ ~q) 
d) (p → q) ∧ (~p ∧ ~q) 
Comentários: 
Estamos à procura de uma contradição. Sabemos que uma contradição clássica é aquela da forma p∧~p. 
Nessa questão, vamos procurar por esse padrão de contradição. 
Primeiramente, note que em diversas alternativas temos  condicional (~q→~p). Essa condicional é a 
equivalência contrapositiva de p→q. Logo, podemos descrever as alternativas da seguinte forma: 
a) (p → q) ∧ (p ∧ ~q) 
b) (p → q) ∧ (p ∨ ~q) 
c) (p → q) ∨ (p ∧ ~q) 
d) (p → q) ∧ (~p ∧ ~q) 
Observe a alternativa A. Note que a segunda parcela, (p ∧ ~q), corresponde à negação da condicional p→q. 
Em outras palavras: ~(p → q) ≡ (p ∧ ~q). Substituindo (p ∧ ~q) por ~(p → q), ficamos com o seguinte: 
(p → q) ∧ ~(p →q) 
Observe, portanto, que a alternativa A apresenta uma contradição da forma p∧~p. Veja que: 
• Se (p → q) for verdadeiro (V), a negação ~(p→q) será falsa (F). Nesse caso, a conjunção será da 
forma V∧F, que é falsa (F). 
• Se (p → q) for falso (F), a negação ~(p→q) será verdadeira (V). Nesse caso, a conjunção será da 
forma F∧V, que também falsa (F). 
Portanto, a conjunção (p → q) ∧ ~(p →q) será sempre falsa, qualquer que seja o valor lógico de (p → q). 
Logo, a alternativa A apresenta a contradição procurada. 
Gabarito: Letra A. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
140
167


 
LISTA DE QUESTÕES - MULTIBANCAS 
Equivalências Lógicas 
 
As questões estão divididas por banca: 
• Outras Bancas 
• FGV 
• CEBRASPE 
• FCC 
• VUNESP 
Dentro de cada banca, caso seja aplicável para ela, podemos ter os seguintes tópicos, 
conforme a teoria da aula: 
• Equivalências fundamentais 
• Negações lógicas 
• Questões com mais de uma equivalência 
• Outras equivalências e negações 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
141
167


 
Outras Bancas 
Outras Bancas - Equivalências Fundamentais 
(QUADRIX/Novacap/2024) As proposições “Se Gabriela cantou, então Jacqueline não cantou” e “Ou 
Gabriela cantou ou Jacqueline cantou” são equivalentes.  
 
(Instituto AOCP/PM PE/2024) Se Carlos mentiu sobre sua aprovação no concurso para a Polícia Militar 
de Pernambuco, então será criticado por sua família nas festas de final de ano. Logo, para a lógica, 
a) Carlos será criticado por sua família nas festas de final de ano. 
b) se Carlos não mentiu sobre sua aprovação no concurso para a Polícia Militar de Pernambuco, então não 
será criticado por sua família nas festas de final de ano. 
c) Carlos mentiu sobre sua aprovação no concurso para a Polícia Militar de Pernambuco. 
d) se Carlos não foi criticado por sua família nas festas de final de ano, então não mentiu sobre sua 
aprovação no concurso para a Polícia Militar de Pernambuco. 
e) se Carlos foi criticado por sua família nas festas de final de ano, então mentiu sobre sua aprovação no 
concurso para a Polícia Militar de Pernambuco. 
 
(Instituto Verbena/IFS/2024) Considere a proposição P referente aos números naturais. 
P: se n2 é par, então n é par. 
Sua contrapositiva é: 
a) se n não é par, então n2 é ímpar. 
b) se n não é par, então n2 é par. 
c) se n é par, então n2 não é ímpar. 
d) se n2 não é par, então n2 é ímpar. 
 
 (IBFC/IBGE/2022) De acordo com a proposição lógica a frase “Se o coordenador realizou a previsão 
orçamentária, então o trabalho foi realizado com sucesso” é equivalente a frase: 
a) Se o coordenador não realizou a previsão orçamentária, então o trabalho não foi realizado com sucesso 
b) O coordenador realizou a previsão orçamentária e o trabalho foi realizado com sucesso 
c) O coordenador realizou a previsão orçamentária ou o trabalho foi realizado com sucesso 
d) Se o trabalho não foi realizado com sucesso, então o coordenador não realizou a previsão orçamentária 
e) Se o trabalho foi realizado com sucesso, então o coordenador realizou a previsão orçamentária 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
142
167


 
(QUADRIX/CRT MG/2022) A proposição “Quem tem boca vai a Roma” é equivalente à proposição “Não 
tem boca ou vai a Roma”. 
 
(Instituto AOCP/PC PA/2021) Considere a seguinte sentença: “O circuito A não possui escala de 
integração SSI ou o circuito B possui escala de integração LSI”. Uma afirmação logicamente equivalente a 
essa sentença dada é: 
a) “Se o circuito A não possui escala de integração SSI, então o circuito B possui escala de integração LSI”. 
b) ”Se o circuito A possui escala de integração SSI, então o circuito B possui escala de integração LSI”. 
c) ”Se o circuito A possui escala de integração SSI, então o circuito B não possui escala de integração LSI”. 
d) ”Se o circuito A não possui escala de integração SSI, então o circuito B não possui escala de integração 
LSI”. 
e) “Se o circuito B possui escala de integração LSI, então o circuito A possui escala de integração SSI”. 
 
Outras Bancas - Negações Lógicas 
(QUADRIX/Novacap/2024) A negação da proposição “Se Carolina dançou, Ana cantou” é “Se Ana não 
cantou, então Carolina não dançou”.  
 
(CONSULPLAM/ISS BH/2024) Uma acareação de um desvio de conduta em uma empresa chegou a um 
suspeito que, em um primeiro momento, deu a seguinte declaração: “O computador estava sem internet 
ou a porta emperrou”. Pela fala, identificou-se que o suspeito estava mentindo. Isto é, 
a) O computador estava sem internet e a porta emperrou. 
b) O computador estava com internet ou a porta não emperrou. 
c) O computador estava com internet e a porta não emperrou. 
d) O computador estava sem internet ou a porta não emperrou. 
e) O computador estava com internet e a porta emperrou. 
 
(CONSULPLAM/ISS BH/2024) Sabe-se que a negação de uma sentença r é denotada por ¬r. Uma 
proposição equivalente a (¬p) ∧ (¬q) é:  
a) ¬p→¬q 
b) pq 
c) q↛p 
d) p∨q 
e) ¬(p∨q) 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
143
167


 
(AOCP/SEAP PR/2024) Considere a proposição P: “Se Marlene é economista, então Marlene avalia 
pesquisas na área econômica do Poder Executivo Estadual”. Se Orlando tem conhecimentos apurados de 
raciocínio lógico e afirma que a proposição P é falsa, então, para Orlando, é correto afirmar que 
a) Marlene não é economista e Marlene não avalia pesquisas na área econômica do Poder Executivo 
Estadual. 
b) se Marlene não avalia pesquisas na área econômica do Poder Executivo Estadual, então Marlene não é 
economista. 
c) Marlene é economista e Marlene não avalia pesquisas na área econômica do Poder Executivo Estadual. 
d) Marlene não é economista ou Marlene avalia pesquisas na área econômica do Poder Executivo Estadual. 
e) Marlene avalia pesquisas na área econômica do Poder Executivo Estadual. 
 
(FUNDATEC/ALE RS/2024) Considere a proposição lógica dada por: 
“Antônio é profissional de Tecnologia da Informação ou de Jornalismo”. 
 A negação desta proposição é: 
a) Antônio não é profissional de Tecnologia da Informação. 
b) Antônio não é profissional de Tecnologia da Informação, mas é de Jornalismo 
c) Antônio é profissional de Tecnologia da Informação, mas não é de Jornalismo. 
d) Antônio não é profissional de Tecnologia da Informação nem de Jornalismo. 
e) Antônio não é profissional de Jornalismo. 
 
 (FUNDATEC/ALE RS/2024) Considere a proposição abaixo. 
“Jairo não é formado em exatas e Marcia é formada em humanas”. 
A negação lógica da proposição acima é dada por: 
a) Jairo é formado em exatas e Márcia também. 
b) Jairo é formado em exatas ou Márcia não é formada em humanas. 
c) Jairo é formado em exatas ou Márcia também. 
d) Jairo não é formado em humanas ou Márcia é. 
e) Jairo é formado em exatas e Márcia não é formada em humanas. 
 
(IBFC/PCP PR/2024) A negação lógica da frase “Hoje é domingo e não trabalharei” é dada por: 
a) hoje é domingo e trabalharei 
b) hoje não é domingo e trabalharei 
c) hoje não é domingo e não trabalharei 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
144
167


 
d) hoje não é domingo ou trabalharei 
e) hoje é domingo ou trabalharei 
 
Outras Bancas - Questões com mais de uma equivalência 
(IBFC/IBGE/2022) De acordo com a proposição lógica a frase “O agente censitário não transcreveu o 
texto em planilha eletrônica ou o trabalho foi realizado com sucesso” é equivalente a frase: 
a) Se o agente censitário não transcreveu o texto em planilha eletrônica, então o trabalho não foi realizado 
com sucesso 
b) O agente censitário transcreveu o texto em planilha eletrônica e o trabalho não foi realizado com 
sucesso 
c) O agente censitário transcreveu o texto em planilha eletrônica ou o trabalho não foi realizado com 
sucesso 
d) Se o trabalho foi realizado com sucesso, então o coordenador não realizou a previsão orçamentária 
e) Se o trabalho não foi realizado com sucesso, então o agente censitário não transcreveu o texto em 
planilha eletrônica 
 
Outras Bancas - Outras equivalências e negações 
(AOCP/DEPEN PR/2024) Em relação à proposição “João nunca foi privado de liberdade, e o relatório 
policial é inconclusivo”, pode-se afirmar que sua negação lógica é corretamente representada em 
a) João sempre foi privado de liberdade, e o relatório policial não é inconclusivo. 
b) João nunca será privado de liberdade, então o relatório policial nunca será inconclusivo. 
c) Se João nunca for privado de liberdade, então o relatório policial nunca é inconclusivo. 
d) Se o relatório policial sempre é inconclusivo, então João sempre é privado de liberdade. 
e) Se o relatório policial é inconclusivo, então ao menos uma vez João foi privado de liberdade. 
 
(IDECAN/Pref SCS/2023)  Uma bicondicional equivale a uma conjunção de duas condicionais. Em 
termos simbólicos, teremos 
a)  pq = (p∨q) e (q∨p) 
b)  pq = (p→q) e (q→p) 
c)  p∨q = (p∨q) e (q→p) 
d)  p←q = (p→~q) e (q→p) 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
145
167


 
(IDECAN/IF PA/2022) Assinale a alternativa que apresenta uma proposição equivalente a “todos os 
empresários conseguirão sucesso no ramo do empreendedorismo se, e somente se, investirem tempo 
com muito estudo e pesquisa". 
a) Se todos os empresários conseguirem sucesso no ramo do empreendedorismo, então investiram tempo 
com muito estudo e pesquisa ou se investiram tempo com muito estudo e pesquisa, então todos os 
empresários conseguirão sucesso no ramo do empreendedorismo. 
b) Se todos os empresários conseguirem sucesso no ramo do empreendedorismo, então investiram tempo 
com muito estudo e pesquisa e investiram tempo com muito estudo e pesquisa se, e somente se, todos os 
empresários conseguirem sucesso no ramo do empreendedorismo. 
c) Se todos os empresários conseguirem sucesso no ramo do empreendedorismo, então investiram tempo 
com muito estudo e pesquisa e se investiram tempo com muito estudo e pesquisa, então todos os 
empresários conseguirão sucesso no ramo do empreendedorismo. 
d) Se não investirem tempo com muito estudo e pesquisa, então nem todos os empresários conseguirão 
sucesso no ramo do empreendedorismo. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
146
167


 
FGV 
FGV - Equivalências Fundamentais 
(FGV/ALESC/2024) Considere a afirmação: 
“Se tenho namorada então não fico sozinho” 
 Uma afirmação logicamente equivalente à afirmação dada é: 
a) Se não fico sozinho então tenho namorada. 
b) Se fico sozinho então não tenho namorada. 
c) Se não tenho namorada então fico sozinho. 
d) Tenho namorada e não fico sozinho. 
e) Tenho namorada ou não fico sozinho. 
 
(FGV/SEFAZ-MG/2023) É dada a afirmativa:  
“Se o cliente pagou então não é devedor.” 
Para cada uma das três afirmativas a seguir, assinale “V” se a afirmativa for logicamente equivalente à 
afirmativa dada e “F” se a afirmativa não for logicamente equivalente à afirmativa dada.  
I. Se o cliente não pagou então é devedor.  
II. Se o cliente não é devedor então pagou.  
III. Se o cliente é devedor então não pagou.  
As afirmativas I, II e III são, respectivamente, 
a) V, V e F.  
b) F, V e F.  
c) F, F e V.  
d) F, V e V.  
e) V, V e V.  
 
 (FGV/AGENERSA/2023) Considere a afirmativa a seguir. 
“Se não durmo, então tenho dor de cabeça.” 
Analise, a seguir, três novas afirmativas: 
I. Se durmo, então não tenho dor de cabeça. 
II. Se tenho dor de cabeça, então não durmo. 
III. Se não tenho dor de cabeça, então durmo. 
Assinale a opção que indica a(s) afirmativa(s) que é(são) equivalente(s) à inicial. 
a) I, apenas. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
147
167


 
b) II, apenas. 
c) III, apenas. 
d) I e II, apenas. 
e) I, II e III. 
 
(FGV/CM Taubaté/2022) Considere a sentença: “Se Antônio é baiano, então Carlos não é 
amapaense”. Uma sentença logicamente equivalente à sentença dada é:  
a) Se Carlos não é amapaense, então Antônio é baiano.  
b) Se Antônio não é baiano, então Carlos é amapaense.  
c) Se Carlos é amapaense, então Antônio é baiano.  
d) Antônio não é baiano ou Carlos não é amapaense.  
e) Antônio é baiano e Carlos é amapaense. 
 
FGV - Negações Lógicas  
(FGV/MPE SP/2023) Considere a proposição: 
“Se estamos em fevereiro, então eu pago o IPVA”. 
Assinale a opção que apresenta uma negação dessa proposição. 
a) Estamos em fevereiro e eu não pago o IPVA. 
b) Não estamos em fevereiro e eu não pago o IPVA. 
c) Se estamos em fevereiro, então eu não pago o IPVA. 
d) Se não estamos em fevereiro, então eu não pago o IPVA. 
e) Se não estamos em fevereiro, então eu pago o IPVA. 
 
 (FGV/PGM Niterói/2023) Considere a sentença: “Se o chapéu é branco, então o sapato é bicolor”. 
A negação lógica da sentença dada é: 
a) se o chapéu é branco, então o sapato não é bicolor; 
b) se o chapéu não é branco, então o sapato é bicolor; 
c) se o sapato não é bicolor, então o chapéu não é branco; 
d) o chapéu não é branco ou o sapato é bicolor; 
e) o chapéu é branco e o sapato não é bicolor. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
148
167


 
(FGV/Pref Niterói/2023) Houve um problema na construção de uma casa e o arquiteto que elaborou o 
projeto disse: 
“O projeto está certo e eu fiscalizei a obra.” 
Considerando que essa frase é falsa, é correto concluir que 
a) “O projeto não está certo e o arquiteto fiscalizou a obra.” 
b) “O projeto está certo e o arquiteto não fiscalizou a obra.” 
c) “O projeto não está certo e o arquiteto não fiscalizou a obra.” 
d) “O projeto está certo ou o arquiteto fiscalizou a obra.” 
e) “O projeto não está certo ou o arquiteto não fiscalizou a obra.” 
 
  (FGV/Câmara dos Deputados/2023) Na canção “Se você jurar”, de Ismael Silva, encontramos a 
afirmação: 
Se você jurar que me tem amor, eu posso me regenerar. 
A negação dessa proposição é 
a) você jura que me tem amor e eu não me regenero. 
b) você não jura que me tem amor e eu não me regenero. 
c) você não jura que me tem amor e eu me regenero. 
d) você jura que me tem amor e eu posso me regenerar. 
e) você não jura que me tem amor e eu não posso me regenerar. 
 
FGV - Questões com mais de uma equivalência 
(FGV/ALESC/2024) Considere a sentença: 
“Se x ≤ 6 e x > 4, então −x ≤ 2”. Uma sentença logicamente equivalente à sentença dada é 
a) Se x > 6 e x ≤ 4, então  −x > 2. 
b) Se  −x ≤ 2, então x ≤ 6 e x > 4. 
c) Se x > 6 ou x ≤ 4, então  − x > 2. 
d) x > 6 ou x ≤ 4 ou  −x ≤ 2. 
e) x > 6 e x ≤ 4 ou  −x ≤ 2. 
 
(FGV/ALE TO/2024) A negação da proposição: 
Se 𝑦 ≠ 0, então 𝑥 > 2 e 𝑥 ≤ 5 
é dada por 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
149
167


 
a) Se 𝑦 = 0, então 𝑥 > 2 e 𝑥 ≤ 5 
b) Se 𝑦 = 0, então 𝑥 < 2 ou 𝑥 ≥ 5 
c) 𝑦 = 0 e 𝑥 ≤ 2 ou 𝑥 > 5 
d) 𝑦 ≠ 0 e 𝑥 ≤ 2 ou 𝑥 > 5 
e) 𝑦 ≠ 0 e 𝑥 ≤ 2 e 𝑥 > 5 
 
(FGV/MPE SP/2023) “Se a TV não está ligada, então eu estou dormindo ou estou lendo”. 
Assinale a opção que descreve uma sentença logicamente equivalente à afirmação acima. 
a) A TV não está ligada e eu estou acordado e não estou lendo. 
b) Se eu não estou dormindo e não estou lendo, então a TV está ligada. 
c) Se eu estou acordado ou não estou lendo, então a TV está ligada. 
d) Eu estou acordado e lendo se, e somente se, a TV está desligada. 
e) A TV está ligada e eu estou acordado ou não estou lendo. 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
150
167


 
CEBRASPE 
CEBRASPE - Equivalências Fundamentais 
(CEBRASPE/SEFAZ AC/2024) Assinale a opção em que é corretamente apresentada uma proposição 
que é logicamente equivalente à proposição “Se não há débito fiscal, então não há cobrança”.  
a) Há débito fiscal e há cobrança.  
b) Não há débito fiscal ou não há cobrança.  
c) Há débito fiscal ou não há cobrança.  
d) Não há débito fiscal ou há cobrança.  
e) Não há débito fiscal e não há cobrança.  
 
(CEBRASPE/SEFAZ AC/2024) Uma criança deseja ficar brincando no parquinho. A mãe diz ao filho: 
 — “Filho, não quero que se molhe. Quando começar a chover ou chegar uma criança grande, vamos 
embora. Não pise na água ou vamos embora.” 
Após alguns minutos, a mãe tomou a criança pela mão e eles foram embora. 
Ainda considerando o texto, assinale a opção em que está apresentada uma exortação que, sob o ponto 
de vista lógico, tenha o mesmo significado daquela feita pela mãe em “Não pise na água ou vamos 
embora”. 
a) Se não pisar na água, não vamos embora. 
b) Não pise na água e não vamos embora. 
c) Pise na água e vamos embora. 
d) Não pise na água e vamos embora. 
e) Se pisar na água, vamos embora.    
 
(CESPE/ANA/2024) P5: Se o habitador artificial se romper antes de chegar o socorro, eu implodo. 
P5 é equivalente a “Se eu não implodi, o habitador artificial não se rompeu antes de chegar o socorro”. 
 
(CESPE/PC PE/2024) P: “Se não preciso tentar roubá-lo, não cometi esse crime.” 
Assinale a opção em que está apresentada uma proposição equivalente a P. 
a) “Preciso tentar roubá-lo, mas não cometi esse crime.” 
b) “Precisava tentar roubá-lo e cometi esse crime.” 
c) “Se não cometi esse crime, não preciso tentar roubá-lo.” 
d) “Preciso tentar roubá-lo ou não cometi esse crime.” 
e) “Se preciso tentar roubá-lo, cometi esse crime.” 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
151
167
==6306a==


 
(CESPE/SERPRO/2023) P4: Se não há prova sem nome nos arquivos do professor, então o aluno não 
se esqueceu de colocar seu nome na prova. 
A proposição P4 é equivalente a “Se o aluno não se esqueceu de colocar seu nome na prova, então não 
há prova sem nome nos arquivos do professor”. 
 
CEBRASPE - Negações Lógicas  
(CESPE/ANA/2024) P4: Se o reciclador de água estragar antes de chegar o socorro, eu morro de sede. 
A negação de P4 pode ser corretamente expressa por “O reciclador de água estragou antes de chegar o 
socorro, mas eu não morri de sede”. 
 
(CESPE/FINEP/2024) Assinale a opção que apresenta a negação da proposição: Paguei o café da 
manhã com o cartão de débito e o almoço com o cartão de crédito. 
a) Paguei o café da manhã com o cartão de crédito e não paguei o almoço com o cartão de débito. 
b) Paguei o almoço com o cartão de débito e o café da manhã com o cartão de crédito. 
c) Não paguei o café da manhã com o cartão de débito nem o almoço com o cartão de crédito. 
d) Não paguei o café da manhã com o cartão de débito e o almoço com o cartão de crédito. 
e) Não paguei o café da manhã com o cartão de débito ou o almoço com o cartão de crédito. 
 
 (CESPE/POLC AL/2023) Considerando os conectivos lógicos usuais e assumindo que as letras 
maiúsculas representam proposições lógicas, julgue o item seguinte, relativo à lógica proposicional. 
A negação da sentença "Se eu me alimento de forma saudável, então terei uma boa qualidade de vida no 
período da terceira idade" corresponde à sentença "Se eu não me alimento de forma saudável, então 
não terei uma boa qualidade de vida no período da terceira idade". 
 
(CESPE/SERPRO/2023) P6: Se a assinatura do aluno não consta da lista de presença do dia da prova, 
então o aluno não fez a prova. 
A negação da proposição P6 pode ser corretamente expressa por “a assinatura do aluno não consta da 
lista de presença do dia da prova, mas o aluno não deixou de fazer a prova”. 
 
CEBRASPE - Questões com mais de uma equivalência 
(CEBRASPE/SEFAZ AC/2024) P6: “Se houver incerteza sobre os impactos nos planos de longo prazo da 
empresa, o investidor ficará receoso e a ação da empresa ficará volátil.” 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
152
167


 
Assinale a opção que corresponde a uma proposição equivalente, sob o ponto de vista lógico, à 
proposição P6. 
a) Se o investidor ficou receoso e a ação da empresa ficou volátil, houve incerteza sobre os impactos nos 
planos de longo prazo da empresa. 
b) Se o investidor não ficou receoso ou a ação da empresa não ficou volátil, não houve incerteza sobre os 
impactos nos planos de longo prazo. 
c) Se o investidor ficou receoso ou a ação da empresa ficou volátil, houve incerteza sobre os impactos nos 
planos de longo prazo da empresa. 
d) Se não houver incerteza sobre os impactos nos planos de longo prazo da empresa, o investidor não 
ficará receoso e a ação da empresa não ficará volátil. 
e) Houve incerteza sobre os impactos nos planos de longo prazo da empresa, o investidor ficou receoso e a 
ação da empresa ficou volátil. 
 
(CEBRASPE/SEFAZ AC/2024) P2: “Se a demanda pelo produto vendido pela companhia sofre retração, 
no novo equilíbrio de mercado, diminuem seu preço e sua quantidade demandada.” 
Assinale a opção em que é apresentada uma proposição que, sob o ponto de vista lógico, expressa o 
exato significado da proposição P2. 
a) “Se, no novo equilíbrio de mercado, diminuem o preço e a quantidade demandada do produto vendido 
pela companhia, sua demanda sofre retração.” 
b) “Se, no novo equilíbrio de mercado, diminui o preço ou a quantidade demandada do produto vendido 
pela companhia, sua demanda sofre retração.” 
c) “Se a demanda pelo produto vendido pela companhia não sofre retração, no novo equilíbrio de 
mercado, não diminuem seu preço nem sua quantidade demandada.” 
d) “A demanda pelo produto vendido pela companhia sofre retração e, no novo equilíbrio de mercado, 
diminuem seu preço e sua quantidade demandada.” 
e) “A demanda pelo produto vendido pela companhia não sofre retração ou, no novo equilíbrio de 
mercado, diminuem seu preço e sua quantidade demandada.” 
 
(CESPE/FINEP/2024) Assinale a opção que é equivalente a "Se a inflação não reflete o aumento do 
custo de vida do cidadão e os juros básicos da economia caem, a rentabilidade da renda fixa fica 
prejudicada." 
a) Se a rentabilidade da renda fixa fica prejudicada, a inflação não reflete o aumento do custo de vida do 
cidadão e os juros básicos da economia caem. 
b) Quando a rentabilidade da renda fixa fica prejudicada, a inflação não reflete o aumento do custo de vida 
do cidadão e os juros básicos da economia caem. 
c) Se a inflação reflete o aumento do custo de vida do cidadão ou os juros básicos da economia não caem, a 
rentabilidade da renda fixa não fica prejudicada. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
153
167


 
d) A inflação reflete o aumento do custo de vida do cidadão, os juros básicos da economia não caem ou a 
rentabilidade da renda fixa fica prejudicada. 
e) A inflação não reflete o aumento do custo de vida do cidadão e os juros básicos da economia caem, mas 
a rentabilidade da renda fixa não fica prejudicada. 
 
(CESPE/Itaipu Binacional/2024) “O chefe não me falou sobre isso, mas, se eu for convidado, aceitarei 
a tarefa.” 
Assinale a opção que apresenta uma negação da proposição anterior. 
a) O chefe me falou sobre isso, ou serei convidado, mas não aceitarei a tarefa. 
b) O chefe me falou sobre isso, mas, se eu não for convidado, não aceitarei a tarefa. 
c) O chefe me falou sobre isso, mas não fui convidado ou não aceitei a tarefa. 
d) O chefe me falou sobre isso, serei convidado, mas não aceitarei a tarefa. 
e) O chefe me falou sobre isso ou eu não serei convidado ou não aceitarei a tarefa. 
 
(CESPE/CGE RJ/2024) A negação do trecho ‘se você acredita, não precisa de explicação; se você não 
acredita, não adianta explicação’ pode ser expressa corretamente por ‘você acredita, mas precisa de 
explicação, ou você não acredita, mas adianta explicação’. 
 
(CESPE/TCDF/2023) São logicamente equivalentes as sentenças I e II, a seguir. 
I. “Se o governador do DF indicou o presidente do TCDF e a Câmara Legislativa indicou o corregedor, 
então o ouvidor é apreciador de música clássica.” 
II. “Ou o presidente do TCDF não foi indicado pelo governador ou o corregedor não foi indicado pela 
Câmara Legislativa ou o ouvidor é apreciador de música clássica.” 
 
CEBRASPE - Outras equivalências e negações  
(CESPE/PETROBRAS/2022) Acerca de lógica matemática, julgue o item a seguir. 
Dadas três proposições p, q e r, tem-se que p∨q→r é equivalente a (p→r)∨(q→r). 
 
 (CESPE/TCE-RS/2013) Com base na proposição P: “Quando o cliente vai ao banco solicitar um 
empréstimo, ou ele aceita as regras ditadas pelo banco, ou ele não obtém o dinheiro”, julgue o item que 
se segue. 
A negação da proposição “Ou o cliente aceita as regras ditadas pelo banco, ou o cliente não obtém o 
dinheiro” é logicamente equivalente a “O cliente aceita as regras ditadas pelo banco se, e somente se, o 
cliente não obtém o dinheiro” 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
154
167


 
FCC 
FCC - Equivalências Fundamentais 
(FCC/SEFAZ BA/2019) Em seu discurso de posse, determinado prefeito afirmou: “Se há incentivos 
fiscais, então as empresas não deixam essa cidade”. Considerando a afirmação do prefeito como 
verdadeira, então também é verdadeiro afirmar: 
a) Se não há incentivos fiscais, então as empresas deixam essa cidade. 
b) Se as empresas não deixam essa cidade, então há incentivos fiscais. 
c) Se as empresas deixam essa cidade, então não há incentivos fiscais. 
d) As empresas deixam essa cidade se há incentivos fiscais. 
e) As empresas não deixam essa cidade se não há incentivos fiscais. 
 
(FCC/SEFAZ BA/2019) Suponha que a negação da proposição “Você é a favor da ideologia X” seja 
“Você é contra a ideologia X”. A proposição condicional “Se você é contra a ideologia A, então você é a 
favor da ideologia C” é equivalente a 
a) Você é a favor da ideologia A e você é a favor da ideologia C. 
b) Ou você é a favor da ideologia A ou você é a favor da ideologia C, mas não de ambas. 
c) Você é a favor da ideologia A ou você é contra a ideologia C. 
d) Você é a favor da ideologia A ou você é a favor da ideologia C. 
e) Você é contra a ideologia A e você é contra a ideologia C. 
 
FCC - Negações Lógicas  
(FCC/TRT 9/2022) A negação da afirmação: “não ficou doente e vai ficar em casa” é: 
a) Ficou doente e não vai ficar em casa. 
b) Não ficou doente ou vai ficar em casa. 
c) Ficou doente ou não vai ficar em casa. 
d) Ficou doente ou vai ficar em casa. 
e) Não ficou doente ou não vai ficar em casa. 
 
(FCC/IBMEC/2019) Dadas duas proposições lógicas P e Q, então a negação da sentença P ∧ Q é 
equivalente a 
a) (- P) ∨ (- Q) 
b) (- P) ∧ (- Q) 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
155
167


 
c) - (P ∨ Q) 
d) (- P) ∧ Q 
e) P ∧ (- Q) 
 
(FCC/AFAP/2019) A negação da afirmação condicional “Se Carlos não foi bem no exame, vai ficar em 
casa” é: 
a) Se Carlos for bem no exame, vai ficar em casa. 
b) Carlos foi bem no exame e não vai ficar em casa. 
c) Carlos não foi bem no exame e vai ficar em casa. 
d) Carlos não foi bem no exame e não vai ficar em casa. 
e) Se Carlos não foi bem no exame então não vai ficar em casa. 
 
 (FCC/SEFAZ-SC/2018) A negação da proposição “se eu estudo, eu cresço” pode ser escrita como: 
a) “se eu não estudo, eu não cresço”.  
b) “se eu não cresço, eu não estudo”.  
c) “cresço e não estudo”.  
d) “estudo e não cresço”.  
e) “se eu cresço, eu não estudo”. 
 
FCC - Questões com mais de uma equivalência 
(FCC/Pref. SJRP/2019) Considere a proposição: “Se Alberto está estudando, então é véspera de prova 
ou é dia 29 de fevereiro”. Uma proposição equivalente a essa é 
a) Se Alberto não está estudando, então não é véspera de prova ou não é dia 29 de fevereiro. 
b) Se Alberto não está estudando, então não é véspera de prova e não é dia 29 de fevereiro. 
c) Se é véspera de prova ou é dia 29 de fevereiro, então Alberto está estudando. 
d) Se Alberto está estudando, então é véspera de prova e é dia 29 de fevereiro. 
e) Se não é véspera de prova e não é dia 29 de fevereiro, então Alberto não está estudando. 
 
(FCC/COPERGÁS/2016) Considere a afirmação a seguir: 
Se eu paguei o aluguel ou comprei comida, então o meu salário entrou na conta. 
Uma afirmação equivalente a afirmação anterior é 
a) Se o meu salário não entrou na conta, então eu não paguei o aluguel e não comprei comida. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
156
167


 
b) Se eu paguei o aluguel e comprei comida, então o meu salário entrou na conta. 
c) O meu salário entrou na conta e eu comprei comida e paguei o aluguel. 
d) Se o meu salário não entrou na conta, então eu não paguei o aluguel ou não comprei comida. 
e) Se eu não paguei o aluguel e não comprei comida, então o meu salário não entrou na conta. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
157
167


 
VUNESP 
VUNESP - Equivalências Fundamentais 
(VUNESP/Pref Marília/2023) Uma afirmação logicamente equivalente à afirmação: ‘Se você começa, 
então a repetição faz você continuar’, está contida na afirmação 
a) Se você não começa, então a repetição não faz você continuar. 
b) Se a repetição não faz você continuar, então você não começa. 
c) Você começa e a repetição faz você continuar. 
d) Ou você começa ou a repetição faz você continuar. 
e) Se a repetição faz você continuar, então você começa. 
 
(VUNESP/TCM SP/2023) Considere a seguinte afirmação: Hélio é casado ou Luana é solteira. 
Uma equivalência lógica para a proposição apresentada está contida na alternativa: 
a) Se Hélio não é casado, então Luana é solteira. 
b) Hélio e Luana são solteiros. 
c) Se Hélio é solteiro, então Luana é casada. 
d) Hélio e Luana são casados. 
e) Se Hélio é casado, então Luana não é solteira. 
 
(VUNESP/TJ SP/2022) Uma equivalente lógica para a proposição “Se eu me cuido, então sou 
saudável” está contida na alternativa: 
a) Eu não me cuido e não sou saudável. 
b) Se sou saudável, então eu me cuido. 
c) Eu não me cuido ou sou saudável. 
d) Sou saudável e eu não me cuido. 
e) Eu me cuido e sou saudável. 
 
VUNESP - Negações Lógicas  
(VUNESP/TCM SP/2023) Considere a seguinte afirmação: Se Júnior é auxiliar técnico de controle 
externo, então ele prestou um concurso. 
Assinale a alternativa que contém uma correta negação lógica para a afirmação apresentada. 
a) Júnior é auxiliar técnico de controle externo e ele não prestou um concurso. 
b) Se Júnior não é auxiliar técnico de controle externo, então ele não prestou um concurso. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
158
167


 
c) Júnior não é auxiliar técnico de controle externo, mas ele prestou um concurso. 
d) Se Júnior não prestou um concurso, então ele não é auxiliar técnico de controle externo. 
e) Júnior não é auxiliar técnico de controle externo e não prestou um concurso. 
 
(VUNESP/PC SP/2022) Considere a afirmação: 
‘As camisas estão passadas e os sapatos não estão engraxados’. 
Uma afirmação que corresponde à negação lógica desta, é: 
a) As camisas estão passadas ou os sapatos estão engraxados. 
b) Ou as camisas estão passadas ou os sapatos não estão engraxados. 
c) As camisas não estão passadas e os sapatos estão engraxados. 
d) As camisas não estão passadas e os sapatos não estão engraxados. 
e) As camisas não estão passadas ou os sapatos estão engraxados. 
 
(VUNESP/PC SP/2022) Em certo dia, Estela afirmou para sua mãe, Marília: 
– Eu não estou doente ou eu fiz a lição de casa. 
Marília sabe que essa afirmação é falsa, logo conclui-se que Estela 
a) está doente se e somente se fez a lição de casa. 
b) se não está doente, então fez a lição de casa. 
c) está doente ou não fez a lição de casa. 
d) está doente e não fez a lição de casa. 
e) está doente se e somente se não fez a lição de casa. 
 
VUNESP - Questões com mais de uma equivalência 
(VUNESP/TCM SP/2023) Considere a seguinte afirmação: Se Carlos é médico, então Selma é auditora 
de controle externo e André é auxiliar técnico de controle externo. 
Assinale a alternativa que contém uma equivalência lógica para a afirmação apresentada. 
a) Se Selma não é auditora de controle externo e André não é auxiliar técnico de controle externo, então 
Carlos não é médico. 
b) Se André não é auxiliar técnico de controle externo ou Selma não é auditora de controle externo, então 
Carlos não é médico. 
c) Carlos é médico e Selma é auditora de controle externo, e André é auxiliar técnico de controle externo. 
d) Carlos é médico, mas André não é auxiliar técnico de controle externo ou Selma não é auditora de 
controle externo. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
159
167


 
e) Carlos é médico, mas Selma não é auditora de controle externo e André não é auxiliar técnico de 
controle externo. 
 
(VUNESP/ALESP/2022) Uma afirmação que corresponde à negação lógica da afirmação: “Troveja e 
chove muito, ou o dia está lindo”, é: 
a) Não troveja e não chove muito, ou o dia não está lindo. 
b) Não troveja ou chove muito, ou o dia está lindo. 
c) Não troveja ou não chove muito, e o dia não está lindo. 
d) Troveja ou chove muito, e o dia não está lindo. 
e) Troveja ou não chove muito, e o dia está lindo. 
 
(VUNESP/PC SP/2022) Assinale a alternativa que apresenta uma afirmação logicamente equivalente à 
seguinte afirmação: 
‘Se os catadores coletaram todas as latinhas, então a sacola arrebenta ou fica pesada’ 
a) Os catadores coletaram todas as latinhas e a sacola arrebenta e fica pesada. 
b) A sacola arrebenta ou fica pesada e os catadores coletaram todas as latinhas. 
c) Se a sacola não arrebenta e fica pesada, então os catadores não coletaram todas as latinhas. 
d) Se a sacola arrebenta e não fica pesada, então os catadores coletaram todas as latinhas. 
e) Se a sacola não arrebenta e não fica pesada, então os catadores não coletaram todas as latinhas. 
 
VUNESP - Outras equivalências e negações  
(VUNESP/TCM SP/2023) Uma negação lógica para a afirmação “Sou feliz se, e somente se, você é 
feliz” está contida na alternativa: 
a) Não sou feliz se, e somente se, você não é feliz. 
b) Se eu não sou feliz, então você não é feliz. 
c) Se você não é feliz, então eu não sou feliz. 
d) Sou feliz e você não é feliz. 
e) Ou eu sou feliz, ou você é feliz. 
 
(VUNESP/CMSJC/2022) Considere a afirmação: "Ou arranjo emprego ou não me caso". A negação 
dessa afirmação é: 
a) Se eu arranjo emprego, então eu me caso. 
b) Se eu não arranjo emprego, então eu me caso. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
160
167


 
c) Ou não arranjo emprego ou me caso. 
d) Ou não arranjo emprego ou não me caso. 
e) Arranjo emprego e não me caso. 
 
(VUNESP/ISS Mogi das Cruzes/2021) Sabe-se que não é verdade que, ou José é rico ou Paula é pobre. 
Sendo assim, é correto afirmar que 
a) José é rico se, e somente se, Paula é pobre. 
b) Se José é rico, então Paula é pobre. 
c) Se Paula é pobre, então José é rico. 
d) José e Paula são ricos. 
e) Paula e José são pobres. 
 
(VUNESP/TJ SP/2021) Uma afirmação equivalente à afirmação “Se Alice estuda, então ela faz uma boa 
prova, e se Alice estuda, então ela não fica triste” é 
a) Se Alice estuda, então ela não faz uma boa prova ou ela fica triste. 
b) Se Alice fica triste e não faz uma boa prova, então ela não estuda. 
c) Se Alice estuda, então ela faz uma boa prova e ela não fica triste. 
d) Alice estuda e ela faz uma boa prova e não fica triste. 
e) Alice não estuda, e ela faz uma boa prova ou não fica triste. 
 
 (VUNESP/EBSERH/2020) Uma correta negação lógica para a afirmação “Rosana é vulnerável ou 
necessitada, mas não ambos” está contida na alternativa: 
a) Rosana é vulnerável se, e somente se, ela é necessitada. 
b) Rosana não é vulnerável se, e somente se, ela é necessitada. 
c) Rosana é vulnerável e necessitada. 
d) Rosana não é vulnerável e, tampouco, necessitada. 
e) Se Rosana não é necessitada, então ela não é vulnerável. 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
161
167


 
GABARITO - MULTIBANCAS 
Equivalências Lógicas 
 ERRADO 
 LETRA D 
 LETRA A 
 LETRA D 
 CERTO 
 LETRA B 
 ERRADO 
 LETRA C 
 LETRA E 
 LETRA C 
 LETRA D 
 LETRA B 
 LETRA D 
 LETRA E 
 LETRA E 
 LETRA B 
 LETRA C 
 LETRA B 
 LETRA C 
 LETRA C 
 LETRA D 
 LETRA A 
 LETRA E 
 LETRA E 
 LETRA A 
 LETRA D 
 LETRA D 
 LETRA B 
 LETRA C 
 LETRA E 
 CERTO 
 LETRA D 
 ERRADO 
 CERTO 
 LETRA E 
 ERRADO 
 CERTO 
 LETRA B 
 LETRA E 
 LETRA D 
 LETRA A 
 CERTO 
 CERTO 
 ERRADO 
 CERTO 
 LETRA C 
 LETRA D 
 LETRA C 
 LETRA A 
 LETRA D 
 LETRA D 
 LETRA E 
 LETRA A 
 LETRA B 
 LETRA A 
 LETRA C 
 LETRA A 
 LETRA E 
 LETRA D 
 LETRA B 
 LETRA C 
 LETRA E 
 LETRA E 
 LETRA D 
 LETRA A 
 LETRA C 
 LETRA A 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
162
167


 
LISTA DE QUESTÕES - MULTIBANCAS 
Álgebra de proposições 
(FUNATEC/Pref. V do Mearim/2026) Assinale corretamente a negação da seguinte proposição lógica. 
“João é bom em matemática se, e somente se, Maria é boa em português.” 
a) João é bom em matemática e Maria não é boa em português ou João não é bom em matemática e Maria 
é boa em português. 
b) João é bom em matemática e Maria é boa em português ou João não é bom em matemática e Maria é 
boa em português. 
c) João não é bom em matemática e Maria não é boa em português ou João é bom em matemática e Maria 
não é boa em português. 
d) João não é bom em matemática se, e somente se, Maria não é boa em português. 
 
(COPS UEL/CM Londrina/2026) Considere as proposições simples e a proposição composta a seguir. 
• p: O computador foi atualizado. 
• q: A impressora imprimiu corretamente. 
• Proposição composta: ~p→(p∨q) 
Sobre essas condições, assinale a alternativa que apresenta, corretamente, uma proposição logicamente 
equivalente a essa, em língua portuguesa. 
a) O computador não foi atualizado ou a impressora imprimiu corretamente. 
b) O computador não foi atualizado e a impressora imprimiu corretamente. 
c) O computador não foi atualizado e a impressora não imprimiu corretamente. 
d) O computador foi atualizado ou a impressora imprimiu corretamente. 
e) O computador foi atualizado e a impressora não imprimiu corretamente. 
 
(FEPESE/Pref. Campos Novos/2026) Em um sistema de controle de acesso, utiliza-se a seguinte regra: 
“Se o funcionário não apresentou identificação, então o acesso é bloqueado.” 
O gestor deseja substituir essa frase por outra logicamente equivalente, mantendo exatamente o mesmo 
sentido lógico, mas escrita de forma direta e sem a estrutura de “se… então”. 
Qual das alternativas abaixo expressa uma frase logicamente equivalente à regra original? 
a) O acesso é bloqueado somente quando o funcionário apresenta identificação. 
b) O acesso nunca é bloqueado quando o funcionário não apresenta identificação. 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
163
167


 
c) O acesso é sempre bloqueado, independentemente da apresentação de identificação. 
d) Somente funcionários com identificação têm acesso bloqueado. 
e) O acesso é bloqueado quando o funcionário não apresenta identificação, ou o funcionário apresenta 
identificação. 
 
(FAUEL/Pref. Cândido Abreu/2024) Assinale a alternativa CORRETA em relação à proposição 
~(p∧q)↔(~p∨~q). 
a) A proposição é uma tautologia. 
b) A proposição é uma contradição. 
c) A proposição é uma contingência. 
d) A proposição é simples. 
 
(FAUEL/Pref. Cândido Abreu/2024) Assinale a alternativa CORRETA em relação à proposição 
(~p∨~q)↔(q∧p). 
a) A proposição é uma tautologia. 
b) A proposição é uma contradição. 
c) A proposição é uma contingência. 
d) A proposição é simples. 
 
(CPCON UEPB/Pref. Nazarezinho/2025) Analise as seguintes expressões lógicas, referentes às 
proposições compostas R, S, T e U, respectivamente. 
• R(p, q) = ~(p ∧ q) 
• S(p, q) = ~(p ∧ q) ∨ (~p) 
• T(p, q) = (~p ∨ ~q) 
• U(p, q) = (~(p ∧ q) ∨ (~p)) → (~p ∨ ~q) 
Assinale a alternativa CORRETA. 
a) As proposições R(p, q), S(p, q), T(p, q) e U(p, q) são individualmente Contingentes. 
b) As proposições S(p, q) e T(p, q) são equivalentes entre si e a proposição U(p, q) é uma Contradição. 
c) As proposições R(p, q) e U(p, q) são equivalentes entre si. 
d) As proposições R(p, q) e T(p, q) são individualmente Contingentes e a proposição U(p, q) é uma 
Contradição. 
e) As proposições R(p, q), S(p, q) e T(p, q) são equivalentes entre si e individualmente Contingentes. Além 
disso, a proposição U(p, q) é uma Tautologia. 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
164
167
==6306a==


 
(FUNDATEC/Pref. Criciúma/2024) Utilizando a argumentação lógica, uma proposição equivalente à 
afirmativa “o cavalo é forte e veloz” é: 
a) Se o cavalo é veloz, então é forte. 
b) Se o cavalo não é forte, então não é veloz. 
c) O cavalo é forte ou veloz. 
d) O cavalo é veloz e forte. 
e) O cavalo é lento e fraco. 
 
(INSTITUTO MAIS/CM Santo André/2024) Dadas as proposições compostas abaixo, assinale a alternativa 
que representa uma contradição. 
a) (~q → ~p) ∧ (p ∧ ~q) 
b) (~q → ~p) ∧ (p ∨ ~q) 
c) (~q → ~p) ∨ (p ∧ ~q) 
d) (p → q) ∧ (~p ∧ ~q) 
 
 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
165
167


 
 GABARITO - MULTIBANCAS 
Álgebra de proposições 
 LETRA A 
 LETRA D 
 LETRA E 
 LETRA A 
 LETRA B 
 LETRA E 
 LETRA D 
 LETRA A 
 
Equipe Exatas Estratégia Concursos
Aula 01
TJs - Curso Regular - Matemática e Raciocínio Lógico 
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
166
167


