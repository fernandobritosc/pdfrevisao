Proibida a reprodução e comercialização sem autorização
Usuário: FERNANDO PINHEIRO DE BRITO, fernandobritosc@gmail.com, CPF: 02049894180
Conceitos, Modelos, Tipos e Topologias de Redes
Hoje em dia, é difícil encontrar um computador que não esteja conectado a alguma rede, principalmente, se for um
conjunto de computadores.
 
Imagine uma empresa, por exemplo, que tenha um computador para controlar as vendas e outra para controlar o
estoque. Se estes computadores funcionarem de forma isolada, em algum momento será preciso coletar os dados
registrados no dois computadores e correlacionar essas informações. Obtendo, assim, informações de todo o
processo da empresa.
 
Entretanto, é bem mais prático colocar os dois computadores interligados e trocando informações. Dessa forma, ao
realizar uma venda o estoque é atualizado na mesma hora e o vendedor não corre o risco de vender um produto que
não esteja mais no estoque.
 
Outra situação comum em uma empresa é o uso da impressora. Vários funcionários podem utilizar a mesma
impressora desde que esteja conectada à rede. Se isso não fosse possível, seria necessário comprar uma impressora
para cada funcionário que precisasse utilizá-la. Além disso, é mais fácil dar manutenção em uma impressora do que
em várias.
 
O exemplo da impressora nos faz concluir que o termo "redes" não se limita apenas ao uso de computadores. Outro
exemplo de equipamento que pode ser interligado a uma rede é o celular quando acessamos à Internet.
 
Por essa razão, iremos utilizar a definição de rede do autor Behrouz A. Forouzan em seu livro "Comunicação de Dados
e Redes de Computadores" - quarta edição:
 
"Rede é um conjunto de dispositivos conectados por links de comunicação."
 
Isso significa que dispositivos (que podem ser computadores, impressoras, etc) interligados por algum meio de
transmissão (um cabo, por exemplo) formam uma rede.
 
Inicialmente, as primeiras redes de computadores foram construídas para que vários computadores pudessem
acessar um periférico compartilhado (por exemplo, uma impressora). Ou seja, o dispositivo era conectado à rede, e
não a um único computador. Assim, era possível acessar o periférico de qualquer computador conectado à rede.
 
Depois de algum tempo, os computadores começaram a ser conectados em grande escala. Mas devido a uma outra
motivação: compartilhar poder computacional. Isso aconteceu porque os primeiros computadores eram bastante
caros (principalmente os de alta potência) e, em razão disso, não era viável que, por exemplo, uma universidade
tivesse vários computadores de alto desempenho. Diante dessa situação, surgiu a ideia de colocar um computador
de alta potência interconectado a uma rede de dados e desenvolver softwares que permitissem outros
computadores executar determinada tarefa no computador principal.
 
É importante lembrar que quando dois ou mais dispositivos estão envolvidos em uma comunicação, estes devem
utilizar um conjunto de regras para trocar mensagens. Esse acordo é conhecido como protocolo de rede.
 
O protocolo permite que dispositivos diferentes possam conversar e se entender. Por isso, o protocolo precisa definir
o que vai ser comunicado, como será comunicado e em qual momento deve ser comunicado.
 
Dessa forma, podemos identificar cinco componentes em uma comunicação de dados: o emissor (envia a
mensagem); receptor (recebe a mensagem); protocolo (conjunto de regras); a mensagem (dados a serem
transmitidos); e o meio de transmissão (que pode ser por meio de cabos ou ondas de rádio).
 
O fluxo de uma comunicação pode ser do tipo simplex, half-duplex ou full-duplex.
 
No fluxo de dados conhecido como simplex, a comunicação é unidirecional, ou seja, apenas um dispositivo pode
enviar dados e o outro dispositivo só pode receber.
 
 
O half-duplex permite a comunicação ocorre nos dois sentidos, entretanto não ocorre ao mesmo tempo. Dessa
forma, quando um dispositivo está enviando dados, o outro só pode receber.
 
 
O modo full-duplex permite a transmissão e recepção dos dados ao mesmo tempo.
 
 
Classificação de Redes
 
As redes pode ser classificados quanto a sua dimensão ou quanto a sua forma (topologia).
 
Quanto a sua dimensão, uma rede pode ser do tipo:
 
PAN (Personal Area Network ou rede de área pessoal) - rede de tamanho reduzido que geralmente se refere a
uma pequena rede doméstica. Os dispositivos podem ser interligados por pequenos cabos de redes ou
comunicação sem fio (rádio frequência). A tecnologia bluetooth é a mais conhecida e utilizada nesse tipo de
rede.
LAN (Local Area Network ou rede de área local) - rede que abrange uma área geográfica pequena (limitada a 10
km no máximo). O principal padrão utilizado nesse tipo de rede é o Ethernet que possui entre outras
características baixo custo, estabilidade e baixas taxas de erro. 
MAN (Metropolitan Area Network ou rede de área metropolitana) - rede projetada para cobrir uma cidade que
interliga vários LAN geograficamente próximos.
WAN (Wide Area Network ou rede de longo alcance) - rede que abrange uma grande área geográfica. A Internet
é a maior WAN que existe, interligando várias redes (LAN e MAN) por meio de fibras ópticas ou satélites, por
exemplo. O custo de comunicação nesse tipo de rede é mais elevado.
 
Já a topologia de uma rede pode ser basicamente do tipo estrela, anel e barramento.
 
Na topologia estrela, todos os computadores de uma rede se conectam a um ponto central que, geralmente, é um
equipamento de rede (hub ou switch, por exemplo). Na prática, dificilmente, vamos encontrar uma rede em estrela
de forma simétrica (ponto central localizado a uma distância igual de todos os computadores). Isso não
descaracteriza a topologia estrela.
 
 
Vantagens:
 
gerenciamento centralizado;
se um computador ou cabo falhar, a rede continua funcionando;
a análise de problemas é mais simples.
 
Desvantagens:
 
o número de computadores fica limitado ao número de portas do equipamento central (hub ou switch);
pode ter um custo elevado, pois cada computador terá que ter um cabo para se conectar com o equipamento
central;
se o equipamento central falhar, toda a rede é comprometida.
 
Na topologia anel, todos os computadores de uma rede se conectam em um loop fechado. Apesar do nome dessa
tipologia, os computadores não precisam estar organizados em um círculo. Basta que o primeiro computador esteja
conectado ao segundo, o segundo ao terceiro, e assim sucessivamente, até que o último computador esteja
conectado de volta ao primeiro.
 
 
Vantagens:
 
desempenho estável.
 
Desvantagens:
 
pouca tolerância a falhas. Se um computador falhar, toda a rede pode ser comprometida. Pois quando um
computador recebe uma mensagem pela rede, ele verifica se é o destinatário. Caso contrário, o computador
envia a mensagem para o próximo. Ou seja, cada computador na topologia anel tem um papel ativo
(repetidor).
 
Na topologia do tipo barramento, todos os computadores de uma rede se conectam em um único cabo (chamado
de barra ou bus). Quando um computador envia um sinal (mensagem), todos os outros recebem, mas somente
aquele a quem se destina pode aceitá-lo. Nesse tipo de topologia, os computadores devem assegurar que somente
um computador envie sinal a cada momento.
 
 
Vantagens:
 
requer menos cabos;
baixo custo
 
Desvantagens:
 
dificuldade em identificar a causa de um problema de transmissão, pois todos computadores compartilham o
mesmo meio físico;
excesso de colisões e lentidão principalmente em uma rede com muitos computadores.
 
As classificações apresentadas são as mais usadas. Existem outras, porém, conhecendo bem as características
dessas, já é possível resolver a maioria das questões que abordam o tema.
 
Além das classificações apresentadas, existe outra distinção no que se refere a topologia. Uma topologia pode ser:
 
física - refere-se à maneira como os dispositivos de rede estão organizados fisicamente. 
lógica - refere-se como os dados trafegam entre os dispositivos de rede.
 
Essa distinção existe porque a topologia física e lógica podem ser distintas em uma mesma rede. Por exemplo,
dificilmente, uma rede vai estar fisicamente em anel. O mais comum é a rede utilizar um hub que internamente
possui um anel, assim, os computadores conectados nesse hub trabalham como se realmente estivessem
conectados em anel, mas fisicamente estão conectados utilizando a topologia estrela. Ou seja, a topologia física é
estrela e a topologia lógica é anel.
 
Wireless (Rede sem fio)
 
Wireless (rede sem fio) é uma tecnologia de rede utilizada para interconectar computadores que, em vez de
transmitir sinais por meio de um cabo, usa sinais de rádio frequência através do ar. Portanto, a primeira diferença
que notamos entre uma rede "tradicional" com cabos e uma rede sem fio é o meio de  transmissão dos dados. Além
dessa diferença, podemos verificar que um dispositivo conectado a uma rede sem fio tem mais liberdade de
locomoção, pois não está "preso" a um cabo. 
 
Uma rede wireless pode ser formada por dispositivos wireless e, opcionalmente, por um equipamento central que
provê um ponto de acesso comum.
 
As redes formadas apenas por dispositivos wireless (sem um ponto de acesso comum) são chamadas de ad hoc. Esse
tipo de rede wireless é isolada (não consegue transmitir dados para outras redes) e independente. Já uma rede
formada por dispositivos wireless e um equipamento central (conhecido como access point) consegue se comunicar
com outras redes.
 
 
Algumas desvantagens da rede wireless:
 
Atenuação - a força do sinal diminui rapidamente, pois é enviado em todas as direções.
Interferência - a comunicação entre um emissor e um receptor pode sofrer interferência de outro dispositivo
que esteja usando a mesma frequência.
 
Redes sem fio podem ser classificadas quanto a sua dimensão:
 
WPAN (Wireless Personal Area Network ou rede pessoal sem fio) – Ex.: Bluetooth. Essa tecnologia é uma
implementação do protocolo definido pelo padrão IEEE 802.15 e é utilizada em smartphones, notebooks,
impressoras, etc. 
WLAN (Wireless Local Area Network ou rede de área local sem fio) – Ex.: rede Wifi de uma casa ou empresa.
WMAN (Wireless Metropolitan Area Network ou rede de área metropolitana sem fio) – Ex.: WiMAX (Worldwide
Interoperability for Microwave Access ou Interoperabilidade Mundial para Acesso de Micro-ondas).
WWAN (Wireless Wide Area Network ou rede de longo alcance sem fio) – Ex.: rede 3G.
 
Resumo
► Rede é um conjunto de dispositivos conectados por links de comunicação. Isto é, dispositivos (que podem ser
computadores, impressoras, etc) interligados por algum meio de transmissão (um cabo, por exemplo) formam
uma rede.
 
► Uma rede de computadores utiliza um conjunto de regras para se comunicarem. Esse acordo é conhecido
como protocolo de rede. Isso permite que dispositivos diferentes possam conversar e se entender.
 
► O fluxo de uma comunicação pode ser do tipo simplex (comunicação unidirecional), half-duplex (comunicação
bidirecional, mas que não ocorre ao mesmo tempo) ou full-duplex (a transmissão e recepção dos dados pode
acontecer ao mesmo tempo).
 
► As redes podem ser classificadas quanto a sua dimensão em:
 
PAN (Personal Area Network ou rede de área pessoal) - rede de tamanho reduzido que geralmente se refere a
uma pequena rede doméstica.
LAN (Local Area Network ou rede de área local) - rede que abrange uma área geográfica pequena (limitada a 10
km no máximo).
MAN (Metropolitan Area Network ou rede de área metropolitana) - rede projetada para cobrir uma cidade que
interliga vários LAN geograficamente próximos.
WAN (Wide Area Network ou rede de longo alcance) - rede que abrange uma grande área geográfica. A Internet
é a maior WAN que existe.
 
► As redes podem ser classificadas quanto a sua forma (topologia):
 
estrela - todos os computadores de uma rede se conectam a um ponto central.
anel - todos os computadores de uma rede se conectam em um loop fechado (formando um círculo).
barramento - todos os computadores de uma rede se conectam em um único cabo (chamado de barra ou
bus).
 
A topologia pode ser do tipo física (refere-se à maneira como os dispositivos de rede estão organizados fisicamente)
ou lógica (refere-se como os dados trafegam entre os dispositivos de rede).
 
► Wireless (rede sem fio) é uma tecnologia de rede utilizada para interconectar computadores que, em vez de
transmitir sinais por meio de um cabo, usa sinais de rádio frequência através do ar. Uma rede wireless pode ser
formada por dispositivos wireless e, opcionalmente, por um equipamento central (access point) que provê um ponto
de acesso comum.
 
Texto: Professor(a) Ramon Ahnert Azeredo
Proibida a reprodução e comercialização sem autorização
Usuário: FERNANDO PINHEIRO DE BRITO, fernandobritosc@gmail.com, CPF: 02049894180
