Aula 01
TJs - Curso Regular (Analista Judiciário -
Área Administrativa) Informática
Autor:
Diego Carvalho, Renato da Costa,
Equipe Informática e TI
22 de Agosto de 2025
95298789153 - Sibeli Maria Linhares Santos
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
Índice
..............................................................................................................................................................................................
1) Redes de Computadores - Parte 2
3
..............................................................................................................................................................................................
2) Redes de Computadores - Parte 2 - Glossário
62
..............................................................................................................................................................................................
3) Questões Comentadas - Redes de Computadores - Parte 2 - Multibancas
65
..............................................................................................................................................................................................
4) Lista de Questões - Redes de Computadores - Parte 2 - Multibancas
74
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
2
80
APRESENTAÇÃO DA AULA 
 
Fala, galera! O assunto da nossa aula de hoje é Protocolos de Comunicação! Pessoal, não há como 
se falar em redes de computadores como a internet sem falar sobre protocolos de comunicação. 
Para utilizar a Internet, você precisará dos protocolos IP, TCP ou UDP; para utilizar um navegador, 
você precisará dos protocolos HTTP, HTTPS e DNS; para enviar/receber e-mail, você precisará dos 
protocolos SMTP, POP3 ou IMAP; e assim por diante... 
 
 
PROFESSOR DIEGO CARVALHO - www.instagram.com/professordiegocarvalho 
 
 
 
Galera, todos os tópicos da aula possuem Faixas de Incidência, que indicam se o assunto cai 
muito ou pouco em prova. Diego, se cai pouco para que colocar em aula? Cair pouco não significa 
que não cairá justamente na sua prova! A ideia aqui é: se você está com pouco tempo e precisa ver 
somente aquilo que cai mais, você pode filtrar pelas incidências média, alta e altíssima; se você tem 
tempo sobrando e quer ver tudo, vejam também as incidências baixas e baixíssimas. Fechado? 
 
INCIDÊNCIA EM PROVA: baixíssima 
 
INCIDÊNCIA EM PROVA: baixa 
 
INCIDÊNCIA EM PROVA: média 
 
INCIDÊNCIA EM PROVA: ALTA 
 
INCIDÊNCIA EM PROVA: Altíssima 
 
Além disso, essas faixas não são por banca – é baseado tanto na quantidade de vezes que caiu em 
prova independentemente da banca e também em minhas avaliações sobre cada assunto... 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
3
80
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
4
80
PROTOCOLOS DE COMUNICAÇÃO 
Conceitos Básicos 
INCIDÊNCIA EM PROVA: baixa 
 
PROTOCOLOS DE COMUNICAÇÃO 
Protocolos são conjuntos de regras e convenções que especificam como os dispositivos em uma rede devem se 
comunicar. Eles definem os formatos dos dados, a sequência de mensagens, a detecção e correção de erros, o 
controle de acesso e muitos outros aspectos necessários para a comunicação eficaz entre computadores em uma 
rede. Esses protocolos desempenham um papel fundamental na garantia de que diferentes dispositivos de rede, 
com hardware e software diversos, possam se comunicar e trocar informações de maneira consistente.  
 
Existe um renomado autor – chamado Andrew Tanenbaum – que afirma que “um protocolo é um 
acordo entre as partes que se comunicam, estabelecendo como se dará a comunicação”. Outro grande 
autor – chamado Behrouz Forouzan – declara que um “protocolo é um conjunto de regras que 
controlam a comunicação de dados”. Já esse que vos escreve – chamado Diego Carvalho – gosta 
de pensar em protocolos simplesmente como um idioma. 
 
Imagine que você está em um país estrangeiro e deseja se comunicar com os habitantes locais. 
Considere que você não conhece o idioma deles, e eles não conhecem o seu idioma. Para se 
entenderem, é necessário seguir regras específicas. Em uma rede de computadores, o idioma é 
como os dados são representados e organizados para a comunicação. Isso inclui a estrutura e a 
gramática usadas para transmitir informações de um dispositivo para outro. 
 
Os protocolos de comunicação são como as regras que você segue para interagir com os habitantes 
locais. Eles definem como os dados são formatados, transmitidos e interpretados em uma rede. 
Cada protocolo tem regras específicas, assim como diferentes idiomas têm suas próprias 
gramáticas e vocabulários. Os dispositivos de rede, como computadores, roteadores e servidores, 
são como as pessoas que desejam se comunicar.  
 
Eles precisam seguir as regras do protocolo para trocar informações com outros dispositivos na 
rede, da mesma forma que você segue as regras do idioma local para se comunicar com os 
habitantes locais. Assim como você pode usar um intérprete ou um dicionário para traduzir seu 
idioma para o idioma local, os dispositivos de rede usam software e hardware para traduzir os 
dados do formato em que estão para o formato que os outros dispositivos entendem.  
 
Isso permite que diferentes dispositivos em uma rede se comuniquem, independentemente de suas 
diferenças de hardware ou software. Em resumo, os protocolos de comunicação são como os 
idiomas que os dispositivos de rede usam para se entender. Eles definem as regras para a 
transmissão de dados e permitem que diferentes dispositivos em uma rede se comuniquem, assim 
como seguir as regras de um idioma permite que você se comunique em um país estrangeiro. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
5
80
Hoje em dia, existe um conjunto de protocolos padrão da internet chamado TCP/IP! Ele é a base 
da comunicação de redes na internet e fornece as regras e convenções que permitem que 
dispositivos em redes diferentes se comuniquem entre si de maneira eficaz. Não importa se é um 
notebook, um tablet ou um computador, também não importa se utiliza Linux ou Windows ou se 
possui arquitetura x86 ou x64. Se estiver conectado à Internet, estará utilizando o TCP/IP!  
 
Modelo OSI/ISO 
INCIDÊNCIA EM PROVA: média 
 
MODELO OSI/ISO 
O Modelo OSI (Open Systems Interconnection / International Organization for Standardization) é um modelo de 
referência utilizado para entender como os protocolos de rede funcionam e interagem. Ele divide as funções de 
comunicação em uma rede de computadores em sete camadas, cada uma com um propósito específico. Essas 
camadas são organizadas hierarquicamente e servem como um guia para o desenvolvimento e a compreensão de 
protocolos de comunicação em redes. 
 
Nós já sabemos que uma rede é uma combinação de hardware e software que envia dados de uma 
localidade para outra. Para que dados possam trafegar de um ponto a outro, é necessário que 
tanto hardware quanto software realizem algumas tarefas. Pessoal, vocês já se perguntaram 
como um e-mail enviado para um amigo que mora do outro lado do mundo consegue chegar até o 
computador dele? Tudo acontece tão rápido que até parece simples, mas não é! 
 
Falando especificamente do contexto de softwares, a atividade de enviar um e-mail pode ser 
dividida em várias tarefas, cada uma das quais realizada por uma camada de software 
diferente. Professor, não estou entendendo bulhufas! Imaginem dois amigos se comunicando por 
cartas! O processo de enviar uma carta a um amigo seria complexo se não existisse nenhum serviço 
disponível das agências dos correios, concordam? Vejamos... 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
6
80
 
Na imagem anterior, temos um remetente, um destinatário e um transportador – 
provavelmente um carteiro. Olhando apenas para o lado do remetente, nós temos três tarefas que 
podem ser divididas em camadas; durante o transporte, a carta se encontra a caminho de seu 
destinatário (nesse momento, não nos interessa analisar as tarefas realizadas pelo transporte); por 
fim, ocorre de forma similar do lado direito, mas em ordem inversa. 
 
De acordo com nossa análise, há três tarefas distintas no lado do remetente e outras três do 
destinatário, sendo que elas devem ser realizadas na sequência correta. Note que cada camada no 
lado do remetente usa os serviços da camada imediatamente inferior. O remetente na camada 
mais alta utiliza os serviços da camada intermediária; a camada intermediária usa os serviços da 
camada mais baixa; e a camada mais baixa utiliza os serviços do transportador. 
 
A passagem de dados pelas camadas do dispositivo entre emissor e receptor é possível graças a 
uma interface entre cada par de camadas adjacentes. Cada interface define as informações e 
serviços que uma camada deve fornecer para a camada superior. Desde que uma camada forneça 
os serviços esperados para a camada superior, a implantação específica de suas funções pode 
ser modificada ou substituída, sem exigir mudanças nas camadas adjacentes. 
 
Galera, dividir um problema em camadas com tarefas e serviços específicos é uma excelente 
estratégia para reduzir a complexidade de um problema. Pois bem... e se eu dissesse para vocês 
que os engenheiros e cientistas pioneiros no estudo de redes de computadores decidiram utilizar essa 
mesma ideia? A ISO (International Standards Organization) criou um modelo conceitual para auxiliar 
a compreender e projetar um modelo de redes de computadores: Modelo OSI. 
 
Esse modelo é considerado um modelo de sistema aberto. Ele foi projetado para promover a 
interoperabilidade entre diferentes sistemas de rede e fabricantes, permitindo que sistemas de 
diferentes origens se comuniquem de maneira eficaz. A ideia por trás de um sistema aberto é que 
ele não é restrito a uma única entidade ou fabricante, mas segue padrões abertos que são 
amplamente aceitos e seguidos pela indústria de tecnologia.  
 
Isso possibilita a criação de redes em que dispositivos de diferentes fabricantes possam funcionar 
em conjunto de forma harmoniosa, seguindo as especificações do Modelo OSI. 
 
numeração 
CAMADA 
Descrição 
protocolos 
7 
APLICAÇÃO 
 
Camada responsável por habilitar o usuário, seja ele 
humano ou software, a estabelecer a comunicação entre 
aplicações e a acessar a rede.  
HTTP, SMTP, FTP, 
SSH, TELNET, SNMP, 
POP3, IMAP, DNS. 
6 
APRESENTAÇÃO 
 
Camada responsável por definir o formato para troca de 
dados entre computadores, como se fosse um tradutor.  
 
AFP, ICA, LPP, NCP, 
NDR, TOX, XDR, PAD. 
5 
SESSÃO 
 
Camada responsável por permitir que duas ou mais 
aplicações em computadores diferentes possam abrir, usar 
e fechar uma conexão, chamada sessão.  
NETBIOS. 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
7
80
4 
TRANSPORTE 
 
Camada responsável por organizar dados em segmentos e 
que eles cheguem ao destino livre de erros (sem perdas, 
sem duplicações e na ordem correta). 
TCP, UDP, NETBEUI. 
3 
REDE 
 
Camada responsável pelo endereçamento, roteamento e 
entrega de pacotes individuais de dados desde sua origem 
até o seu destino, provavelmente através de várias redes.  
IP, ICMP, ARP RARP, 
NAT. 
2 
ENLACE 
 
Camada responsável por organizar os dados em frames (ou 
quadros) e por estabelecer uma conexão nó-a-nó entre dois 
dispositivos físicos que compartilham o mesmo meio físico.  
Ethernet, Token Ring, 
Bluetooth, Wi-Fi. 
1 
FÍSICA 
 
Camada responsável por definir as especificações elétricas 
e físicas da conexão de dados.  
 
USB, DSL. 
 
MNEMÔNICO das camadas1 
F 
E 
R 
T 
S 
A 
A 
FÍSICA 
ENLACE 
REDE 
TRANSPORTE 
SESSÃO 
APRESENTAÇÃO 
APLICAÇÃO 
FLAMENGO 
ENSACOU NA 
REDE 
TRÊS 
SAPECADAS NO 
ATLÉTICO E 
avaí 
 
O Modelo OSI é basicamente um modelo de referência para conexão e projetos de sistemas de 
redes que se baseia em camadas sobrepostas. Sendo bem rigoroso, esse modelo não é uma 
arquitetura de rede, dado que não especifica serviços e protocolos exatos que devem ser utilizados 
em cada camada. Em outras palavras, nem sempre será possível “encaixar” um protocolo em uma 
camada específica do Modelo OSI (Ex: X.25 é um protocolo que atua nas três primeiras camadas). 
 
 
 
 
Esse modelo é apenas uma abstração teórica – uma referência conceitual – usado pela 
academia para representar o que seria um modelo perfeito de rede com suas respectivas 
descrições de camadas. Ele tem uma função mais didática do que pragmática. Não se trata 
de um modelo utilizado atualmente em redes de computadores – na prática, a arquitetura 
utilizada atualmente é o TCP/IP. 
 
 
1 Se vocês quiserem, podem memorizar na ordem inversa das camadas também: Aplicação > Apresentação > Sessão > Transporte > Rede > Enlace 
> Física – Mnemônico: Até A Sua Tia Ri Enquanto Fofoca 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
8
80
Nós sabemos que a comunicação entre dois computadores é 
extremamente complexa, logo esse modelo sugere dividir essa 
complexidade em uma estrutura de sete camadas distintas, porém 
relacionadas entre si, cada uma das quais definindo uma parte do 
processo de transferência de informações através de uma rede. 
Compreender esses conceitos é importante para entender 
posteriormente a função de cada protocolo. Nos tópicos seguintes, 
nós veremos a função de cada uma dessas camadas. Vem comigo... é 
legal! Eu juro... no fim da aula, tudo fará sentido! 
 
Camada Física 
 
A camada física coordena as funções necessárias para transportar um fluxo de bits através de 
um meio físico. Ela trata das especificações mecânicas e elétricas da interface e do meio de 
transmissão e também define os procedimentos e funções que os dispositivos físicos e interfaces 
têm de executar para que a transmissão seja possível. A imagem seguinte mostra a posição da 
camada física em relação ao meio de transmissão e a camada de enlace. 
 
Características da CAMADA FÍSICA 
Responsável por definir as especificações dos meios de transmissão, como sinais elétricos, ópticos ou de rádio. 
Responsável por definir as especificações físicas dos dispositivos de rede, como cabos, conectores e transceptores. 
Responsável por definir como os bits serão codificados para serem transmitidos como sinais elétricos, ópticos, etc. 
Responsável por definir o sentido das transmissões entre dois dispositivos: simplex, Half-duplex ou full-duplex. 
Responsável por descrever a topologia da rede, ou seja, como os dispositivos estão fisicamente conectados. 
Responsável por transmitir e recepcionar bits brutos. 
Responsável por definir os níveis de voltagem, frequência e modulação para a transmissão de dados. 
Essa camada não se preocupa com o conteúdo dos dados, apenas com sua transmissão física. 
 
Camada de Enlace 
 
A camada de enlace de dados transforma a camada física de um meio de transmissão bruto em 
um link confiável. Ela faz com que a camada física pareça livre de erros para a camada superior (a 
camada de rede). Ela oferece diversos serviços: empacotamento de bits em quadros (ou frames); 
oferecer um endereçamento físico; realizar o controle de fluxo, controle erros, correção de erros, 
controle acesso; etc.  
 
A imagem apresentada a seguir representa como essa camada empacota conjuntos de bits no que 
chamamos de quadros (ou frames). Vejamos: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
9
80
 
 
Agora vamos detalhar um pouco mais três serviços oferecidos por essa camada: controle de fluxo, 
controle de erros e controle de acesso: 
 
▪ Controle de Fluxo: previne a sobrecarga do receptor ajustando a taxa de transmissão de dados. 
Um exemplo é o método de Janelas Deslizantes, onde o receptor informa ao emissor sua 
capacidade de recebimento, permitindo um ajuste eficaz da taxa de envio. Isso garante a 
entrega eficiente de dados sem sobrecarregar o receptor, similar a um garçom em um 
restaurante que carrega uma quantidade limitada de pratos por vez para evitar acidentes. 
 
▪ Controle de Erros: garante a confiabilidade na transmissão de dados, detectando e corrigindo 
erros. A camada de enlace adiciona bits de verificação de erro ao final dos quadros de dados. 
Técnicas como CRC, Verificação de Paridade e Checksum são usadas para detectar erros. Se 
detectado, o quadro pode ser descartado e sua retransmissão solicitada. Isso é semelhante a um 
garçom verificando se um prato está danificado ou errado antes de entregá-lo ao cliente. 
 
▪ Controle de Acesso: determina qual dispositivo tem controle do link de comunicação em redes 
onde múltiplos dispositivos estão conectados ao mesmo link. A camada de enlace é dividida em 
duas subcamadas: LLC e MAC. A primeira lida com controle de fluxo e erros, enquanto a segunda 
gerencia o acesso ao meio de comunicação, usando métodos específicos para diferentes tipos 
de redes, como CSMA/CD para Ethernet ou tokens para Token Ring. 
 
 
 
 
Características da CAMADA de enlace 
Responsável pela comunicação direta entre dispositivos adjacentes na mesma rede local. 
Responsável por fornecer mecanismos de detecção e correção de erros. 
Responsável por controlar o acesso ao meio compartilhado, quando necessário. 
Responsável por definir os endereços físicos dos dispositivos na rede (Endereço MAC). 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
10
80
Responsável por realizar o controle de fluxo e acesso à camada de enlace. 
É dividida em duas subcamadas: LLC (Camada de Controle Lógico) e MAC (Controle de Acesso ao Meio). 
 
Camada de Rede 
 
A camada de rede é responsável pela entrega de um pacote desde sua origem até o seu destino, 
possivelmente através de várias redes. Embora a camada de enlace coordene a entrega do pacote 
entre dois sistemas na mesma rede, a camada de rede busca transmitir cada pacote de seu ponto 
de origem até seu destino final. Se dois sistemas estiverem conectados ao mesmo link, em geral 
não há a necessidade de uma camada de rede. 
 
Entretanto, se dois sistemas estiverem conectados a redes diferentes por meio de dispositivos 
intermediários de conexão entre as redes (como roteadores), normalmente, há a necessidade da 
camada de rede para realizar a entrega da origem até o destino. Essa camada é responsável pela 
entrega de pacotes individuais de dados desde o host (máquina) de origem até o host de 
destino. Além disso, é responsável pelo endereçamento lógico e pelo roteamento.  
 
A imagem apresentada a seguir representa como essa camada empacota conjuntos de frames no 
que chamamos de pacotes (ou packets). Vejamos: 
 
 
 
O endereçamento físico (Endereço MAC) implementado na camada de enlace trata do problema 
de endereçamento localmente. Se um pacote ultrapassar os limites da rede, precisaremos de um 
outro sistema de endereçamento para ajudar a distinguir os sistemas de origem e destino. A 
camada de rede adiciona um cabeçalho ao pacote proveniente da camada superior que, entre 
outras coisas, inclui o endereçamento lógico (Endereço IP) do emissor e do receptor.  
 
Características da CAMADA de rede 
Responsável pelo roteamento, permitindo que pacotes sejam enviados da origem ao destino em redes distintas. 
Responsável por definir os endereços lógicos dos dispositivos na rede, como os endereços IP. 
Responsável por realizar o controle de congestionamento e encaminhamento dos pacotes de dados. 
Responsável por dividir pacotes longos em fragmentos menores para transmissão e reagrupá-los no destino. 
Responsável por implementar tabelas de roteamento para decidir o melhor caminho para encaminhar os pacotes. 
 
Camada de Transporte 
 
A camada de transporte é responsável pela entrega processo a processo de toda a mensagem. 
Processo é a instância de uma aplicação que está sendo executada em uma máquina. Embora a 
camada de rede supervisione a entrega da origem ao destino dos pacotes individuais, ela não 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
11
80
reconhece qualquer relação entre esses pacotes. Ela trata cada um deles independentemente, 
como se cada trecho pertencesse a uma mensagem separada, ocorra isto ou não.  
 
Normalmente, computadores executam vários programas ao mesmo tempo. Logo, a entrega 
origem-ao-destino significa a entrega não apenas de um computador para o seguinte, mas também 
de um processo específico (programa em execução) em um computador para um processo 
específico no outro. A camada de rede encaminha cada pacote para o computador correto; a 
camada de transporte leva a mensagem inteira para o processo correto naquele computador. 
 
Na camada de transporte, uma mensagem é dividida em segmentos transmissíveis, com cada 
segmento contendo um número de sequência. Esses números permitem à camada de transporte 
remontar a mensagem corretamente após a chegada no destino e identificar e substituir 
pacotes que foram perdidos na transmissão. Ela também pode ser tanto orientada à conexão 
como não. Como assim, Diego? 
 
Uma camada de transporte não orientada à conexão trata cada segmento como um pacote 
independente e o entrega à camada de transporte na máquina de destino. Uma camada de 
transporte orientada à conexão estabelece em primeiro lugar uma conexão com a camada de 
transporte na máquina de destino antes de iniciar a entrega dos pacotes. Após todos os dados 
serem transferidos a conexão é encerrada. 
 
A camada de transporte também responsável por garantir que a mensagem chegue intacta e na 
sequência correta, supervisionando tanto o controle de erros como o controle de fluxo no nível 
origem-destino. Professor, a camada de enlace já não fazia um controle de erros e fluxo? Sim, mas 
ela fazia no nível nó e nó adjacente; aqui ocorre no nível origem-destino. A imagem seguinte 
apresenta o funcionamento da comunicação na camada de transporte: 
 
 
 
A imagem apresentada a seguir representa como essa camada empacota conjuntos de pacotes no 
que chamamos de segmentos (ou segments). Vejamos: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
12
80
 
 
Sendo rigoroso com a nomenclatura utilizada (e as bancas, infelizmente, nem sempre são), existem 
três tipos de comunicação diferentes:  
 
TIPOS DE COMUNICAÇÃO 
DESCRIÇÃO 
NÓ A NÓ 
Também chamada de comunicação ponto-a-ponto ou comunicação hop-a-hop, conecta 
um dispositivo intermediário a outro dispositivo intermediário adjacente. Trata-se do tipo 
de comunicação realizada na camada de enlace. 
HOST A HOST 
Conecta uma máquina a outra, ignorando dispositivos intermediários. Trata-se do tipo de 
comunicação realizada na camada de rede (Obs: autores divergem nesse ponto, alguns 
afirmam que a camada de rede também se comunica nó a nó). 
FIM A FIM 
Também chamada de comunicação processo-a-processo ou comunicação ponta-a-ponta, 
conecta processos ou aplicações rodando em duas máquinas. Trata-se do tipo de 
comunicação realizada na camada de transporte. 
 
 
 
Características da CAMADA de transporte 
Responsável por fornecer comunicação processo a processo entre dois dispositivos em diferentes sistemas finais. 
Responsável pela segmentação e reagrupamento de dados em pacotes ou segmentos para a transmissão. 
Oferece controle de fluxo para garantir que dispositivos transmitam dados em uma taxa compatível. 
Responsável por realizar a multiplexação e os segmentos sejam identificados corretamente no destino. 
Fornece detecção de erros e retransmissão de pacotes perdidos ou corrompidos, quando necessário. 
Responsável por implementar os protocolos de transporte. 
 
Camada de Sessão 
 
Essa camada é responsável por permitir que duas ou mais aplicações em computadores 
diferentes possam abrir, usar e fechar uma conexão, chamada sessão. Ela gerencia a 
comunicação para que, caso haja alguma interrupção, ela possa ser reiniciada do ponto da última 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
13
80
marcação recebida. Essa camada controla o diálogo da rede – estabelecendo, mantendo e 
sincronizando a interação entre sistemas que se comunicam. 
 
Essa camada possibilita a dois sistemas estabelecerem um diálogo, permitindo que a comunicação 
entre dois processos ocorra em modo half ou full-duplex. Ela também permite que um processo 
adicione pontos de verificação/sincronização, ao fluxo de dados. Exemplo: se um sistema estiver 
enviando um arquivo de 2.000 páginas, é recomendável inserir esses pontos a cada 100 páginas para 
garantir que cada unidade de 100 páginas foi recebida e confirmada de forma independente.  
 
Nesse caso, se ocorrer uma falha durante a transmissão da página 523, as únicas páginas que 
precisarão ser reenviadas após a recuperação do sistema serão as páginas 501 a 523.  
 
Características da CAMADA de sessão 
Responsável pelo estabelecimento, gerenciamento e encerramento de sessões de comunicação entre dispositivos. 
Controla o diálogo entre aplicativos em sistemas finais e coordena as interações entre eles. 
Realiza a sincronização dos dados, garantindo que eles sejam transmitidos de forma ordenada e sem duplicações. 
Responsável por fornecer serviços para garantir que a comunicação possa ser retomada após uma interrupção. 
Responsável por lidar com a detecção e correção de erros relacionados à sequência de mensagens. 
Responsável por implementar mecanismos de controle de diálogo, como controle de turnos e controle de token. 
 
Camada de Apresentação 
 
A camada de apresentação é responsável pela sintaxe e semântica das informações trocadas 
entre dois sistemas. Essa camada também é responsável pela tradução, compressão e criptografia 
dos dados – além de estabelecer formato para troca de dados entre computadores. Ela cuida das 
diferenças sintáticas na representação de dados. Um exemplo de um serviço de apresentação seria 
a conversão de dados codificados em EBCDIC para dados codificados em ASCII. 
 
Normalmente, processos (programas em execução) em dois sistemas em geral trocam informações 
na forma de strings (sequências de caracteres), números, entre outros. As informações têm de ser 
convertidas em fluxos de bits antes de serem transmitidas. Como diferentes computadores 
utilizam sistemas de codificação diferentes, a camada de apresentação é a camada responsável 
pela interoperabilidade entre esses métodos de codificação diferentes.  
 
A camada de apresentação no emissor traduz as informações de um formato específico do emissor 
em um formato comum. A camada de apresentação no receptor traduz o formato comum em um 
formato específico do receptor. E quando temos que transmitir informações confidenciais? Um 
sistema deve ser capaz de garantir privacidade! A criptografia significa que o emissor converte as 
informações originais em um outro formato e envia a mensagem resultante pela rede. 
 
A descriptografia reverte o processo original convertendo a mensagem de volta ao seu formato 
original. Por fim, a compressão de dados reduz o número de bits contidos nas informações. Ela 
se torna particularmente importante na transmissão de conteúdos multimídia, como texto, áudio e 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
14
80
vídeo. A camada de apresentação garante que os pratos sejam servidos da maneira que os clientes 
desejam, seja com enfeites especiais ou embalagens diferenciadas. 
 
Características da CAMADA de apresentação 
Responsável pela tradução, compressão e criptografia dos dados que serão transmitidos na rede. 
Lida com questões de representação dos dados, como codificação de caracteres e formatação de dados. 
Garante a interoperabilidade entre diferentes sistemas, permitindo a comunicação em diferentes formatos.  
Realiza a compressão de dados para otimizar a eficiência da transmissão. 
Pode criptografar os dados para fornecer segurança durante a transmissão. 
Lida com a detecção e correção de erros de representação de dados. 
 
Camada de Aplicação 
 
A camada de aplicação habilita o usuário, seja ele humano ou software, a acessar a rede. Ela 
fornece interface com o usuário e suporte a serviços, como e-mail, acesso e transferência de 
arquivos remotos, gerenciamento de bancos de dados compartilhados e outros tipos de serviços de 
informação distribuídos. Em suma: essa camada é responsável por prover serviços ao usuário. 
Vejamos suas principais características 
 
Características da CAMADA de aplicação 
Responsável por fornecer serviços de rede diretos aos aplicativos do usuário final. 
Envolve aplicativos de software, como navegadores, clientes de e-mail, e outros programas que utilizam a rede. 
Fornecimento de uma interface entre o aplicativo do usuário e as camadas inferiores do Modelo OSI. 
Implementa protocolos específicos de aplicação (Ex: HTTP para web e SMTP para e-mails). 
Realiza a comunicação com os aplicativos de usuário final, traduzindo os comandos e solicitações dos aplicativos. 
Fornecimento de serviços de aplicação (Ex: autenticação, transferência de arquivos, acesso a bancos de dados). 
 
 
 
Por fim, nós vimos na aula anterior os principais dispositivos de rede. Agora vejam na imagem em 
que camada trabalha cada um desses dispositivos. É importante notar que cada dispositivo 
trabalha em uma camada principal, mas todos trabalham nas camadas abaixo de sua principal. Em 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
15
80
outras palavras, as camadas são acumulativas – um roteador trabalha com foco na camada de rede, 
mas também trabalha – em algum nível – nas camadas física e de enlace.  
 
 
 
 
SWITCH 
ACCESS POINT 
ROTEADOR 
BRIDGE 
HUB 
PLACA DE REDE 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
16
80
Arquitetura TCP/IP 
INCIDÊNCIA EM PROVA: ALTA 
 
ARQUITETURA TCP/IP 
A arquitetura TCP/IP (Transmission Control Protocol / Internet Protocol) é um conjunto de protocolos de 
comunicação que são amplamente utilizados na internet e em redes locais. Ela fornece um conjunto de regras e 
especificações que permitem que diferentes dispositivos se comuniquem em redes de computadores, 
independentemente do fabricante ou sistema operacional. 
 
Nós acabamos de ver em detalhes o Modelo OSI e descobrimos que – apesar de ser um modelo 
conceitual bastante interessante e de facilitar o entendimento da comunicação entre redes – ele é 
apenas um modelo teórico utilizado didaticamente para mostrar o funcionamento ideal da 
comunicação de dados em uma rede de computadores. Ele não é uma tecnologia, nem um 
conjunto de protocolos, nem um software e só tem utilidade pedagógica.  
 
Na prática, o que é utilizado é a Arquitetura ou Pilha TCP/IP. Essa arquitetura foi desenvolvida – na 
verdade – antes do Modelo OSI. Dessa forma, as camadas que nós veremos a seguir não 
correspondem exatamente àquelas do Modelo OSI. A Arquitetura TCP/IP é o conjunto de 
protocolos e camadas utilizados para conectar várias redes diferentes de maneira uniforme: trata-
se do conjunto padrão de protocolos da Internet.  
 
A quantidade e nome das camadas apresentada a seguir para a Arquitetura TCP/IP foi baseada 
na documentação oficial (RFC 1122)2. No entanto, alguns autores modelam essa arquitetura com 
três, quatro ou cinco camadas de nomes bastante diversos. Observem que ela condensa as camadas 
de aplicação, apresentação e sessão na camada de aplicação. Ademais, ela condensa a camada 
física e de enlace na camada de enlace e chama a camada de rede de internet.  
 
 
2 O projeto original do TCP/IP prevê quatro camadas (conforme a RFC 1122). Apesar disso, como os modelos TCP/IP e OSI não combinam, há autores 
que defendem uma arquitetura híbrida de cinco camadas: física, enlace, rede, transporte e aplicação. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
17
80
 
 
 
 
Eventualmente, quando um servidor – uma máquina especializada – fornece os 
serviços de um protocolo, é comum chamar esse servidor pelo nome do protocolo 
que ele implementa. Isso facilita a compreensão e a identificação de servidores e 
seus propósitos. Logo, temos que: 
 
▪ Um Servidor que fornece serviços de apresentação de páginas web pode ser 
chamado de Servidor HTTP; 
▪ Um Servidor que fornece serviços de envio de e-mails pode ser chamado de 
Servidor SMTP; 
▪ Um Servidor que fornece serviços de tradução de domínios pode ser chamado 
de Servidor DNS; 
▪ Um Servidor que fornece serviços de transferência de arquivos pode ser 
chamado de Servidor FTP. 
 
Principais Protocolos 
 
Protocolos da Camada de Rede 
 
IP (Internet Protocol) 
INCIDÊNCIA EM PROVA: Altíssima 
 
INTERNET PROTOCOL (IP) 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
18
80
O IP é a base da comunicação na Internet, sendo responsável por rotear pacotes de dados de origem para destino 
em uma rede. Cada dispositivo conectado à Internet recebe um endereço IP exclusivo, que é usado para identificar 
e encaminhar dados para o destinatário correto. Quando um dispositivo deseja enviar dados para outro, ele divide 
os dados em pacotes. Cada pacote contém informações sobre o remetente, destinatário, dados reais e outros 
metadados – esses pacotes são então enviados pela rede. O roteamento é o processo pelo qual os pacotes são 
direcionados do remetente para o destinatário através de vários dispositivos intermediários, como roteadores. 
 
O que significa essa sigla? Essa sigla significa Internet Protocol (em português, Protocolo de 
Internet). Vamos traduzir também Internet? Inter significa entre e net significa rede, logo Internet 
significa entre redes. Agora vamos juntar tudo isso e dar um significado! IP é um protocolo – um 
conjunto de normas, padrões e convenções – para comunicação entre redes. O endereço IP define 
de forma única e universal a conexão de um dispositivo (Ex: um computador ou um roteador).  
 
Eles são exclusivos no sentido de que cada endereço deﬁne uma única conexão com a Internet 
– dois dispositivos jamais podem ter o mesmo endereço ao mesmo tempo na mesma rede. Além 
disso, eles são universais no sentido de que o sistema de endereçamento tem de ser aceito por 
qualquer host (máquina) que queira se conectar à Internet. Agora vamos ver uma analogia para 
entender o seu funcionamento... 
 
IP: Funcionamento 
 
Imagine que você queira enviar uma carta para um amigo que mora em uma outra cidade. Essa 
carta é como um pacote de dados na Internet. Vamos comparar cada elemento: 
 
- Passo 1: Endereço do Destinatário (Endereço IP) 
 
Antigamente, para enviar uma carta a alguém, você 
pegava 
um 
pedaço 
de 
papel, 
escrevia 
diversas 
informações, colocava dentro de um envelope com o 
endereço de origem (remetente) e endereço de destino 
(destinatário). Na internet, ocorre de maneira bastante 
similar: as informações que eu desejo transmitir são 
encapsuladas dentro de um envelope chamado Pacote IP, 
que contém necessariamente um endereço IP de origem e 
um endereço IP de destino. Na Internet, cada dispositivo 
possui um endereço IP exclusivo.  
 
A imagem anterior apresenta o formato de um Pacote IP (Versão 4). Notem que existem diversos 
campos, mas aqui vamos nos focar em apenas quatro:  
 
CAMPOS do ip 
DESCRIÇÃO 
VERSÃO Trata-se da versão do IP (IP Versão 4 ou IP Versão 6); 
ENDEREÇO DE ORIGEM Trata-se do IP do Remetente; 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
19
80
ENDEREÇO DE DESTINO Trata-se do IP do Destinatário; 
DADOS Trata-se da carga útil de dados que serão enviados. 
 
O Protocolo IP é responsável por especificar o formato desse Pacote IP que trafegará entre 
roteadores e sistemas finais. Voltando à nossa analogia: assim como no Pacote IP, um envelope 
pode conter outras informações além dos dados em si (Ex: carimbo de identificação, data de envio 
da carta, quantidade de palavras contidas, entre outros). Em outras palavras, o Pacote IP conterá 
os dados em si, além de um cabeçalho com diversas outras informações que facilitem a entrega. 
 
- Passo 2: Divisão em Pacotes 
 
Agora uma pergunta: eu posso enviar um processo com 50.000 páginas pelos Correios? Posso! No 
entanto, os Correios não vão conseguir colocar 50.000 páginas dentro de um único envelope!  
 
Os Correios impõem um tamanho limite para o pacote que ele é 
capaz de transportar, da mesma forma que existe um tamanho 
limite para o pacote IP. E qual é o tamanho, Diego? Esse limite é de 
64 Kb! Caraca, professor... por que tão pequeno? Galera, quando a 
internet foi criada, isso era uma quantidade absurda de informação. 
Vejam essa imagem ao lado: isso é um HD de 1960 capaz de 
armazenar estrondosos 5 Mb de informação. Incrível, não? Claro que 
não é mais assim hoje em dia. Uma foto tirada pelo celular possui 
cerca de 6.4 Mb (= 6400 Kb). E se eu quiser enviar essa foto para outra 
pessoa, caberá tudo em um pacote? Jamais! O IP terá que dividir a 
foto em pacotes de 64 Kb. Como 6400 Kb dividido por 64 Kb é 100, 
teremos que dividir a foto em 100 pacotinhos e enviá-los um a um.  
 
Em suma: o IP divide dados grandes em pacotes menores antes de enviá-los pela rede em um 
processo conhecido como Fragmentação de Pacotes. Ele ocorre quando um pacote é muito 
grande para ser transmitido em uma rede com uma determinada capacidade máxima de carga útil. 
Quando um roteador encontra um pacote que é maior do que o tamanho máximo permitido pela 
rede seguinte (MTU - Maximum Transmission Unit), ele divide o pacote em fragmentos menores.  
 
Cada fragmento contém uma parte dos dados originais e é transmitido separadamente pela rede. 
No destino, os fragmentos são reagrupados para recriar o pacote original. 
 
- Passo 3: Correios (Roteadores) 
 
Agora que você já fragmentou sua encomenda em envelopes menores, você poderá entregá-los em 
uma agência dos correios local. Essa agência é como o roteador mais próximo. Sabe quando você 
vai rastrear um pacote dos correios em que ele mostra cada agência que o pacote passou até chegar à 
sua casa? Pois é, os correios são os responsáveis por encaminhar cada envelope para a agência de 
destino. Os roteadores fazem o mesmo, encaminhando pacotes pela rede. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
20
80
 
- Passo 4: Roteamento 
 
O roteamento refere-se ao processo de encaminhar pacotes de dados de um dispositivo de 
origem para um dispositivo de destino através de uma rede. Envolve a escolha do caminho mais 
eficiente e adequado entre os diversos dispositivos interconectados na rede, assim como cada 
agência dos correios sabe como chegar a outras agências. Eles decidem para onde encaminhar cada 
envelope com base no endereço do destinatário. 
 
O dispositivo de origem envia o pacote para o roteador mais próximo. O roteador consulta sua 
tabela de roteamento para determinar para onde encaminhar o pacote. Com base nas informações 
da tabela de roteamento, o roteador decide qual é o próximo dispositivo (roteador) ao longo do 
caminho até o destino. Essa escolha é feita com base no endereço IP de destino e nas 
informações de roteamento. 
 
O roteador encaminha o pacote para o próximo dispositivo ao longo do caminho. Esse processo se 
repete em cada roteador ao longo do percurso até o pacote atingir seu destino final. Os roteadores 
utilizam métricas (como distância, largura de banda, atraso) para determinar a melhor rota para um 
pacote, escolhendo caminhos eficientes com base nas condições da rede. Da mesma forma, os 
Correios utilizam métricas para determinar a melhor rota de entrega de um pacote. 
 
- Passo 5: Entrega ao Destinatário 
 
Finalmente, os envelopes chegam à agência dos correios mais próxima do seu amigo, que os 
encaminha até a casa dele. Já os roteadores garantem que pacotes cheguem ao destino final. 
 
- Passo 6: Montagem de Pacotes 
 
Seu amigo recebe os envelopes e os reúne para reconstruir a carta original. Dispositivos no destino 
fazem algo semelhante, montando os pacotes para obter os dados originais. 
 
IP: Características 
 
O IP possui duas características importantes que podem cair em prova. Trata-se de um protocolo 
de distribuição de pacotes não confiável (ou de melhor esforço) e sem conexão. Vejamos: 
 
a) Não confiável 
 
O IP é considerado um protocolo de comunicação "não confiável" porque não fornece garantias de 
entrega de dados, confirmação de recebimento ou controle de fluxo. Ele é projetado para fornecer 
roteamento eficiente de pacotes de dados pela rede, mas não inclui mecanismos embutidos 
para verificar se os pacotes realmente chegam ao destino. Vejamos algumas razões pelas quais 
esse protocolo é considerado não confiável: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
21
80
Características 
DESCRIÇÃO 
Sem confirmação de 
entrega 
IP não possui um mecanismo integrado para confirmar se um pacote de dados chegou ao 
destino. Após enviar um pacote, não há garantia de que ele será recebido com sucesso. 
 
Sem controle de 
fluxo 
IP não gerencia o controle de fluxo, o que significa que não ajusta automaticamente a taxa 
de transmissão de dados com base na capacidade da rede ou na capacidade de 
processamento do destinatário. Isso pode levar a congestionamentos e perda de pacotes. 
Sem reordenação de 
pacotes 
IP não reordena automaticamente pacotes fora de ordem. Se os pacotes forem recebidos 
fora de sequência, cabe às camadas superiores, como o protocolo de transporte (como 
TCP), lidar com a reordenação. 
Sem garantia de 
integridade 
IP não verifica a integridade dos dados dentro dos pacotes. Se houver corrupção nos dados 
durante a transmissão, o IP não detectará ou corrigirá automaticamente. 
 
 
b) Sem Conexão 
 
O IP é considerado um protocolo "sem conexão" porque não estabelece uma conexão prévia antes 
de enviar dados. Em vez disso, cada pacote de dados contém dados suficientes para serem 
tratados independentemente e roteados separadamente pelos dispositivos de rede. Dessa 
forma, eles podem seguir caminhos diferentes pela rede e chegar ao destino em ordens diferentes 
daquela em que foram enviados. 
 
IP: Classificação 
 
Endereços IP podem ser classificados em estáticos ou dinâmicos. Essa classificação trata de 
como os endereços IP são atribuídos aos dispositivos em uma rede de computadores. A escolha 
entre endereços IP estáticos e dinâmicos depende dos requisitos específicos da rede, da escala da 
infraestrutura e das necessidades de gestão dos endereços. Muitas redes utilizam uma combinação 
de ambos para atender às diversas demandas. Vejamos... 
 
a) IP Estático 
 
Também chamado de IP Fixo, são atribuídos manualmente aos dispositivos e permanecem 
constantes, não mudando automaticamente. A sua configuração geralmente é feita 
manualmente pelo administrador da rede. Isso pode ser feito no dispositivo em si ou por meio de 
configurações no servidor DHCP (veremos mais à frente). Sua utilização é mais comum quando um 
dispositivo precisa ter sempre o mesmo endereço (Ex: servidores, impressoras e roteadores). 
 
As principais vantagens desse tipo de Endereço IP é a facilidade da administração, dado que os 
endereços são previsíveis e conhecidos. Além disso, conforme já vimos, pode ser útil para 
dispositivos que precisam ser sempre acessíveis com o mesmo endereço. Sabe quem tem um IP 
Estático? O servidor web do Estratégia Concursos! Toda vez que você acessa a página do Estratégia, 
ela acessa o mesmo servidor web que possui sempre o mesmo Endereço IP. 
 
b) IP Dinâmico 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
22
80
 
São atribuídos automaticamente por um servidor DHCP na rede sempre quando um dispositivo 
se conecta. Os dispositivos obtêm um endereço temporário que precisa ser renovado 
periodicamente e o servidor DHCP gerencia esse processo de renovação. Os endereços IP 
dinâmicos são alocados conforme necessário, evitando a necessidade de atribuir manualmente 
endereços e permitindo um uso mais eficiente do espaço de endereço. 
 
Em suma, os dispositivos podem receber endereços IP diferentes em cada conexão, dependendo 
do pool de endereços disponíveis no servidor DHCP. Ele facilita a gestão em redes grandes, pois 
não é necessário atribuir manualmente endereços a cada dispositivo. Além disso, aumenta a 
eficiência na utilização do espaço de endereçamento. Sabe quem tem um IP Dinâmico? Eu (e muito 
provavelmente você). 
 
Pois é... cada vez que eu me conecto à internet, é atribuído um novo endereço IP a minha máquina. 
O IP Dinâmico é bem mais utilizado que o IP Estático, principalmente em redes domésticas. 
 
IP: Versionamento 
 
Agora vamos falar um pouquinho sobre versões do Protocolo IP. Nós temos basicamente duas 
versões: IPv4 (Versão 4) e IPv6 (Versão 6). Vamos iniciar nosso papo falando sobre o IPv4!  
 
a) IPv4 (Versão 4)  
 
Esse protocolo utiliza endereços de 32 bits, que podem ser representados por meio de duas 
notações: Notação de Octetos Binários ou Notação Decimal Pontuada. Ambas as notações são 
comumente utilizadas, mas a Notação Decimal Pontuada é mais intuitiva para os humanos, 
facilitando a leitura e compreensão dos endereços IP. No entanto, antes de prosseguir, vamos falar 
um pouco sobre numeração... 
 
 
 
Existem diversos sistemas de numeração! Seres humanos utilizam um sistema de 
numeração decimal, isto é, nós fazemos contas utilizando dez dígitos (0, 1, 2, 3, 4, 5, 6, 7, 8 
e 9). Já os computadores utilizam um sistema de numeração binária, isto é, eles fazem 
contas utilizando apenas dois dígitos (0 e 1) – o nome desse dígito binário é Bit (do inglês, 
Binary Digit). É possível converter números de um sistema para outro sem nenhum 
inconveniente. Vejam abaixo o número 123 em outros sistemas numéricos: 
 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
23
80
 
Na notação de octetos binários, os 32 bits são representados por meio de quatro conjuntos de oito 
bits, sendo que esse conjunto de 8 bits (ou 1 byte) é chamado de octeto: 
 
Endereço Ip com notação de octetos binários 
10101010 
01010101 
11100111 
10111101 
 
Ocorre que utilizar endereço em bits pode acabar incorrendo em erros. Como só temos os dígitos 0 
e 1, se você tem miopia, pode acabar errando. Por conta disso, alguém teve a brilhante ideia de 
converter esses números do sistema binário para o sistema decimal. Dessa forma, cada octeto 
em binário pode ir de 0 a 255 em decimal (você nunca vai encontrar um número que esteja fora 
dessa extensão). Se convertermos os números da notação anterior para notação decimal, teremos: 
 
Endereço IP com NOTAÇÃO DECIMAl pontuada 
170 
. 
85 
. 
231 
. 
189 
 
Professor, está tudo muito abstrato! Você pode dar um exemplo? Claro! Para tal, eu vou propor um 
exercício para vocês: eu quero que vocês pressionem simultaneamente as teclas Windows + R. 
 
 
 
Quando vocês fizerem isso, aparecerá essa imagem da esquerda. Eu quero, então, que vocês 
escrevam o comando cmd e cliquem em OK:  
 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
24
80
Notem que será exibida essa janela da esquerda. Em seguida, eu quero que vocês escrevam o 
comando ipconfig e aperte ENTER. No meu caso, foi exibido: 
 
 
 
Eu destaquei em branco uma informação importante: meu Endereço IPv4 é 192.168.0.17! Logo, se 
alguém quiser me encontrar nesse dia, esse era o endereço lógico do meu computador na Internet.  
 
Pessoal, é importante entender que esses endereços que vimos anteriormente no IPv4 não são 
aleatórios: existem diversas regras que devem ser obedecidas para cada endereço. Uma delas é o 
Endereçamento por Classes. O que é isso, Diego? Trata-se de uma abordagem para a alocação de 
endereços IP e foram criadas para alocar blocos de endereços de maneira mais estruturada e 
eficiente. 
 
Com o crescimento da internet, era necessário alocar blocos de endereços IP de acordo com o 
tamanho das redes. Redes maiores precisavam de mais endereços do que redes menores. Para 
atender a essa demanda por tamanhos variados de blocos de endereços, as classes foram 
introduzidas para estruturar e classificar os endereços IP em categorias que correspondessem ao 
tamanho das redes. 
 
As classes permitiam identificar o tamanho aproximado da rede com base no endereço IP. Por 
exemplo, uma empresa que necessitasse de muitos endereços teria uma classe de endereço 
diferente de uma rede doméstica pequena. Galera, nós já sabemos que um endereço IPv4 possui 32 
bits e já sabemos também que um bit só pode ter dois valores (0 ou 1). Logo, nós temos 232 ou 
4.294.967.296 endereços possíveis. 
 
O endereçamento por classes busca dividir esse espaço de endereços possíveis em cinco classes: 
Classe A, Classe B, Classe C, Classe D e Classe E. Logo, todo e qualquer IP pode ser classificado em 
uma dessas cinco classes. E como eu faço para descobrir à qual classe um endereço pertence, 
professor? É extremamente simples: basta analisar o primeiro número (na notação decimal 
pontuada) conforme é apresentado na tabela seguinte: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
25
80
1º octeto 
CLASSE 
UTILIZAÇÃO 
0 A 1273 
A 
Inicialmente destinado a grandes organizações. 
128 A 191 
B 
Inicialmente destinado a organizações de médio porte. 
192 A 223 
C 
Inicialmente destinado a pequenas organizações. 
224 A 239 
D 
Inicialmente reservado para multicast. 
240 A 255 
E 
Inicialmente reservado para testes. 
 
Como interpreta essa tabela? É bem simples! Se o primeiro número de um endereço IP for de 1 a 126, 
ele será da Classe A (geralmente utilizado por grandes organizações); se for de 128 a 191, ele será 
da Classe B (geralmente utilizado por organizações de médio porte); se for e 192 a 223, ele será da 
Classe C (geralmente utilizado por pequenas organizações); se for de 224 a 239, será da Classe D 
(reservado para multicast); e se for de 240 a 255, será da Classe E (reservado para testes). 
 
Nós vimos acima que existem quase 4.3 bilhões de possibilidades de Endereços IP, no entanto esse 
valor é bem menor na prática. Endereços de Classe D e Classe E não podem ser utilizados na 
internet. Além disso, vários endereços são proprietários ou reservados para alguma organização. 
Vocês sabiam que a Apple é dona de todo IP que se inicia pelo número 17 e a Ford de todo IP que se 
inicia por 19? Pois é... apenas cerca de metade dos endereços podem realmente ser utilizados. 
 
Atualmente, a utilização das classes de endereçamento foi amplamente substituída por 
abordagens mais flexíveis, permitindo uma alocação mais precisa de endereços com base nas 
necessidades específicas das redes, resultando em uma gestão mais eficiente do espaço de 
endereço disponível. Agora eu preciso fazer uma pequena confissão para vocês: eu menti na página 
anterior! Quando, Diego? Quando eu mostrei o meu endereço na janelinha preta... 
 
Aquele endereço não era meu endereço IPv4 real! Como assim, professor? Pessoal, todo dispositivo 
em uma mesma rede necessita de um Endereço IP único – não podem existir dois dispositivos 
com o mesmo Endereço IP! No entanto, com o passar dos anos a quantidade de dispositivos 
conectados à internet aumentou assustadoramente. Por exemplo: na minha casa, há dois 
smartphones, dois computadores, um notebook, dois tablets e dois smartwatches.  
 
Só na minha casa há nove dispositivos conectados à internet. E na casa do vizinho? E no condomínio? 
E no bairro? E na cidade? E no país? E no mundo? Lembrando que o nosso planeta acabou de alcançar 
a marca de 8 bilhões de pessoas – quatro vezes a quantidade efetiva de endereços possíveis no IPv4 
(e, como disse, nem todos estão disponíveis). Logo, algo precisava ser feito antes que 
chegássemos ao total esgotamento de endereços.  
 
Nesse momento, os engenheiros tiveram que arrumar uma solução enquanto não havia uma nova 
versão para o Protocolo IP. E como eles fizeram, Diego? Eles resolveram de uma maneira genial! 
Pensem comigo: uma coisa é a rede doméstica privada na sua casa/escritório e outra coisa é a 
 
3 Na verdade, endereços iniciados por 0 não podem ser utilizados na internet porque são endereços indefinidos (utilizados em contextos específicos) 
e endereços iniciados por 127 também não porque são endereços de loopback (reservado para testes). Não precisamos entrar em detalhes... 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
26
80
rede mundial de computadores (Internet). Logo, os engenheiros padronizaram algumas faixas de 
endereços que deveriam ser utilizados exclusivamente para redes privadas. 
 
Professor, eles reduziram mais ainda a quantidade de endereços efetivamente possíveis na internet? 
Sim (parece contraditório, mas vocês vão entender). Todo Endereço IP que estivesse dentro dessa 
faixa que eles convencionaram não poderiam ser utilizados na internet – eles só poderiam ser 
utilizados em redes internas. Que valores são esses? Na tabela a seguir, nós podemos ver quais são 
essas faixas de endereços: 
 
Classe 
Faixa de Endereços para redes privadas 
A 
10.0.0.0 até 10.255.255.255  
B 
172.16.0.0 até 172.31.255.255  
C 
192.168.0.0 até 192.168.255.255  
 
Professor, ainda não entendi por que você disse que mentiu? Pessoal, 
eu disse algumas páginas atrás que o meu IP era 192.168.0.17. 
Façam-me um favor: confiram agora na tabela apresentada se 
esse endereço informado está presente em alguma dessas faixas! 
Ora, está dentro da Classe C! Logo, eu não menti exatamente para 
vocês – eu apenas informei qual era o meu endereço IP dentro da 
minha rede doméstica – também chamado de IP Privado ou Local!  
 
Para deixar mais claro ainda, eu olhei nas configurações de rede do 
meu smartphone para descobrir qual era o IP dele: 192.168.0.20. 
Como meu celular está conectado na minha Wi-Fi, ele faz parte 
da minha rede doméstica, logo esse também possui um IP 
Privado ou Local. Em outras palavras, eu possuo sete 
equipamentos na minha casa e cada um possui um endereço privado 
diferente. Professor, eu ainda não entendi... 
 
Galera, a imagem ao lado representa a 
configuração básica da maioria das redes que 
temos em nossas casas. No caso, existem 
quatro dispositivos diferentes conectados a um 
equipamento que faz o papel de modem e/ou 
roteador e que se conecta à internet. Vejam se na 
casa de vocês não é exatamente dessa maneira... 
 
Na minha casa é assim: dois computadores e um notebook estão conectados via cabo ao 
modem/roteador e os outros dispositivos também estão conectados a ele, porém via Wi-Fi. Note 
que eu disse que o endereço do meu computador era 192.168.0.17 e o endereço do meu 
smartphone era 192.168.0.20. Ambos os endereços estão dentro da faixa de endereços 
privados, logo eles não existem na internet – existem apenas na rede interna. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
27
80
==6306a==
 
Vocês sabem que todo dispositivo em uma rede precisa ter um endereço IP. Ora, o modem/roteador 
não é um dispositivo? Sim, logo ele precisa ter um endereço IP! Sabe qual é o endereço dele? 
189.6.109.248. Esse endereço está contido em alguma das faixas de endereços privados? Não, logo 
ele é um endereço público. Então, a minha rede tem nove equipamentos – cada um com seu 
endereço pertencente a faixa de endereços privados.  
 
Já o meu roteador é o único dispositivo da minha rede local com um endereço pertencente a faixa 
de endereços públicos. Legal, mas como eu faço para que meus equipamentos se comuniquem com a 
internet se o endereço deles é privado, portanto não existe na internet? Agora vem à tona a criação 
genial dos engenheiros de redes: Network Address Translation (NAT). Trata-se de um recurso 
utilizado em roteadores e dispositivos de rede para traduzir endereços de uma rede para outra.  
 
Essa tecnologia desempenha um papel crucial em permitir que dispositivos de uma rede privada se 
comuniquem com a internet. Ela permite a um usuário ter internamente em sua rede doméstica 
uma grande quantidade de endereços privados e, externamente, possuir apenas um endereço 
público. Dessa forma, qualquer rede doméstica pode utilizar um endereço da faixa de endereços 
privados sem a necessidade de pedir permissão para provedores de internet.  
 
Eu disse para vocês diversas vezes que não podem existir equipamentos com o mesmo endereço IP 
em uma mesma rede. Ora, se meu computador é 192.168.0.17 na minha rede local e o seu também 
é 192.168.0.17 na sua rede local, não há nenhum problema porque estamos em redes diferentes. 
Logo, sempre que um pacote de dados sai da rede privada para a internet, ele tem seu endereço de 
origem substituído pelo endereço do roteador: 
 
 
 
Na imagem acima, existem 20 equipamentos cujos endereços privados variam do 172.18.3.1 até 
172.18.3.20. No entanto, sempre que qualquer pacote sai dessa rede a partir de qualquer 
equipamento e acessa a internet, ele sai com um único endereço público: 200.24.5.8. Dados 
provenientes da internet para os equipamentos da rede interna sofrem o processo inverso – o 
endereço público é substituído pelo endereço privado específico da máquina destinatária. 
 
Professor, como ele sabe para qual máquina os dados devem ser enviados? Para tal, o NAT armazena 
uma tabela de tradução: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
28
80
 
 
A tabela de tradução apresenta duas colunas: o endereço privado e o endereço público. Quando um 
pacote de dados sai da rede interna para a rede pública (internet), o roteador armazena na tabela 
tanto o endereço de origem (privado) quanto o endereço de destino (público). Quando a máquina 
de destino envia uma resposta para a máquina da rede interna, o roteador consulta a tabela e 
descobre o endereço privado que deve receber os dados. 
 
Na imagem seguinte, um pacote de dados sai da rede interna com endereço privado de origem 
172.18.3.1 com destino a máquina da rede externa com endereço público de destino 25.8.2.10. 
Quando ele passa pelo roteador, o NAT armazena na tabela o endereço privado/interno e o 
endereço público/externo. Note também que ao passar pelo roteador, o endereço de origem muda 
de 172.18.3.1 para 200.24.5.8, porque esse é o endereço do roteador. 
 
 
 
Na volta, um pacote de dados cujo endereço público de origem é 25.8.2.10 tem como endereço de 
destino 200.24.5.8. Quando esse pacote chega ao roteador, o NAT consulta quem havia enviado 
dados para o endereço 25.8.2.10 e descobre que havia sido a máquina da rede interna cujo endereço 
privado era 172.18.3.1, logo ele substitui o endereço do roteador 200.24.5.8 por 172.18.3.1. Com 
isso, nós aumentamos absurdamente a quantidade de equipamentos sem esgotar os endereços.  
 
Professor, há uma maneira de descobrir meu IP público? Sim, basta acessar www.whatismyip.com. 
Vejam que esse site informa que meu IP público é: 189.6.109.248. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
29
80
 
 
Em suma: o NAT é responsável por traduzir endereços privados (que existem apenas dentro de 
redes internas) para endereços públicos (que existem na internet). 
 
b) IPv6 (Versão 6):  
 
O IPv4 foi implementado em 1983, quando a internet ainda estava engatinhando. Nenhum 
engenheiro de redes imaginou que teríamos em pouco tempo uma quantidade tão absurda de 
equipamentos no mundo acessando a internet. Nós estávamos avançando em máxima velocidade 
ao esgotamento total de endereços IP. Era evidente: endereços não são infinitos – eles são 
recursos escassos como qualquer outro... 
 
Conforme acabamos de ver, surgiram soluções de curto prazo para ajudar a resolver o problema de 
esgotamento de endereços (Ex: NAT). No entanto, a escassez de endereços não era o único 
problema! Havia outros, tais como a falta de tratamento específico para transmissão de áudio/vídeo 
em tempo real e a criptografia/autenticação de dados para algumas aplicações. Tudo isso serviu de 
motivação para a criação de uma nova versão do Protocolo IP: IPv6 (Versão 6). 
 
A nova versão possui 128 Bits, logo temos até 2¹²8 possíveis endereços ou 340 undecilhões de 
endereços ou 340.282.366.920.938.000.000.000.000.000. 000.000.000 de endereços!  
 
No IPv4, decidiu-se utilizar uma representação decimal de 32 bits para facilitar a configuração! 
Ainda que fizéssemos isso com o IPv6, teríamos uma quantidade imensa de números. Dessa forma, 
optou-se por utilizar uma representação com hexadecimal, que necessita de todos os números e 
mais algumas letras: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F. Dividem-se 128 Bits em 8 grupos de 16 
Bits (seção de 4 hexadecimais), separados por dois-pontos. 
 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
30
80
O IPv6 não possui o conceito de classes e nem endereço de broadcast. Além disso, como o 
endereço ainda fica grande com o hexadecimal, há algumas formas de abreviar: zeros não 
significativos de uma seção (quatro dígitos entre dois-pontos) podem ser omitidos, sendo que 
apenas os zeros não significativos podem ser omitidos e, não, os zeros significativos. Na tabela 
abaixo, temos um exemplo: 
 
ENDEREÇO ORIGINAL 
FDEC:0074:0000:0000:0000:B0FF:0000:FFF0 
ENDEREÇO ABREVIADO 
FDEC:74:0:0:0:B0FF:0:FFF0 
ENDEREÇO MAIS ABREVIADO 
FDEC:74::B0FF:0:FFF0 
 
Usando-se essa forma de abreviação, 0074 pode ser escrito como 74, 000F como F e 0000 como 0. 
Observe que se tivéssemos o número 3210, por exemplo, não poderia ser abreviado. Outras formas 
de abreviações são possíveis se existirem seções consecutivas formadas somente por zeros. 
Podemos eliminar todos os zeros e substituí-los por um dois-pontos duplo. Note que esse tipo 
de abreviação é permitido apenas uma vez por endereço (Ex: não pode 2001:C00::5400::9). 
 
Se existirem duas ocorrências de seções de zeros, apenas uma delas pode ser abreviada. A 
reexpansão do endereço abreviado é muito simples: devemos alinhar as partes não abreviadas e 
inserir zeros para obter o endereço original expandido. É interessante notar também que o IPv6 
permite também o endereçamento local, isto é, endereços usados em redes privadas. Por fim, o 
IPv6 não pode se comunicar diretamente com o IPv4, mas existem diversas estratégias indiretas. 
 
ENDEREÇO ORIGINAL 
2001:0C00:0000:0000:5400:0000:0000:0009 
ENDEREÇO ABREVIADO 
2001:C00:0:0:5400:0:0:9 
ENDEREÇO MAIS ABREVIADO 
2001:C00::5400:0:0:9 ou 2001:C00:0:0:5400::9 
 
NÃO PODE SER ABREVIADO 
2001:C00::5400::9 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
31
80
ICMP (Internet Control Message Protocol) 
INCIDÊNCIA EM PROVA: baixíssima 
 
Internet control message protocol (icmp) 
Protocolo da camada de rede responsável por enviar mensagens de erro e mensagens operacionais indicando, por 
exemplo, que um serviço não está disponível ou que um roteador ou host não pode ser alcançado. Ele Inclui tipos 
de mensagens como “destino inalcançável”, ”redirecionamento”, ”tempo excedido”, entre outros. Esse protocolo 
é amplamente utilizado para diagnóstico de rede e geração de erros, funcionando intimamente com o protocolo 
IP, para relatar erros e outras informações relevantes. 
 
Nós já sabemos que o protocolo IP fornece serviços não confiáveis de entrega de pacotes. Ele foi 
projetado dessa forma para utilizar os recursos da rede de forma mais eficiente, oferecendo serviços 
de entrega de melhor esforço que possibilitam encaminhar um pacote desde sua origem até seu 
destino ﬁnal. No entanto, ele apresenta duas deﬁciências: falta de controle de erros e falta de 
mecanismos de notificação de erros.  
 
Agora o que acontece quando algo dá errado na entrega de um pacote ao destinatário? E se um 
roteador não conseguir encontrar um caminho até o destino final? O que acontece se houver um 
problema nos cabos de Internet? Estes são alguns exemplos de situações nas quais ocorreram erros! 
O protocolo IP não apresenta mecanismos integrados para notificar erros ao remetente dos 
dados. E agora, o que fazer? 
 
 
 
O ICMP (Internet Control Message Protocol) foi desenvolvido para suprir essas deﬁciências – ele 
é um protocolo auxiliar do protocolo IP. Trata-se de um protocolo da camada de Internet/Rede da 
Arquitetura TCP/IP, sendo utilizado para comunicar a ocorrência de situações anormais na 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
32
80
transferência de um pacote, gerando relatórios de erros4 à fonte original e respondendo às 
consultas a respeito do estado das máquinas da rede e roteadores.  
 
Na imagem acima, eu executo o comando ping. Esse comando utiliza o protocolo ICMP para 
verificar a conexão com uma máquina qualquer. Nesse caso, eu tentei acessar o servidor do 
Estratégia Concursos em www.estrategiaconcursos.com.br. Notem que ele informa que foram 
enviados 4 pacotes para o servidor e 4 foram recebidos, logo não houve perda. Ocorreu tudo muito 
rápido (média de 171 milissegundos) e foi um sucesso. 
 
ARP (Address Resolution Protocol) 
INCIDÊNCIA EM PROVA: baixíssima 
 
Address resolution protocol (ARP) 
Protocolo da camada de rede utilizado para mapear Endereços IP para Endereços MAC em redes locais, sendo 
fundamental para o funcionamento de redes IPv4. Ele é responsável por enviar uma requisição na rede local para 
descobrir o Endereço MAC correspondente a um Endereço IP específico. Os dispositivos na rede respondem com 
seus endereços MAC se o endereço IP solicitado corresponder ao seu. 
 
Protocolo 
da 
Camada 
de 
Rede/Internet, ele é responsável 
por manter uma tabela de 
conversão de endereços lógicos 
em endereços físicos. Vocês 
devem se lembrar que endereço 
lógico é o endereço IP e endereço 
físico é o endereço MAC. Esse 
protocolo mantém uma tabela 
de 
mapeamento 
entre 
endereços IP (Camada de Rede) 
e endereços MAC (Camada de 
Enlace). Onde eu encontro essa 
tabela, professor?  
 
No prompt de comando do sistema operacional, se você digitar arp -a, você verá a tabela e todas as 
suas entradas, conforme imagem a seguir. Note que temos uma coluna com Endereço IP e outra 
com Endereço Físico. Existe também o Reverse ARP (RARP), que é responsável por fazer o 
sentido contrário, isto é, ele mapeia endereços MAC (Camada de Enlace) para endereços IP 
(Camada de Rede). Notem que o Endereço MAC tem formato XX-XX-XX-XX-XX-XX. 
 
Protocolos da Camada de Transporte 
 
 
4 Note que ele não é responsável por corrigir eventuais falhas, apenas comunicá-las por meio de relatórios. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
33
80
TCP (Transmission Control Protocol) 
INCIDÊNCIA EM PROVA: ALTA 
 
TRANSMISSION CONTROL PROTOCOL (TCP) 
Protocolo da camada de transporte, considerado confiável e orientado à conexão. Ele utiliza portas para 
estabelecer conexões, utiliza controle de fluxo para evitar congestionamento na rede, permite a transferência de 
dados bidirecional e confirma o recebimento de pacotes, retransmitindo os que não são confirmados. Além disso, 
ele garante que os pacotes cheguem na ordem correta e utiliza a soma de verificação para detectar erros nos dados 
recebidos. O TCP é amplamente utilizado em aplicações que requerem entrega garantida de dados, como 
navegadores web e e-mail. 
 
Nós já sabemos que o Protocolo IP é classificado como não-confiável porque não oferece garantias 
de entrega de pacotes, sequenciamento de pacotes ou proteção contra duplicatas. Para resolver 
esse problema de confiabilidade, nós temos um outro protocolo na camada de transporte 
chamado TCP (Transmission Control Protocol). Por meio dele, é possível superar as limitações do 
Protocolo IP e oferecer uma comunicação confiável. 
 
TCP: Funcionamento 
 
O Protocolo de Controle de Transmissão (TCP) é um protocolo confiável, pois garante que os 
dados serão entregues íntegros e em ordem. Logo, se eu quero garantir que meu pacote chegará 
ao seu destino final, eu devo usar tanto o IP (protocolo que vai levar o pacote por várias redes) 
quanto o TCP (que vai garantir a entrega do pacote). Para tal, encapsula-se o TCP dentro do pacote 
IP. Como é, Diego? Isso mesmo! O TCP vai dentro do IP controlando e monitorando tudo... 
 
O IP não estabelece um contato com o destino antes de enviar os pacotes, não é capaz de garantir 
a entrega dos dados, não é capaz de predizer quão congestionada estará uma rede e não é capaz 
controlar o fluxo de pacotes enviados para o destinatário. Já o TCP é um protocolo orientado à 
conexão e confiável que faz o controle de congestionamento/fluxo e ainda permite a 
comunicação fim-a-fim. Vamos entender isso melhor... 
 
TCP: Características 
 
a) Orientado a Conexões 
 
O TCP (Transmission Control Protocol) é um protocolo de comunicação de dados orientado a 
conexões. Antes de enviar dados, o TCP estabelece uma conexão virtual entre o remetente e o 
destinatário. Este processo assegura a preparação do destinatário para receber os dados e 
possibilita a confirmação de recebimento e a retransmissão de segmentos perdidos ou 
corrompidos. 
 
No TCP, a transmissão de dados é full-duplex, permitindo que ambos os lados transmitam e 
recebam dados simultaneamente. O estabelecimento da conexão no TCP envolve três etapas, 
conhecidas como Three-Way Handshake: (1) O remetente envia um segmento SYN para iniciar a 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
34
80
comunicação; (2) O destinatário responde com um segmento SYN/ACK; (3) O remetente envia um 
segmento ACK para confirmar. 
 
1. O remetente envia um segmento SYN para iniciar a comunicação. 
2. O destinatário responde com um segmento SYN/ACK. 
3. O remetente envia um segmento ACK para confirmar. 
 
Após essa sequência, a conexão está estabelecida, permitindo a 
troca de segmentos de dados. O TCP garante a entrega de dados e 
a integridade da informação, sendo mais lento, porém mais 
confiável que o UDP (User Datagram Protocol), que não estabelece 
conexão e não garante a entrega dos dados. 
 
b) Conexão Fim-a-Fim 
 
Imaginem que na rota entre duas grandes capitais brasileiras existam dezenas de cidades. Nós 
podemos dizer que entre esses dois pontos existem milhares de caminhos possíveis. O TCP é capaz 
de criar uma conexão entre dois processos em uma máquina – fim-a-fim – ignorando quaisquer nós 
intermediários que existam entre emissor e destinatário da informação e focando-se apenas nos 
processos finais. O IP é um protocolo host-a-host, já o TCP é um protocolo fim-a-fim. 
 
Lembrando que um processo se refere a um programa ou aplicação em execução em um 
computador que usa a rede para se comunicar. A natureza fim-a-fim (também chamada de 
processo a processo) do TCP assegura uma comunicação confiável e ordenada diretamente entre 
processos específicos, independentemente das características físicas e das rotas da rede 
subjacente. Entendido? 
 
c) Controle de Fluxo 
 
Imaginem que após vários dias enviando pacotes para o meu pai, eu passo na frente da casa dele e 
vejo uma montanha pacotes fora de casa porque ele ainda não conseguiu abrir espaço para 
armazenar os pacotes. Eu posso reduzir meu fluxo e enviar apenas a quantidade que ele consegue 
absorver de forma que ele não fique sobrecarregado. O controle de fluxo previne o receptor de 
ficar sobrecarregado por meio de um mecanismo chamado Janela Deslizante.  
 
d) Controle de Congestionamento 
 
Toda vez que meu pai recebe meus pacotes, ele me avisa que os recebeu. Se eu percebo que ele 
está demorando demais para receber os pacotes que eu estou enviando, eu posso concluir – por 
exemplo – que o tráfego está intenso e que o caminhão de entrega está em um congestionamento. 
E, assim, posso reduzir a quantidade de pacotes enviados. O controle de congestionamento 
previne que a rede fique sobrecarregada. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
35
80
TCP: Portas 
 
Portas, em protocolos de rede, funcionam como identificadores para processos específicos em 
um computador. Assim como uma casa tem um único endereço, mas vários quartos com diferentes 
portas, um computador tem um único endereço IP, mas múltiplos processos rodando, cada um 
acessível por uma porta distinta. Quando um pacote de dados chega ao computador, o número da 
porta é usado para identificar o processo destinatário correto.  
 
Na camada de enlace de dados, o Endereço MAC é utilizado; na camada de rede, usa-se o 
Endereço IP; e na camada de transporte, emprega-se o Número da Porta. As portas variam de 0 
a 65535, permitindo até 65536 serviços diferentes ativos simultaneamente em um servidor com um 
único Endereço IP. Por exemplo, o protocolo HTTP padrão da web utiliza a porta 80, conforme 
definido pela IANA (Internet Assigned Number Authority).  
 
Tentar acessar um serviço na porta errada, como usar a porta 21 (geralmente designada para FTP) 
para acessar um site HTTP, resultará em um erro, pois indica que o pacote de dados não está 
destinado ao processo correto. Logo, o número da porta é essencial para garantir que os dados 
enviados pela rede cheguem ao processo correto no computador de destino. Isso é crucial para 
a comunicação eficiente entre processos em diferentes máquinas na rede5. 
 
PROTOCOLO (CAMADA DE APLICAÇÃO) 
PROTOCOLO (CAMADA DE TRANSPORTE) 
NÚMERO DA PORTA 
HTTP 
TCP 
80 
HTTPS 
TCP 
443 
POP3 
TCP 
110 
SMTP 
TCP 
25/5876 
IMAP4 
TCP 
143 
FTP 
TCP 
20/21 
TELNET 
TCP 
23 
SSH 
TCP 
22 
DNS 
TCP/UDP 
53 
DHCP 
UDP 
67/68 
IRC 
TCP 
194 
EM VERMELHO, OS PROTOCOLOS CUJO NÚMERO DE PORTA MAIS CAEM EM PROVA! 
 
 
Galera, não precisa se desesperar para decorar todas essas portas! Eu coloquei em vermelho as 
principais, mas mesmo essas não caem com bastante frequência, logo analisem o custo-benefício 
de memorizar. Por fim, é importante falar sobre Data Protocol Unit (DPU) ou Unidade de Dados 
 
5 A combinação do Protocolo + Endereço IP + Número da Porta é também chamada de Socket. 
6 Via de regra, o padrão respaldado pela RFC do SMTP é Porta 25. Excepcionalmente, o Brasil adotou a porta 587 para evitar SPAM. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
36
80
de Protocolos. Cada camada possui um nome para sua unidade, um tipo de comunicação e um tipo 
de endereço (sendo que pacote é um termo genérico para qualquer unidade): 
 
CAMADas 
Unidade de dados padrão 
Tipo de comunicação 
Tipo de endereço 
FÍSICA 
Bits 
Ponto-a-Ponto 
- 
ENLACE 
Quadros/Frames 
Ponto-a-Ponto 
Endereço Físico (MAC) 
REDE 
Datagramas 
Host-a-Host 
Endereço Lógico (IP) 
TRANSPOrTE 
Segmentos7 
Fim-a-Fim 
Endereço de Portas 
SESSÃO 
Mensagens 
Fim-a-Fim 
Endereços Específicos 
(URL) 
APRESENTAÇÃO 
APLICAÇÃO 
 
UDP (User Datagram Protocol) 
INCIDÊNCIA EM PROVA: baixíssima 
 
User datagram protocol (udp) 
Protocolo da camada de transporte, considerado sem conexão e utiliza portas para comunicação de forma similar 
ao TCP. Ele não possui controle de fluxo e permite a transferência de dados rápida, mas sem garantias de entrega, 
ordem ou integridade. Esse protocolo é considerado não confiável porque não é capaz de confirmar o recebimento 
de pacotes e não retransmite os pacotes perdidos. Ele também não reordena pacotes e realiza apenas verificações 
básicas de erros nos dados recebidos (mas não os corrige). Por fim, ele não requer estabelecimento de conexão 
antes da transferência de dados, sendo ideal para aplicações que requerem transmissão rápida, como streaming 
de vídeo e jogos online. 
 
O UDP (User Datagram Protocol) é um protocolo da Camada de Transporte que oferece um 
serviço de entrega de dados sem conexão e não confiável, com baixo overhead. Diferente do 
TCP, o UDP não implementa controle de fluxo ou de congestionamento, nem garante a entrega dos 
dados. Dentre as vantagens do UDP incluem sua simplicidade e eficiência para enviar mensagens 
pequenas sem se preocupar com a confiabilidade.  
 
É ideal para serviços em tempo real como chamadas de áudio ou vídeo, onde perdas ocasionais 
de pacotes são aceitáveis e não prejudicam significativamente a experiência do usuário. Tentar 
reenviar pacotes perdidos em tais contextos seria inútil, pois atrasaria a entrega, afetando a fluidez 
da comunicação. O TCP, por outro lado, é orientado à conexão e garante a entrega confiável de 
dados através de controle de fluxo, congestionamento e retransmissão de dados perdidos.  
 
Oferece serviços ponto-a-ponto e unicast, com transferência de dados full-duplex, adequados para 
situações que exigem confiabilidade e integridade de dados. O UDP, não sendo orientado à 
conexão, permite maior flexibilidade, podendo operar em modos ponto-a-ponto ou ponto-
 
7 UDP, na verdade, é orientado a datagramas. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
37
80
multiponto e suportando unicast, multicast e broadcast. Assim, pode transferir dados de um 
remetente para um, alguns ou todos os destinatários, também em full-duplex. 
 
As diferenças entre TCP e UDP são consequências de suas respectivas orientações à conexão e à 
não-conexão, com cada protocolo sendo mais adequado para diferentes necessidades: 
 
TCP 
udp 
É comparativamente mais lento que o UDP 
É comparativamente mais rápido que o TCP 
Entregas confiáveis 
Entregas não confiáveis (melhor esforço) 
Orientado à conexão 
Não orientado à conexão 
Dados perdidos são retransmitidos 
Dados perdidos não são retransmitidos. 
Realiza controle de fluxo e congestionamento  Não realiza controle de fluxo e congestionamento 
Tolera atrasos, mas não tolera perdas 
Tolera perdas, mas não tolera atrasos  
Envia dados em unicast 
Envia dados em unicast, multicast ou broadcast 
Oferece conexão ponto a ponto 
Oferece conexão ponto a ponto ou ponto-multiponto 
Bastante utilizada em e-mail, navegação, etc. 
Bastante utilizada em VoIP, streaming, etc. 
 
Protocolos da Camada de Aplicação 
 
Protocolos de E-Mail 
INCIDÊNCIA EM PROVA: ALTA 
 
Correio Eletrônico (E-Mail) é uma forma de comunicação digital que permite aos usuários enviar 
e receber mensagens através de redes eletrônicas. O serviço de correio eletrônico é baseado em 
uma arquitetura cliente/servidor, isto é, uma arquitetura composta de máquinas responsáveis por 
oferecer serviços (por essa razão, é chamada de servidor) e de máquinas responsáveis por consumir 
serviços (por essa razão, é chamada de cliente).  
 
No decorrer desse tema, vamos ver diversos termos que vocês estão acostumados, mas que podem 
gerar dúvidas. Dessa forma, vamos parar um pouquinho para detalhá-los: 
 
Cliente de e-mail Trata-se de uma aplicação instalada em uma máquina local que permite enviar/receber 
e-mails (Ex: Mozilla Thunderbird, Microsoft Outlook, etc); 
Servidor de e-mail Trata-se de uma máquina especializada que recebe e-mails de um cliente de e-mail ou de 
um webmail, e os envia para o servidor de e-mail de destino; 
Provedor de e-mail Trata-se de uma empresa ou serviço que hospeda e disponibiliza serviços de e-mail para 
outras empresas ou usuários finais (Ex: Gmail, Outlook, Yahoo, Uol, etc); 
webmail Trata-se de uma aplicação hospedada em um servidor remoto que permite 
enviar/receber e-mails (Ex: Outlook.com, Gmail.com, Yahoo.com, Uol.com, etc). 
 
Os principais protocolos de correio eletrônico são: SMTP, POP e IMAP. Vamos vê-los 
resumidamente na tabela a seguir e depois entraremos nos detalhes de cada um: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
38
80
PROTOCOLOS 
DE E-MAIL 
DESCRIÇÃO 
SMTP 
Protocolo utilizado basicamente para enviar e-mails. Ele transfere mensagens de e-mail de um 
cliente para um servidor ou entre servidores. Funciona bem para a entrega de mensagens, mas não 
para recuperá-las. 
 
POP 
Protocolo projetado para recuperar e-mails de um servidor. Quando você o utiliza, os e-mails são 
baixados para o seu dispositivo e geralmente são excluídos do servidor. Isso é útil para acessar e-
mails offline, mas pode ser limitante se você usar vários dispositivos, pois as mensagens estão 
disponíveis apenas no dispositivo onde foram baixadas inicialmente. 
IMAP 
Também usado para recuperar e-mails de um servidor, mas – diferentemente do anterior – ele 
mantém as mensagens no servidor. Isso permite que você acesse seus e-mails de vários dispositivos, 
mantendo tudo sincronizado. As mudanças feitas em um dispositivo (como ler ou excluir uma 
mensagem) são refletidas em todos os outros dispositivos. 
 
SMTP 
POP3 
IMAP 
ENVIAr 
Receber e COPIAr 
Receber e ACESSAr 
 
E-Mail: SMTP 
 
Simple mail transfer protocol (SMTP) 
Protocolo da camada de aplicação responsável pelo envio de e-mails de um cliente para um servidor ou entre 
servidores de e-mail. Ele é bastante utilizado por clientes de e-mail e servidores de e-mail para a transmissão de 
mensagens de correio eletrônico, funcionando por meio de uma arquitetura cliente/servidor. Além disso, é 
interoperável com outros protocolos de e-mail (Ex: POP3 e IMAP) para uma funcionalidade de e-mail completa. 
 
O SMTP é um protocolo da camada de aplicação utilizado para enviar mensagens de e-mail de 
um cliente de e-mail para um servidor de e-mail e entre servidores de e-mail em uma rede de 
computadores. Quando um usuário envia um e-mail, o SMTP cuida de encaminhar essa mensagem 
do servidor de e-mail do remetente para o servidor de e-mail do destinatário. O SMTP é eficaz para 
enviar mensagens, mas não para recuperá-las ou armazená-las. 
 
S 
M 
T 
P 
SUA 
MENSAGEM 
TÁ  
PARTINDO 
 
Ele também é utilizado para a comunicação entre servidores de e-mail, permitindo que eles passem 
e-mails de um para o outro até que a mensagem alcance o servidor de e-mail do destinatário final 
(veremos esse caso específico mais à frente). O SMTP – em seu uso moderno – inclui mecanismos 
de autenticação para aumentar a segurança, ajudando a prevenir o abuso do sistema de e-mail, 
como o envio de spam. Vejamos alguns cenários de utilização: 
 
a) Cenário 1: troca de e-mails em um mesmo provedor 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
39
80
 
Diego compõe uma mensagem no Gmail e a envia para Renato. O 
SMTP é utilizado para enviar esta mensagem do cliente de e-mail 
de Diego para o servidor de e-mail do Gmail. Uma vez que o 
servidor do Gmail recebe a mensagem, ele identifica que o 
destinatário, Renato, também está no Gmail. O servidor então 
processa a mensagem internamente, sem a necessidade de enviar 
a mensagem para outro servidor. A mensagem é colocada na caixa 
postal de Renato no Gmail, que pode acessá-la posteriormente. 
 
b) Cenário 2: troca de e-mails em provedores diferentes 
 
Diego escreve e envia um e-mail para Renato por meio do Gmail. O SMTP transfere a mensagem 
para o servidor de e-mail do Gmail. Esse servidor também utiliza o SMTP para enviar a mensagem 
para o servidor de e-mail do Yahoo, que é o provedor de Renato. Este processo pode envolver a 
mensagem passando por vários servidores e redes de computadores na internet. Uma vez que o 
servidor do Yahoo receba a mensagem, ele a processa e entrega na caixa de Renato no Yahoo. 
 
 
 
 
 
Vocês se lembram que eu falei que o SMTP também é utilizado para comunicação entre servidores? 
Bem, isso caiu apenas uma vez em prova, mas foi uma polêmica imensa! Nós já vimos 
exaustivamente que o SMTP é o principal protocolo de transferência de correio eletrônico através 
da rede. Eu menti? Não! No entanto, ele também pode ser utilizado para receber e-mail em uma 
única situação. Para entender melhor, vamos analisar a imagem seguinte:  
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
40
80
 
 
Percebam que o remetente utiliza o protocolo SMTP para enviar uma mensagem de correio 
eletrônico. No entanto, notem que na comunicação entre o servidor de correio eletrônico do 
remetente e do destinatário também é utilizado o SMTP. Logo, nesse caso específico de 
comunicação entre servidores, ele é utilizado tanto para envio quanto para recebimento de correio 
eletrônico. Não é o padrão, é apenas nesse caso! Bacana? 
 
E-Mail: POP 
 
Post office protocol (pop) 
Protocolo da camada de aplicação responsável por recuperar e-mails de um servidor de e-mail. Em regra, ele baixa 
os e-mails do servidor para o cliente local e os deleta do servidor, mas há outros modos de funcionamento. O POP3 
suporta criptografia via SSL/TLS e autenticação através de usuário/senha, além de permitir a leitura de e-mails 
offline e controle limitado sobre as mensagens no servidor. Por outro lado, ele não sincroniza o estado da 
mensagem entre múltiplos dispositivos (lido/não lido, marcado/não marcado). Ele é menos flexível que IMAP, 
sendo ideal para usuários que acessam e-mail de um único dispositivo. 
 
O POP3 é um protocolo da camada de aplicação criado como uma forma simplificada para fazer 
o download de mensagens da caixa postal de um servidor de correio eletrônico para a máquina 
do usuário. Por meio desse protocolo, Renato poderá acessar a caixa postal no servidor de correio 
remoto e baixar seus e-mails para a sua máquina local. Galera, o POP já foi mais popular (piada 
infame), mas é bem menos utilizado hoje em dia. Por quê, professor? 
 
Antigamente, o espaço de armazenamento dos servidores de correio eletrônico era bastante 
pequeno. Hoje em dia, qualquer provedor oferece uma conta gratuita com 15Gb de espaço de 
armazenamento. Há muito tempo, nem se você pagasse, você teria tanto espaço assim disponível. 
Era comum, inclusive, que os usuários tivessem que acessar seus e-mails todos os dias para evitar 
que a caixa de e-mails ficasse lotada e futuros e-mails não fossem recebidos. 
 
O POP era extremamente útil porque ele permitia apagar a mensagem do servidor de correio 
eletrônico após a leitura pelo destinatário e armazená-la em sua máquina local. Dessa forma, o 
espaço de armazenamento era liberado para a chegada de novos e-mails no servidor. Na verdade, 
esse é o modo padrão de funcionamento desse protocolo, mas possui duas maneiras distintas de 
trabalhar com correio eletrônico. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
41
80
No modo Delete, esse protocolo remove as mensagens da caixa postal após a realização do 
download para a máquina local. Esse modo tem como vantagens poder organizar as mensagens 
recebidas e abrir espaço no servidor para o recebimento de novas mensagens. No entanto, o 
gerenciamento de e-mails se tornava complexo se o usuário utilizasse mais de um computador – 
além do risco de sua máquina ser infectada por um malware ou simplesmente ser furtada. 
 
No modo Keep, esse protocolo permanece realizando o download dos e-mails para a máquina 
local, porém ele não os remove da caixa postal. Esse modo tem como vantagens manter um 
gerenciamento centralizado dos e-mails e não correr o risco de perda de dados porque os e-mails 
eram mantidos no servidor. No entanto, o armazenamento de e-mails poderia ultrapassar o espaço 
de armazenamento, resultando em um descarte de novos e-mails recebidos. 
 
Esse protocolo era indicado para as pessoas que não possuíam acesso fácil à Internet, para poderem 
consultar os e-mails recebidos de forma offline. Lembrem-se que – até um tempo atrás – o acesso 
à Internet era algo bastante raro e muitas pessoas não podiam ficar sem acesso aos seus e-mails 
quando não estivessem conectadas à Internet. Galera, a verdade é que o tempo foi passando e o 
POP3 foi se mostrando ineficiente em algumas situações.  
 
Ele não permite ao usuário organizar mensagens ou criar pastas no servidor; não permite que o 
usuário verifique parte do conteúdo da mensagem antes de fazer o download; possui problemas 
quando configurado em mais de um computador; etc. Já o IMAP permite que você acesse todos 
os seus correios eletrônicos a qualquer momento. Além disso, ele traz diversas funções 
adicionais. Vejamos... 
 
E-Mail: IMAP 
 
INTERNET MESSAGE ACCESS PROTOCOL (IMAP) 
Protocolo da camada de aplicação responsável pelo acesso, gerenciamento e sincronização de e-mails 
armazenados em um servidor de e-mail. Ele permite ao usuário visualizar e manipular mensagens diretamente no 
servidor, além de sincronizar o estado das mensagens (lido/não lido, marcado/não marcado) entre múltiplos 
dispositivos. Ele suporta criptografia via SSL/TLS e autenticação através de usuário e senha. Esse protocolo é mais 
flexível que o POP3, sendo ideal para usuários que acessam e-mail de múltiplos dispositivos. As mensagens 
geralmente permanecem no servidor, permitindo acesso a partir de qualquer dispositivo. 
 
Um usuário pode verificar o cabeçalho de um e-mail antes de baixá-lo; pode procurar pelo conteúdo 
de um e-mail antes de baixá-lo; pode baixar parcialmente um e-mail – isso é útil se a largura de 
banda for limitada e o e-mail tiver conteúdos com grandes exigências de largura de banda; um 
usuário pode criar, eliminar ou renomear caixas de correio no servidor de e-mail; e pode criar uma 
hierarquia de caixas de correio em pastas para armazenamento de e-mails. 
 
O IMAP é equivocadamente associado a webmails pelo caráter de repositório central que esses 
serviços oferecem ao permitir amplo acesso a e-mails (mobilidade). No entanto, navegadores (e 
consequentemente webmails) não suportam IMAP – eles utilizam o HTTP/HTTPS! O IMAP possui 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
42
80
uma versão mais segura chamada IMAPS (IMAP Secure). Nesse caso, ele utilizará a Porta 993 
e, não, 143. Vamos ver uma tabela comparativa: 
 
Pop3 
Imap 
Post Office Protocol (Version 3) 
Internet Message Access Protocol 
Não recomendado para acesso em múltiplos dispositivos 
Recomendado para acesso em múltiplos dispositivos 
Não permite criar e organizar pastas no servidor 
Permite criar e organizar pastas no servidor 
Não permite verificar o cabeçalho antes de baixá-lo 
Permite verificar o cabeçalho antes de baixá-lo 
Modificações em um dispositivo não refletidas em outros 
Modificações em um dispositivo refletidas em outros 
Não permite baixar parcialmente um e-mail 
Permite baixar parcialmente um e-mail 
Por padrão, mensagens de e-mail são lidas offline 
Por padrão, mensagens de e-mail são lidas online 
Não permite múltiplas caixas postais 
Permite múltiplas caixas postais 
Porta 110 
Porta 143  
 
E-Mail: WebMail 
 
webmail 
Um webmail é um serviço de e-mail que pode ser acessado e usado através de um navegador da web, em vez de 
um cliente de e-mail dedicado. Ele funciona como uma interface baseada na web para enviar, receber e gerenciar 
mensagens de e-mail (Ex: Gmail, Yahoo, Outlook, Hotmail, etc). 
 
Por fim, podemos utilizar também um Webmail! O Webmail é um sistema web que faz a interface 
com um serviço de e-mail hospedado em um Servidor Web! Armaria, professor... entendi foi nada! 
Galera, quando vocês acessam a página do Estratégia Concursos, vocês estão acessando – por meio 
de um browser – uma página que está hospedada (armazenada) em uma máquina especializada 
chamada Servidor Web. Ocorre de maneira semelhante com e-mail... 
 
Quando vocês acessam – por meio de um navegador – um serviço de e-mail, temos um... webmail! 
É como se o cliente de e-mail apresentado no esquema anterior estivesse hospedado em um 
servidor web e você utilizasse um browser para acessá-lo. Logo, a comunicação entre a máquina 
do remetente e o servidor web de origem se dá por meio do HTTP! Ao final, para recuperar o e-mail 
do servidor web para a máquina do destinatário também se utiliza o HTTP. 
 
 
 
Algumas questões não primam pelo rigor técnico e acabam omitindo o servidor web e tratando 
ambos – servidor web e servidor de correio eletrônico – apenas como servidor de correio eletrônico. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
43
80
E-Mail: MIME 
 
Multipurpose Internet Mail Extensions (mime) 
Trata-se de um padrão importante no contexto do correio eletrônico. Ele expande as capacidades do e-mail 
original, que era limitado a textos em formato ASCII8, permitindo a inclusão de uma variedade de tipos de 
conteúdo. Ele é essencial para a funcionalidade moderna do e-mail, permitindo uma rica variedade de conteúdos 
e formatos de arquivo a serem compartilhados por meio deste meio de comunicação. 
 
Para finalizar, vamos falar rapidamente sobre MIME (Multipurpose Internet Mail Extensions)! O 
correio eletrônico possui uma estrutura simples, porém isso tem um preço. Ele, por exemplo, possui 
certas limitações no formato de envio de algumas mensagens. Originalmente, ele não pode ser 
utilizado para criar mensagens em idiomas que não são suportados por caracteres ASCII de 7 bits 
(como francês, alemão, hebraico, russo, chinês e japonês).  
 
Da mesma forma, ele não pode ser usado para transmitir arquivos binários ou dados no formato de 
fotos, áudio ou vídeo. Professor, mas eu já enviei e-mail com todos esses formatos! Se você já fez isso, 
agradeça ao MIME! Ele é um protocolo complementar ao SMTP que possibilita que dados em 
diferentes formatos sejam enviados por e-mail. Podemos imaginar o MIME como um conjunto de 
funções de software que convertem dados não-ASCII (fluxos de bits) em dados ASCII e vice-versa. 
 
Em outras palavras, ele é um recurso, formato ou extensão utilizado para formatação de 
mensagens que facilita o envio de mensagens e permite o envio de arquivos de diferentes tipos 
(imagem, áudio, vídeo, documento, executável, etc) em um e-mail. Ele também possui uma 
versão mais segura – que permite a criptografia e assinatura dos dados – chamada S/MIME. Isso não 
costuma cair com frequência, mas é bem simples de entender... 
 
Protocolo DHCP 
INCIDÊNCIA EM PROVA: baixa 
 
Dynamic host configuration protocol (dhcp) 
Protocolo da camada de aplicação responsável por atribuir automaticamente endereços IP e outras configurações 
de rede a dispositivos em uma rede. Ele funciona com um modelo cliente-servidor em que o Servidor DHCP atribui 
IPs dinamicamente aos clientes da rede e suporta alocação dinâmica, alocação automática e alocação estática de 
endereços IP. O DHCP simplifica o gerenciamento de endereços IP (especialmente em redes grandes), sendo 
amplamente utilizado em redes domésticas, corporativas e públicas para simplificar a configuração de rede. 
 
O DHCP (Dynamic Host Configuration Protocol) é um protocolo da camada de aplicação que 
facilita a alocação de endereços IP (também conhecidos como endereços lógicos). Diferente dos 
endereços físicos (Endereço MAC), os endereços IP podem mudar sem problemas. Eles são 
 
8 ASCII, sigla para "American Standard Code for Information Interchange" (Código Padrão Americano para o Intercâmbio de Informação), é um 
padrão de codificação de caracteres usado para a representação de texto em computadores e outros dispositivos eletrônicos. Desenvolvido na década 
de 1960, o ASCII originalmente representava caracteres usando 7 bits, o que permitia 128 caracteres diferentes, incluindo letras do alfabeto inglês 
(maiúsculas e minúsculas), dígitos numéricos, sinais de pontuação e alguns caracteres de controle. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
44
80
fundamentais para cada dispositivo na internet, não podendo ser escolhidos aleatoriamente, pois 
muitos já estão em uso ou reservados.  
 
Os provedores de internet (Ex: Net, Claro, Vivo) fornecem esses endereços, que podem ser estáticos 
ou dinâmicos. O endereço IP estático é permanente, alterado apenas manualmente pelo provedor 
ou pelo administrador de rede. Comum em servidores, espera-se que esse endereço não mude 
frequentemente. Por outro lado, o endereço IP dinâmico, mais comum em usuários domésticos, 
é atribuído temporariamente durante a conexão à internet e pode mudar a cada nova conexão.  
 
Este é configurado automaticamente pelo protocolo DHCP, sendo uma solução ideal para uso 
doméstico por não requerer equipamentos avançados ou conhecimentos técnicos específicos para 
configuração. A configuração manual de uma rede, realizada computador por computador, 
pode ser trabalhosa, especialmente em redes grandes. Com o uso do Servidor DHCP, essa 
configuração é automatizada.  
 
O servidor DHCP não apenas encontra um endereço IP para cada máquina na rede, mas 
também recupera informações como a máscara de sub-rede e o endereço do servidor DNS. Isso 
contrasta com o método antigo, onde era necessário contactar o provedor para obter esses dados 
para cada conexão à internet. O servidor DHCP simplifica este processo, configurando 
automaticamente a rede e alocando endereços IP dinâmicos.  
 
Ao final da conexão, o endereço é liberado, disponibilizando-o para outros usuários. Logo, o DHCP 
é crucial para a alocação dinâmica e automática de endereços IP em redes modernas. 
 
Protocolo DNS 
INCIDÊNCIA EM PROVA: Altíssima 
 
Domain Name System (DNS) 
Protocolo da camada de aplicação responsável por traduzir (também chamado de resolver) nomes de domínio 
legíveis por humanos para Endereços IP. Ele funciona em um modelo de consulta e resposta, sendo estruturado de 
maneira hierárquica com vários níveis de Servidores DNS. Esse protocolo armazena as respostas recentes para 
reduzir o tempo de resposta e o tráfego na rede, incluindo extensões de segurança para proteger contra ataques. 
O DNS é essencial para a navegação na internet, permitindo o uso de URLs em vez de endereços IP numéricos. 
 
D 
N 
S 
DÁ 
NOME AO 
SITE 
 
DNS: Funcionamento 
 
Nós já sabemos que cada página web é armazenada em um servidor, que possui um endereço IP 
único. De forma análoga, os computadores na internet são identificados por endereços IP, como o 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
45
80
192.168.10.15. Para facilitar a memorização, o Domain Name System (DNS) foi o sistema 
desenvolvido para converter endereços lógicos (IP) em nomes mais amigáveis e vice-versa (Ex: 
o endereço IP 216.58.211.14 leva à página do Google).  
 
O DNS funciona como uma agenda telefônica da internet, transformando endereços numéricos em 
nomes compreensíveis (Ex: www.google.com), mais fáceis de recordar do que sequências 
numéricas. Dessa forma, o DNS facilita a navegação, traduzindo nomes de domínio em endereços 
IP e vice-versa, semelhante à como uma agenda telefônica conecta nomes de contatos a seus 
respectivos números de telefone. A tabela mostra a correspondência entre URL e Endereço IP: 
 
DNS (DOMAIN NAME SYSTEM) 
URL 
IP 
www.google.com 
216.58.211.14 
 
DNS: URL 
 
Antes de prosseguir, vamos entender o que é uma URL (Uniform Resouce Locator)! Trata-se do 
endereço de um recurso em uma rede de computadores. Todo recurso computacional (página 
web, arquivo, servidor, impressora, computador, documento, entre outros) deve possuir um 
endereço para que possa ser localizado. Ela oferece uma maneira uniforme e padronizada de 
localizar recursos na rede. Uma URL é formada pela seguinte estrutura: 
 
URL - Sintaxe abstrata 
protocolo://ip-ou-domínio:porta/caminho/recurso 
 
Componentes DESCRIÇÃO 
Protocolo Também chamado de esquema, trata-se do protocolo utilizado para acessar um recurso. 
ip Número de IP do Servidor (Host) que hospeda um recurso. 
DOmínio Nome do Domínio do Servidor (Host) que hospeda um recurso. 
PORTA Ponto lógico que permite criar uma conexão em um processo. 
Caminho Estrutura de diretórios dentro do servidor que armazena um recurso. 
recurso Componente físico ou lógico disponível em um sistema computacional. 
 
A URL é o endereço virtual de um recurso em uma rede, logo ela está informando que para 
encontrar o recurso desejado, você deve utilizar um determinado protocolo, informar o endereço 
lógico ou nome do domínio para encontrar o servidor, depois procurar em uma porta específica, 
seguir um caminho nos diretórios no disco que armazena esse recurso até finalmente encontrá-lo. 
Então vamos ver um exemplo: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
46
80
https://www.estrategiaconcursos.com.br/app/dashboard/cursos/aulas/aula1.pdf 
 
Componentes DESCRIÇÃO 
Protocolo https 
domínio estrategiaconcursos.com.br (www é apenas um prefixo que pode ser omitido) 
PORTA 443 (apesar de ter sido omitida, essa é a porta padrão desse protocolo) 
Caminho /app/dashboard/cursos/aulas 
recurso Aula1.pdf 
 
Existe uma confusão entre URL e Domínio! Observem que – se eu modifico o nome do recurso da 
URL anterior para “Aula2.pdf”, eu terei uma URL diferente, no entanto o domínio permanecerá o 
mesmo! Pessoal, nós vimos na página anterior a sintaxe abstrata de uma URL! Por que dizemos que 
se trata de uma sintaxe abstrata? Porque a sintaxe completa pode conter vários outros 
componentes como apresentado abaixo: 
  
URL – sintaxe completa 
protocolo://nome-de-usuário@ip-ou-domínio:porta/caminho/recurso?query#fragmento 
 
Dos componentes apresentados, apenas dois são obrigatórios: Protocolo e Domínio. Porta, 
Caminho e Recurso são bastante comuns, mas opcionais. Já na sintaxe completa, é possível ver mais 
três componentes opcionais bem mais raros: Query (ou QueryString), Fragmento e Nome de 
Usuário. O primeiro é usado para passar parâmetros de pesquisa; o segundo para ir diretamente 
para uma parte específica de uma página web; e o terceiro para autenticação de usuários. 
 
Componentes extras DESCRIÇÃO 
Query / queryString Utilizado para passar parâmetros adicionais para o servidor em formato chave-valor. 
fragmento Utilizado para navegar diretamente para uma seção específica de uma página da web. 
Nome de usuário Utilizado em contextos em que é necessária a autenticação para acessar os recursos. 
 
A Query String permite passar parâmetros adicionais para o servidor. Isso inclui dados de 
formulários, filtros para pesquisas, informações de paginação, ou qualquer outro dado que precise 
influenciar a resposta do servidor. Ela é iniciada por um ponto de interrogação (?) e é seguida por 
uma ou mais pares de chave-valor, que são separados por e comercial (&)9. Cada par chave-valor é 
composto pela chave, um sinal de igual (=), e o valor associado. 
 
A Query String permite passar parâmetros adicionais para o servidor. Isso inclui dados de 
formulários, filtros para pesquisas, informações de paginação, ou qualquer outro dado que precise 
 
9 Note que a URL não permite acentuação gráfica e possui alguns caracteres reservados (Ex: ?, /, $, :, etc). A codificação de URL converte os 
caracteres reservados em um formato inteligível por navegadores (Ex: espaço em branco é codificado como “%20”). 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
47
80
influenciar a resposta do servidor. Ela é iniciada por um ponto de interrogação (?) e é seguida por 
uma ou mais pares de chave-valor, que são separados por e comercial (&)10. Cada par chave-valor é 
composto pela chave, um sinal de igual (=), e o valor associado. 
 
Há um parâmetro muito comum chamado utm_source, que é um identificador utilizado em 
campanhas de marketing digital para indicar a origem de tráfego, isto é, de onde veio o visitante 
que acessou aquela página. UTM (Urching Tracking Module) é um padrão criado pelo Google para 
rastrear campanhas no Google Analytics. Já o parâmetro utm_source normalmente informa qual 
foi a plataforma, site ou ferramenta que trouxe o usuário até o link. Há outros parâmetros de 
rastreamento, tais como:  
 
▪ utm_medium indica o meio da campanha, como o tipo de tráfego (Ex: utm_medium=cpc indica 
que o acesso veio de anúncio pago);  
 
▪ utm_campaign indica o nome da campanha de marketing, utilizado para diferenciar promoções 
ou iniciativas (Ex: utm_campaign=blackfriday);  
 
▪ utm_term geralmente é usado em campanhas pagas para indicar palavras-chave ou termos de 
busca (Ex: utm_term=tenis+adidas);  
 
▪ utm_content serve para diferenciar versões de anúncios ou links em uma mesma campanha (Ex: 
utm_content=banner1) identifica que o clique veio do primeiro banner da campanha. 
 
Já o fragmento (ou âncora) é uma parte da URL que segue o caractere cerquilha (#) e é usada 
para identificar e direcionar para uma parte específica dentro de um documento. O fragmento 
não é enviado ao servidor durante uma solicitação HTTP; ele é processado exclusivamente pelo 
navegador. Por exemplo, em uma página com múltiplos títulos ou seções, é possível acessar 
diretamente uma seção específica.  
 
DNS: Esquemas 
 
Algumas observações importantes: os principais componentes em uma URL são o Protocolo e o 
Domínio – todos os outros costumam ser omitidos com alguma frequência. Além disso, os 
protocolos ou esquemas mais comuns que são suportados em uma URL são: HTTP, HTTPS, FTP, 
FILE e MAILTO. Os três primeiros protocolos ainda serão vistos nessa aula, já os dois últimos 
esquemas nós veremos agora... 
 
Esquema 
descrição 
 
10 Note que a URL não permite acentuação gráfica e possui alguns caracteres reservados (Ex: ?, /, $, :, etc). A codificação de URL converte os 
caracteres reservados em um formato inteligível por navegadores (Ex: espaço em branco é codificado como “%20”). 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
48
80
File 
O esquema FILE é usado para indicar recursos locais, ou seja, arquivos armazenados no 
próprio computador do usuário. Ao abrir um arquivo local no navegador, a URL exibida 
começa com "file://". 
 
mailto 
O esquema MAILTO é usado para criar um e-mail para um destinatário específico. Inserir 
uma URL começando com "mailto://" (ou mesmo omitindo o "//") em um navegador pode 
abrir uma janela de nova mensagem em um cliente de e-mail com o endereço de destinatário 
predefinido, conforme especificado na URL. 
 
Além disso, é importante notar que o serviço de correio eletrônico, como outros serviços na 
internet, depende de servidores acessíveis graças às conversões de endereço realizadas pelo 
DNS. As URLs podem variar significativamente em seus componentes, incluindo a presença ou 
ausência de portas, protocolos ou caminhos específicos, refletindo a diversidade de recursos e 
métodos de acesso na web. 
 
Exemplos de url 
www.estrategiaconcursos.com.br mailto:diego@carvalho?subject=informatica 
http://www.estrategiaconcursos.com.br https://www.estrategiaconcursos.com.br/professores 
mailto://contato@diegocarvalho.com.br ftp://admin@diegocarvalho.com.br 
http://www.estrategiaconcursos.com.br:80 mailto:professordiegocarvalho@gmail.com 
 
DNS: Hierarquia 
 
O domínio é o principal componente de uma URL e, por isso, dizemos que o DNS traduz, 
transforma, resolve um Nome/Domínio em um Endereço IP e vice-versa. Agora vamos falar mais 
detalhadamente sobre domínios. O DNS é um protocolo cliente/servidor que apresenta uma 
estrutura hierárquica e distribuída, em que seu espaço de nomes é dividido em vários servidores 
de domínio baseado em níveis. Vejam a imagem seguinte... 
 
 
 
O DNS (Domain Name System) é um protocolo cliente/servidor hierárquico e distribuído, 
essencial para a tradução de nomes de domínio em endereços IP e vice-versa. O espaço de 
nomes do DNS é organizado para garantir que cada nome seja único, evitando ambiguidades, já 
que cada endereço IP é exclusivo. A ICANN (Internet Corporation for Assigned Names and 
Numbers) é a entidade global responsável pelo registro e manutenção de domínios.  
 
.br
.gov
tesouro
.com
estratEgiaconcursos
.org
lbv
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
49
80
Ela define domínios nacionais, como .br para o Brasil, .pt para Portugal, .jp para o Japão e .es para 
a Espanha. No Brasil, o Registro.br é a entidade que gerencia os domínios .br. O custo de registro 
de um domínio é acessível, com planos de longo prazo custando cerca de R$3 por mês. Além disso, 
o domínio .br possui subcategorias, como .com.br para atividades comerciais e .org.br para 
organizações não-governamentais sem fins lucrativos.  
 
Algumas categorias têm restrições e exigem comprovação documental para empresas de setores 
específicos. 
 
 
 
Existem algumas regras que devem ser observadas em um nome de domínio registrado no 
Registro.br: (1) deve possuir entre 2 e 26 caracteres, não incluindo a categoria. Logo, o domínio 
www.x.com.br é inválido porque possui apenas 1 caractere; (2) deve ser composto por caracteres 
alfanuméricos. Logo, o domínio www.123.com.br é inválido porque não contém letras; (3) não pode 
começar ou terminar com hífen, mas pode ter acentuação e cedilha desde 2008. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
50
80
DNS: Whois 
 
Por fim, vamos falar rapidinho sobre o Whois! Trata-
se de um serviço que permite consultar informações 
sobre os responsáveis por domínios e blocos de IP 
registrados na Internet. Como assim, Diego? Imagine 
que houve uma tentativa de invasão à rede de um 
órgão, mas que foi impedida por um firewall, que 
salvou o endereço IP da tentativa de invasão.  
 
Qual seria uma atitude recomendável do administrador 
dessa rede? Bem, ele poderia consultar um Servidor 
Whois para tentar identificar informações úteis sobre 
o invasor. Galera, esse é apenas um cenário, mas você 
– sim, você mesmo – pode consultar um Servidor 
Whois em busca de informações sobre qualquer 
Domínio ou Endereço IP.  
 
Vamos tentar descobrir informações sobre o domínio www.estrategiaconcursos.com.br. Como se 
trata de um domínio brasileiro, basta acessar o registro.br em: 
 
https://registro.br/tecnologia/ferramentas/whois 
 
Protocolos Web 
INCIDÊNCIA EM PROVA: Altíssima 
Web: HTTP 
 
Hypertext transfer protocol (http) 
Protocolo da camada de aplicação utilizado para carregar páginas da web, enviar formulários, realizar transações 
online, obter recursos, entre outros. Trata-se de um protocolo baseado em um modelo de requisição-resposta 
entre um cliente (Navegador Web) e um servidor (Servidor Web): mensagens enviadas pelo cliente são chamadas 
de solicitações ou requisições (Requests) e as mensagens enviadas pelo servidor são chamadas de respostas 
(Responses). 
 
O HTTP (Protocolo de Transferência de Hipertexto) é um protocolo de camada de aplicação 
usado pelos navegadores para acessar conteúdos na web, incluindo textos, áudio, imagens e 
vídeos. Originalmente focado em hipertexto (textos com links para outros textos), agora abrange 
hipermídia, integrando multimídia ao hipertexto. Conforme a imagem seguinte, uma transação 
HTTP típica possui um Cliente HTTP e um Servidor HTTP.  
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
51
80
 
 
O cliente, como um navegador, solicita acesso a uma página web enviando uma mensagem de 
solicitação ao servidor. Se o acesso for autorizado, o servidor responde com a página desejada. 
Servidores web, diferentemente de servidores de e-mail, hospedam e armazenam páginas e 
recursos da web. Prosseguindo... toda solicitação ou requisição a um servidor web retorna um 
código de status de três dígitos e divididos em cinco categorias: 
 
CÓDIGO 
CATEGORIA 
SIGNIFICADO 
1XX 
INFORMAÇÃO 
100 significa que o servidor concorda em atender à requisição. 
 
2XX 
SUCESSO 
200 significa que a requisição foi bem-sucedida e 204 significa que a 
página está sem conteúdo. 
3XX 
REDIRECIONAMENTO 
301 significa que a página foi movida e 304 significa que a página em 
cache ainda é válida. 
4XX 
ERRO DO CLIENTE 
403 significa que a página é proibida e 404 significa que a página não foi 
encontrada. 
5XX 
ERRO DO SERVIDOR 
500 significa que houve um erro interno e 503 significa que você deve 
tentar novamente mais tarde. 
 
Professor, há como explicar melhor o que você quis dizer? Claro que sim! Façam um teste: abram um 
navegador e digitem: www.estrategiaconcursos.com.br/euamopinkfloyd. 
 
 
 
Vocês viram que retornou um erro? Pois é, Erro 404! Esse erro é da categoria Erro do Cliente e significa 
que uma determinada página não foi encontrada. Por quê, professor? Cara, essa página não foi 
encontrada basicamente porque ela não existe – eu acabei de inventar apenas para mostrar um 
código de retorno! Esse código sempre existirá para qualquer requisição, mas nem sempre será 
exibido para os usuários (se houve sucesso, não faz sentido exibir). 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
52
80
 
 
HTTP é um protocolo para transferência ou acesso de hipertexto e HTML é uma 
linguagem para criação de páginas web. HTTP é Protocolo e HTML é Linguagem. 
 
Web: HTTPS 
 
Hypertext transfer protocol SECURE (https) 
Protocolo da camada de aplicação utilizado para carregar páginas da web, enviar formulários, realizar transações 
online, obter recursos, entre outros, porém com uma camada adicional de segurança entre o cliente e o servidor. 
Possui recursos para criptografar a comunicação, protegendo a troca de dados contra interceptação e alteração. 
Esse protocolo requer certificados digitais para autenticar a identidade do servidor e garante que os dados 
transferidos sejam acessíveis apenas para o destinatário pretendido. Além disso, ele verifica se os dados enviados 
não foram alterados ou corrompidos durante a transferência e confirma a identidade do site para o usuário. 
 
O HTTPS é uma versão segura do HTTP, responsável pela transferência de páginas web com 
conteúdo multimídia entre um servidor e um cliente. A diferença principal é que o HTTPS 
adiciona uma camada de segurança usando os protocolos SSL/TLS, proporcionando criptografia, 
autenticação e integridade aos dados transmitidos. Isso significa que as informações são 
criptografadas. Como assim, Diego?   
 
Informações criptografadas tornam-se ilegíveis se interceptadas, e a autenticidade do servidor 
web é verificada por meio de certificados digitais. Por exemplo, em um café, se você estiver 
usando uma conexão HTTP para fazer compras online, seus dados do cartão de crédito podem ser 
facilmente interceptados. Com o HTTPS, mesmo que os dados sejam interceptados, eles 
permanecerão criptografados e seguros. 
 
Além disso, o HTTPS utiliza certificados digitais para confirmar a identidade do site. Seu navegador 
verifica a autenticidade do certificado com autoridades certificadoras, e se um certificado for 
inválido, expirado ou revogado, o navegador emitirá um aviso. Por exemplo: ao acessar um site 
de banco pela Internet, você verá "https://" e um cadeado na barra de endereço, indicando uma 
conexão segura e um certificado digital válido.  
 
Embora isso não seja uma garantia absoluta de segurança, oferece uma camada significativa de 
proteção para a transmissão de dados. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
53
80
 
 
Se você entrar em um site de um Internet Banking, você visualizará o endereço começando com 
https:// e um pequeno cadeado do lado esquerdo da barra de endereço indicando que a conexão a 
essa página é segura. Por quê? Porque veja que é informado que o certificado já foi recebido, já foi 
verificado e foi considerado válido. Galera, é claro que isso não é uma garantia absoluta, é apenas 
uma forma de garantir que a informação trafegada estará segura. 
 
 
 
Protocolo FTP 
INCIDÊNCIA EM PROVA: Altíssima 
 
FILE TRANSFER PROTOCOL (FTP) 
Protocolo da camada de aplicação baseado no modelo cliente/servidor utilizado para a transferência de arquivos 
entre sistemas. Ele pode transferir uma variedade de tipos de dados (incluindo arquivos binários e de texto), além 
de permitir upload e download de arquivos, além de suporte a comandos para manipulação de diretórios. Ademais, 
requer autenticação (nome de usuário e senha) para acesso, embora possa ter acesso anônimo. O FTP é 
amplamente utilizado para distribuição de arquivos, backup e transferência de dados entre sistemas. 
 
O FTP (File Transfer Protocol) é o protocolo responsável pela realização de transferências de 
arquivos entre um Cliente FTP e um Servidor FTP. Definições que já encontrei em prova: 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
54
80
 
- FTP é o protocolo de transferência de arquivos entre computadores; 
- FTP é o protocolo para transferência de arquivos entre dois computadores conectados à Internet; 
- FTP é o protocolo responsável pela transferência de arquivos remotos; 
- FTP é o protocolo que permite a cópia de arquivos entre dois computadores; 
- FTP é o protocolo responsável pelo download/upload de arquivos; 
- FTP é o protocolo que permite fazer upload de arquivos para um servidor remoto. 
 
Esse protocolo difere de outros por estabelecer duas conexões entre cliente e servidor: uma para a 
transferência dos dados em si (Porta TCP 20) e a outra para a troca de informações de controle 
(Porta TCP 21). Essa divisão ocorre para tornar o protocolo mais eficiente, visto que as informações 
de controle utilizam uma conexão mais simples, enquanto a transferência de dados possui uma 
conexão mais complexa, permitindo o envio de múltiplos arquivos, etc.  
 
É comum que empresas disponibilizem um Servidor FTP e as máquinas dos usuários possuam 
Clientes FTP. Dessa forma, diversos clientes podem fazer o upload de arquivos para o servidor, 
que funcionará como um repositório central de arquivos. Da mesma forma, clientes poderão 
fazer o download dos arquivos do repositório. O FTP permite fazer download, upload, renomeação, 
exclusão de arquivos de forma geralmente autenticada. Existem diferentes modos de transmissão: 
 
MODO DE TRANSMISSÃO DESCRIÇÃO 
FLUXO CONTÍNUO 
(stream) 
O arquivo é enviado, por um fluxo contínuo de bytes, ao TCP. Quando chega nesse 
protocolo, ele separa os dados recebidos em porções com um tamanho apropriado para 
o transporte – trata-se do modo-padrão. 
BLOCADO 
Os dados são entregues do FTP para o TCP em blocos. Nesse caso, cada bloco é precedido 
por um cabeçalho de três bytes. O primeiro byte é chamado de descritor de blocos; os dois 
seguintes deﬁnem o tamanho do bloco em bytes. 
COMPRIMIDO 
No caso de arquivos muito grandes, os dados podem ser comprimidos, antes de serem 
enviados, usando um algoritmo. 
 
 
Galera, por que nós utilizamos a internet? Basicamente para nos comunicar! E para haver 
comunicação, são necessárias duas partes: um emissor e um receptor. Quando você acessa um 
portal da web, quando você faz o download de um arquivo, quando você joga um jogo na internet, 
quando você acessa uma rede social ou quando você vê um vídeo no Youtube, sempre haverá 
transferência (envio ou recebimento) de informações. 
 
Por falar nisso, há dois termos que eu tenho certeza que vocês estão bastante familiarizados porque 
já fazem parte do nosso vocabulário em português: Download e Upload! Nós já sabemos que a 
Internet funciona por meio de uma arquitetura ou modelo chamado Cliente/Servidor! O que é isso, 
professor? Grosso modo, isso significa que ela é baseada em um conjunto de computadores que 
exercem a função de clientes ou servidores. Relembrando... 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
55
80
Os computadores servidores são aqueles que fornecem um serviço e os computadores clientes 
são aqueles que consomem um serviço. Sabe aquele domingo à noite em que quer ver um filme 
maneiro? Você liga sua televisão, acessa a página web da Netflix, escolhe um filme e começa a 
assisti-lo! Nesse momento, sua televisão funciona como um cliente que está consumindo um 
serviço. Esse serviço é disponibilizado por quem? Pela Netflix! 
 
A Netflix possui um bocado de computadores servidores que hospedam ou armazenam os 
filmes, então a sua televisão está consumindo um serviço de um servidor da Netflix. E quase 
tudo na internet é assim: você acessa o servidor do Estratégia para ver uma videoaula; você acessa 
o servidor do Spotify para ouvir uma música; você acessa o servidor do Google para acessar sua 
página e fazer alguma busca; e assim por diante. Dito isso, vamos ver o que é download e upload... 
 
Ambos os termos são utilizados para referenciar a transmissão de dados de um dispositivo para 
outro através de um canal de comunicação previamente estabelecido. O termo download está 
relacionado com a obtenção de conteúdo da Internet, em que um servidor hospeda dados que 
são acessados pelos clientes através de aplicativos específicos que se comunicam com o 
servidor por meio de protocolos preestabelecidos (Ex: HTTP, FTP, etc). 
 
De forma análoga, o termo upload faz referência a operação inversa à do download, isto é, refere-
se ao envio de conteúdo à internet. Do ponto de vista da participação do dispositivo que iniciou 
a transmissão de dados, a obtenção de dados de um dispositivo é chamada de download e a 
disponibilização de dados para um dispositivo é chamada de upload. Tudo certo? Então, vamos 
prosseguir... 
 
 
 
Eu já recebi essa dúvida no fórum dezenas de vezes, portanto vamos tentar deixar bastante claro 
para não haver margem para questionamentos! O objetivo principal do FTP é transferir arquivos, 
no entanto nem toda transferência de arquivos ocorrerá por FTP. É possível transferir arquivos 
por e-mail? Sim, nesse caso estaremos utilizando SMTP/MIME. É possível transferir arquivos por uma 
página web? Sim, nesse caso estaremos utilizando HTTP/HTTPS. 
 
Quando você faz o download de uma aula ou vídeo em nosso site, você está utilizando o HTTP para 
transferência de arquivos do servidor web para a sua máquina local. Em suma: HTTP é utilizado 
para transferência de hipertexto, mas pode ser utilizado alternativamente para transferência 
de arquivos; SMTP é utilizando para transferência de e-mails, mas pode ser utilizado 
alternativamente para transferência de arquivos; e existem dezenas de outros exemplos. 
 
Diversos outros protocolos possuem seus objetivos principais, mas alternativamente também 
permitem enviar arquivos – já o objetivo principal do FTP é a transferência de arquivos. A grande 
verdade é que o FTP tem sido cada vez menos utilizado – principalmente após a popularização do 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
56
80
armazenamento em nuvem (Cloud Storage). Eu arrisco dizer que a maioria de vocês nunca usou 
esse protocolo em toda vida, apesar de fazer transferência de arquivos há anos na internet.  
 
Há algum tempo, esse protocolo permanecia sendo utilizado para transferência de arquivos muito 
grandes. Hoje em dia, eu faço o upload do arquivo grande para nuvem e envio o link para quem eu 
quiser – sem precisar configurar um Cliente/Servidor FTP. Apesar de estar em desuso, ele continua 
sendo bastante cobrado em prova. Por essa razão, muito cuidado para não achar que toda 
transferência de arquivos ocorre por meio do FTP. 
 
Protocolos Diversos 
INCIDÊNCIA EM PROVA: baixíssima 
 
Agora veremos alguns protocolos que caem muito muito muito raramente em prova, portanto 
veremos bem rápido. Acompanhem a tabela seguinte... 
 
PROTOCOLOS 
DESCRIÇÃO 
telnet 
Trata-se de um protocolo cliente/servidor utilizado para permitir a comunicação remota entre 
computadores em uma rede de computadores. Ele proporciona uma facilidade de comunicação 
baseada em texto interativo bidirecional utilizando um terminal virtual, isto é, ele não permite o 
controle remoto da interface gráfica – permite apenas executar comandos em um terminal de outro 
computador. Vejam como ele é... 
 
 
 
Ele permite, por exemplo, acessar um computador remoto e executar um comando para desligá-lo. 
Nesse contexto, a máquina que oferece o acesso remoto é o servidor e o equipamento que acessa é 
o cliente.  O TELNET não garante uma comunicação segura, até dados e senhas são compartilhados 
em texto livre durante a conexão. Esse protocolo está obsoleto há anos, por conta de novos 
protocolos mais eficientes e por possuir diversos problemas de segurança.  
 
Ssh 
Trata-se de um protocolo cliente/servidor de acesso remoto que utiliza autenticação de chave 
pública baseada no servidor para estabelecer a identidade do usuário com segurança. A principal 
diferença para o protocolo anterior é que ele utiliza criptografia, o que garante confidencialidade e 
integridade de dados sobre uma rede insegura (como a Internet) e que os dados transmitidos na rede 
estejam seguros contra interceptações não autorizadas.  
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
57
80
 
 
Se vocês já trabalharam em alguma empresa grande, já devem ter ligado para um técnico de 
informática detalhando algum problema que foi resolvido remotamente. O técnico de suporte 
acessa o seu computador, realizando todas as manutenções ou correções requisitadas. Existem 
softwares que implementam diversos protocolos de acesso remoto (inclusive sobre sistemas 
operacionais diferentes)  – um dos mais conhecidos é o PuTTY.  
 
Irc 
Trata-se de um protocolo cliente/servidor utilizado basicamente para bate-papo e troca de arquivos, 
permitindo uma conversa em grupo ou privada (IRC – Internet Relay Chat). Quem é mais antigo sabe 
que antigamente a única maneira de falar com outra pessoa era por meio de um telefone. Quando 
eu, com uns oito anos de idade, vi um Cliente IRC pela primeira vez e descobri que era possível falar 
com outra pessoa pelo computador, eu achei genial! 
 
O Cliente IRC mais comum era o mIRC! Era lento e feio, mas para quem não tinha nada, era uma das 
melhores coisas do mundo. Crianças, eu vos apresento a comunicação via computador dos anos 90: 
 
 
 
Snmp 
Trata-se de um protocolo para monitoramento e gerenciamento de dispositivos em uma rede de 
computadores (SNMP – Simple Network Management Protocol). Para tal, esse protocolo coleta um 
conjunto de métricas de diversos dispositivos, tais como roteadores, computadores, servidores, 
entre outros. Ele opera sobre o Protocolo UDP na Porta 161 e está atualmente em sua terceira versão 
– SNMPv3.  
rtp 
Trata-se de um protocolo para transmissão de áudio e vídeo em tempo real sobre Redes IP (RTP – 
Real-time Transport Protocol). Ele é comumente utilizado em aplicações VoIP e opera sobre o 
Protocolo UDP. Existe uma polêmica sobre a camada em que opera esse protocolo – alguns afirmam 
que se trata da camada de transporte e outros afirmam que se trata da camada de aplicação. 
Lembrem-se que nem sempre é possível alocar perfeitamente um protocolo a uma camada. 
nntp Trata-se de um protocolo da camada de aplicação utilizado para grupos de discussão, permitindo 
especificar, buscar, recuperar e postar artigos usando um sistema de transmissão confiável. Ele 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
58
80
também era útil para leitura de notícias em tempos remotos. Esse protocolo encontra-se obsoleto e 
está em desuso há muito anos, mas vez ou outra cai em prova.  
 
 
TELNET 
SSH 
NÃO! NÃO TEM CRIPTOGRAFIA 
SIM! TEM CRiPTOGRAFIA 
 
Serviço VoIP 
INCIDÊNCIA EM PROVA: média 
 
Voip 
VoIP (Voice over Internet Protocol) é uma tecnologia que permite a transmissão de voz e comunicações multimídia 
(como chamadas telefônicas, videotelefonia e sessões de conferência) através da Internet ou de outras redes 
baseadas em protocolos IP. Essencialmente, o VoIP transforma sinais de voz em dados digitais que podem ser 
enviados pela internet, como qualquer outro tipo de dado. 
 
A tecnologia de VoIP (ou Voz sobre IP) representa uma evolução da telefonia tradicional para a 
digital. Nela, a voz é convertida em dados digitais e transmitida via Internet, ao contrário da 
telefonia convencional (PSTN) que usava comutação por circuitos para estabelecer uma linha 
dedicada entre os interlocutores. O VoIP usa a comutação por pacotes, que é mais eficiente e 
flexível para o uso de largura de banda, além de suportar diversos serviços.  
 
A infraestrutura da Internet inclui dispositivos, cabos, algoritmos, técnicas, ferramentas, 
paradigmas e a Arquitetura TCP/IP, que coordena a comunicação entre dispositivos na Internet. No 
contexto do VoIP, a voz é convertida em sinais digitais e encapsulada em pacotes pelo 
Protocolo IP. Os principais protocolos de transporte na Internet são TCP e UDP. Agora eu tenho 
uma pergunta: vocês acham que o VoIP utiliza qual desses protocolos?  
 
 
 
A voz é encapsulada em pacotes e 
preparada para transporte  
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
59
80
TCP é confiável e orientado à conexão, garantindo a entrega correta dos dados, enquanto UDP é 
mais rápido, mas não garante a entrega. VoIP utiliza UDP, juntamente com protocolos como SIP11 
ou H.323, para estabelecer conexões. Embora o UDP não seja confiável, sua combinação com 
outros protocolos faz do VoIP uma aplicação orientada à conexão e não-confiável, priorizando 
a simplicidade e agilidade na comunicação. 
 
Agora vamos imaginar um cenário em que eu desejo te enviar um áudio que eu gravei tocando 
sanfona. Se eu te enviar esse áudio por meio do Protocolo UDP e houver uma perda de pacotes no 
meio do caminho, você receberá o áudio faltando partes. Imagine só... vai perder a introdução da 
música, por exemplo, que eu toquei com todo carinho. Nesse caso, é importante que você receba 
os dados, logo é mais interessante utilizar o Protocolo TCP em vez do Protocolo UDP. 
 
Agora vamos imaginar outro cenário em que você deseja me ligar para avisar que passou no 
concurso público dos seus sonhos. Eu atendo sua ligação, mas volta e meia há um corte ou uma 
pequena interrupção. Ora, faz sentido eu receber depois essas partes que foram perdidas? Não, 
perdeu, já era! Nesse caso, é mais interessante utilizar o Protocolo UDP em vez do Protocolo TCP. 
E em qual contexto se encaixa o uso do VoIP? No segundo, porque ele utiliza o UDP! 
 
Professor Diego... eu posso afirmar que ele utiliza um serviço com conexão não confiável e não 
orientado à conexão? Não! Como não? Aqui há um detalhe: VoIP utiliza outro protocolo (SIP ou 
H.323) junto com o UDP para garantir o estabelecimento de uma conexão com o destinatário. Logo, 
podemos afirmar que uma aplicação VoIP é orientada à conexão e não-confiável. O foco aqui é 
na simplicidade e na agilidade da comunicação. 
 
VANTAGENS DO VOIP 
Permite fazer e receber ligações telefônicas tanto em uma rede local (LAN/Interna) quanto em uma rede pública 
(WAN/Externa). 
Permite fazer e receber ligações para telefones fixos ou telefones celulares da telefonia convencional ou da 
telefonia digital por meio da utilização de um conjunto de dispositivos (adaptadores, gateways, etc). 
Permite compartilhar o canal de comunicação de dados com outros serviços, podendo transmitir – além da voz – 
vídeos, imagens, entre outros. 
Permite uma instalação extremamente escalável, podendo expandir com facilidade sem a necessidade de novas 
linhas dedicadas e aproveitando a infraestrutura de Redes IP12. 
 
desVANTAGENS DO VOIP 
Pode oscilar e perder a qualidade da ligação caso não esteja disponível uma conexão eficiente com a Internet. 
Menos confiável que a telefonia convencional em relação a quedas de energia. 
Podem ocorrer problemas de latência, atraso, interrupção e cortes na comunicação, além de perdas de dados. 
 
11 O SIP é um protocolo aberto utilizado para controlar sessões de comunicação multimídia, como chamadas de voz via Internet, possibilitando 
estabelecer, alterar e encerrar conexões. Funciona sobre TCP/UDP e opera com um mecanismo de requisição-resposta, semelhante ao HTTP, 
facilitando a interação em tempo real entre usuários. 
12 Em geral, há duas alternativas: (1) substituir o telefone convencional por um telefone IP conectado por meio de um conector RJ-45; (2) ou utilizar 
um ATA (Adaptador de Terminal Analógico), que converte um sinal analógico em um sinal digital e vice-versa. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
60
80
Apresenta menor disponibilidade do canal de comunicação, uma vez que não possui um canal dedicado. 
 
Convergência de Redes 
 
A Convergência de Rede é uma tendência tecnológica que consiste em unificar diversas redes 
distintas em uma única rede de computadores. Esta rede unificada é capaz de fornecer os serviços 
anteriormente oferecidos pelas redes separadas. Anteriormente, as redes de comunicação eram 
segmentadas por tipo de serviço (voz, imagens, vídeos, documentos, etc.). A convergência de redes 
introduziu a ideia de usar uma única rede para oferecer diferentes tipos de serviços. 
 
Uma rede convergente suporta tráfego de voz, imagem e dados em uma só rede digital, operando 
de maneira integrada. Isso resulta em uma gestão de tecnologia mais eficiente e custos reduzidos. 
O VoIP é um exemplo chave dessa convergência, permitindo às empresas integrar funcionalidades 
como desvio de chamadas, conferências, trabalho remoto, URA (Unidade de Resposta Audível), 
filas de espera com música, caixa postal e identificação de transferência, entre outros. 
 
Videoconferências 
 
Durante a pandemia de COVID-19, as conferências virtuais se tornaram uma tendência global. A 
adoção de teletrabalho por órgãos públicos impulsionou o uso de videoconferências, promovendo 
reuniões remotas e comunicação interna. Isso reduz custos de deslocamento e aumenta a 
eficiência. Videoconferência é a interação visual e sonora entre pessoas em locais diferentes, 
criando a sensação de estarem no mesmo local.  
 
Existem diferenças conceituais entre webconferências e videoconferências. As webconferências 
geralmente são mais simples e utilizadas em ambientes domésticos; já as videoconferências são 
mais comuns em ambientes corporativos. As webconferêcias utilizam equipamentos básicos e 
softwares como Hangouts e Skype, enquanto as videoconferências usam equipamentos mais 
sofisticados e softwares como Zoom e Teams. 
 
Com a pandemia, essas diferenças diminuíram. Em sistemas de videoconferência, conexões ponto-
a-ponto envolvem duas câmeras, enquanto sistemas multiponto conectam três ou mais câmeras, 
geralmente com um MCU (Unidade de Controle Multiponto). Há dois modos de videoconferência: 
Modo VAS (Switch Ativado por Voz), onde a janela do falante fica em destaque, e Modo Presença 
Contínua, que mostra todas as câmeras simultaneamente.  
 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
61
80
GLOSSÁRIO 
 
Termo
definição 
REDES DE 
COMPUTADORES
Conjunto de computadores e dispositivos interconectados para compartilhamento de 
recursos e troca de informações. 
PROTOCOLOS DE 
REDES
Conjunto de regras que determinam como os dados são transmitidos e recebidos em uma 
rede. 
TCP/IP
Conjunto de protocolos de comunicação usados para interconexão de redes e na internet.
 
INTERNET
Rede global de computadores interconectados que utilizam o protocolo TCP/IP para 
comunicação. 
DISPOSITIVOS DE 
REDES
Equipamentos utilizados para conectar e gerenciar a comunicação em redes de 
computadores. 
HIERARQUIA DE 
CAMADAS
Estrutura de organização de protocolos de rede em camadas com funções específicas. 
 
SERVIÇOS DE REDE
Funções disponíveis em uma rede, como compartilhamento de arquivos, impressoras, 
comunicação, etc. 
INTEROPERABILIDADE
Capacidade de sistemas e dispositivos diferentes se comunicarem e trabalharem juntos.
 
SISTEMAS ABERTOS
Sistemas que suportam interoperabilidade e são construídos com padrões abertos.
 
CONVERGÊNCIA DE 
REDES
Processo de unificar diferentes tipos de redes, serviços e protocolos em uma única 
infraestrutura de rede. 
MODELO OSI
Modelo conceptual que caracteriza e padroniza as funções de um sistema de 
telecomunicações ou computação. 
ISO
Organização internacional que desenvolve e publica padrões internacionais (International 
Organization for Standardization). 
CAMADA FÍSICA
Camada do modelo OSI que lida com a transmissão física de dados através do meio.
 
MEIO DE 
TRANSMISSÃO
Material ou substância que carrega o sinal de uma extremidade à outra (como cabos ou ondas 
de rádio). 
CAMADA DE ENLACE
Camada do modelo OSI responsável pelo controle da forma como os dados são transmitidos.
 
CONTROLE DE FLUXO
Técnica para evitar que um transmissor sobrecarregue um receptor com dados.
 
CONTROLE DE ERROS
Métodos usados para detectar e corrigir erros na transmissão ou armazenamento de dados.
 
CAMADA DE 
TRANSPORTE
Camada do modelo OSI responsável pelo transporte confiável de dados. 
 
Multiplexação
Técnica que combina múltiplos sinais em um único meio ou canal de transmissão.
 
Camada de sessão
Camada do modelo OSI que estabelece, gerencia e termina sessões entre aplicações.
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
62
80
Camada de 
apresentação
Camada do modelo OSI que traduz os dados entre o formato da rede e o formato entendido 
pela aplicação. 
Camada de 
aplicação
Camada superior do modelo OSI que fornece serviços para aplicações de software. 
 
Roteamento de 
pacotes
Processo de seleção de caminhos em uma rede para enviar pacotes de dados. 
 
Endereço ip
Identificador numérico único utilizado para identificar dispositivos em uma rede IP.
 
Endereço ip público
Endereço IP visível na internet e único em todo o espaço da rede global.
 
Endereço ip privado
Endereço IP utilizado dentro de uma rede local (LAN) e não roteável na internet.
 
Tabelas de 
roteamento
Estrutura de dados que armazena as rotas para diferentes destinos em uma rede. 
 
Nat
Técnica que modifica os endereços de rede nos cabeçalhos de pacotes IP enquanto eles estão 
em trânsito. 
Mtu
Maior tamanho de pacote ou quadro de dados que pode ser enviado em uma rede.
 
Endereçamento por 
classes
Sistema antigo de categorização de endereços IP baseado no intervalo de números IP. 
 
Icmp
Protocolo utilizado para diagnosticar e relatar problemas na comunicação de dados na 
internet. 
Arp
Protocolo que mapeia endereços IP em endereços físicos de rede (endereços MAC).
 
Dns
Sistema que traduz nomes de domínios legíveis por humanos em endereços IP numéricos.
 
dhcp
Protocolo que automaticamente fornece um endereço IP e outras configurações de rede para 
dispositivos em uma rede. 
ftp
Protocolo usado para transferir arquivos entre computadores em uma rede TCP/IP.
 
http
Protocolo padrão para transmissão de documentos hipermídia na World Wide Web.
 
https
Versão segura do HTTP que usa criptografia para proteger a comunicação entre navegador 
e servidor. 
Ssl/tls
Protocolos de criptografia para garantir a segurança na comunicação de dados na internet.
 
telnet
Protocolo de rede usado para realizar comunicação remota baseada em texto com outro 
computador. 
Ssh
Protocolo para operações de rede seguras, como login remoto e transferência de arquivos.
 
Snmp
Protocolo usado para gerenciar e monitorar dispositivos em redes de computadores.
 
Rtp
Protocolo usado para entrega de áudio e vídeo em tempo real pela internet.
 
Smtp
Protocolo padrão para envio de e-mails através de redes de computadores.
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
63
80
==6306a==
Pop
Protocolo utilizado para recuperar e-mails de um servidor de e-mail, geralmente baixando-
os para o cliente de e-mail local. 
Imap
Protocolo que permite acessar e gerenciar e-mails diretamente no servidor de e-mail, 
facilitando o acesso a partir de múltiplos dispositivos. 
Mime
Padrão que expande a capacidade do e-mail para suportar a transferência de dados que não 
são apenas texto, como imagens e arquivos de áudio. 
Webmail
Serviço de e-mail acessível via navegador da web, permitindo enviar, receber e gerenciar e-
mails sem a necessidade de um cliente de e-mail instalado. 
Whois
Protocolo utilizado para consultar informações sobre o registro de domínios na Internet, 
incluindo o proprietário, a data de criação e outros detalhes. 
url
Endereço usado para identificar e acessar recursos na Internet, como páginas da web ou 
arquivos. 
Voip
Tecnologia que permite realizar chamadas de voz e vídeo através da Internet ao invés de 
redes telefônicas tradicionais. 
Irc
Protocolo de comunicação usado para conversas em grupo ou privadas em tempo real 
através da Internet. 
Videoconferência
Sistema de comunicação que permite realizar reuniões ou conferências com vídeo e áudio 
entre participantes em locais diferentes. 
Webconferência
Tipo de conferência online que utiliza a web para realizar reuniões ou apresentações virtuais, 
geralmente com suporte a compartilhamento de tela e colaboração em tempo real. 
Crc
Método utilizado para detectar erros em dados digitais através da aplicação de um algoritmo 
de soma de verificação. 
Verificação de 
paridade
Técnica simples para detecção de erros em dados digitais, que adiciona um bit de paridade 
para garantir que o número total de bits definidos como '1' seja par ou ímpar. 
Checksum
Valor calculado a partir de um conjunto de dados para verificar a integridade desses dados 
durante a transmissão ou armazenamento. 
Llc
Subcamada da camada de enlace de dados, responsável pela identificação e encapsulamento 
de protocolos da camada de rede, e pelo controle de fluxo e correção de erros. 
Mac
Subcamada da camada de enlace de dados que controla o acesso ao meio de transmissão 
físico, atribuindo endereços únicos (endereços MAC) a cada dispositivo na rede. 
Fragmentação
Processo de dividir dados em pedaços menores (fragmentos) para transmissão em redes que 
têm limitação de tamanho máximo de pacote, e posterior reagrupamento no destino. 
Three-way 
handshake
Método utilizado pelo protocolo TCP para estabelecer uma conexão entre dois dispositivos, 
envolvendo o envio sequencial de um pacote SYN, um pacote SYN-ACK, e um pacote ACK. 
Portas
Números utilizados para identificar processos ou serviços específicos em dispositivos de 
rede, permitindo a comunicação direcionada e a multiplexação de serviços. 
Certificados 
digitais
Arquivos eletrônicos que associam a identidade de uma entidade (como uma pessoa ou 
organização) a uma chave pública. 
Grupos de 
discussão
Espaços online para troca de mensagens e informações sobre tópicos específicos, onde os 
usuários podem postar e responder a mensagens. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
64
80
QUESTÕES COMENTADAS – DIVERSAS BANCAS 
 
1. (REIS&REIS / PREFEITURA DE POTIM-SP – 2022) No contexto da manipulação de arquivos na 
Internet, o termo que corresponde à ação de transferir dados de um computador remoto para 
um computador local é conhecida como: 
 
a) Copy. 
b) Paste. 
c) Download. 
d) Upload. 
 
Comentários: 
 
Quando há a transferência de dados de um dispositivo remoto para um computador local, do ponto 
de vista do computador local temos um download. Já do ponto de vista do computador remoto 
temos um upload. 
              
Gabarito: Letra C 
 
2. (QUADRIX / CRF-GO – 2022) O FTP (File Transfer Protocol) é o protocolo de transferência de 
hipertexto. É ele que permite a navegação na Word Wide Web. 
 
Comentários: 
 
Na verdade, o FTP é o protocolo de transferência de arquivos entre computadores – o protocolo de 
transferência de hipertexto é o HTTP. 
              
Gabarito: Errado 
 
3. (FADESP / SEFA-PA – 2022) O algoritmo de roteamento que mantém uma tabela com a melhor 
distância conhecida a cada destino, determina qual enlace deve ser utilizado, bem como atualiza 
as tabelas por meio de troca de informações com os roteadores vizinhos, fazendo com que, no 
final, cada roteador saiba o melhor enlace para alcançar cada destino é o: 
 
a) caminho mais curto 
b) inundação 
c) vetor de distância 
d) estado de enlace 
e) controle de congestionamento 
 
Comentários: 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
65
80
Esse é um exemplo de questão em que o examinador acha que está aplicando prova para alunos de 
doutorado. Esse nível de aprofundamento do algoritmo específico de roteamento é surreal até para 
alunos da área de redes de computadores. O examinador decidiu ler um parágrafo do livro do 
Andrew Tanenbaum e fazer uma questão absurda: 
 
“Os algoritmos de roteamento, que usam vetor de distância, operam de forma que cada roteador 
mantenha uma tabela (isto é, um vetor), que fornece a melhor distância conhecida até o destino, e 
também indica qual linha deve ser utilizada para a transmissão. Tais tabelas são atualizadas através 
da troca de informações com os vizinhos”. 
 
Gabarito: Letra C 
 
4. (FADESP / SEFA-PA – 2022) Considerando as Redes de Datagrama, analise as afirmativas a 
seguir, julgando-as verdadeiras (V) ou falsas (F). 
 
I. Em uma rede de comutação de pacotes não existe reserva de recursos, pois os recursos são 
alocados sob demanda. 
 
II. O endereço de destino no cabeçalho de um pacote em uma rede de datagrama permanece o 
mesmo durante toda a jornada do pacote. 
 
III. A comutação na Internet é realizada usando a metodologia de datagrama para a comutação 
de pacotes na camada de transporte.  
 
A sequência que expressa corretamente o julgamento das afirmativas é: 
 
a) I - F; II - V; III - F. 
b) I - F; II - F; III - V.  
c) I - V; II - V; III - F. 
d) I - V; II - F; III - F. 
e) I - F; II - V; III - V. 
 
Comentários: 
 
(I) Correto. É na rede de comutação por circuito que há reserva de recursos; já na rede comutada 
por pacotes, os recursos são compartilhados; (II) Correto. O endereço de destino do pacote não é 
alterado durante a jornada do pacote; (III) Errado, é na camada de rede e, não, transporte. 
 
Gabarito: Letra C 
 
5. (FADESP / SEFA-PA – 2022) Considerando o modelo em camadas OSI utilizado para o projeto 
de sistemas de redes de computadores, julgue verdadeira (V) ou falsa (F) cada uma das 
afirmativas a seguir. 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
66
80
I. A camada de Rede é responsável por transferir os pacotes da origem ao destino, fornecer 
ligação entre as redes e recuperar erros. 
 
II. A camada de Enlace de dados é responsável por organizar bits em frames, comprimir os dados 
e fornecer entrega nó a nó. 
 
III. A camada de Transporte é responsável por prover a entrega confiável de mensagens de 
processo a processo, criptografar e comprimir os dados. 
 
A sequência correta é: 
 
a) I - F; II - V; III - V. 
b) I - V; II - F; III - V.  
c) I - V; II - V; III - F.  
d) I - F; II - F; III - F.  
e) I - V; II - V; III - V. 
 
Comentários: 
 
 
 
(I) Errado, a recuperação de erros é função da camada de transporte; (II) Errado, a compressão de 
dados é função da camada de apresentação; (III) Errado, criptografar e comprimir dados é função 
da camada de apresentação. 
 
Gabarito: Letra D 
 
6. (CESGRANRIO / Banco do Brasil - 2021) O serviço de correio eletrônico é uma ferramenta 
essencial para o trabalho do dia a dia dos colaboradores de uma empresa. Para garantir a 
segurança da comunicação do cliente de correio eletrônico com os servidores de correio 
eletrônico de entrada e de saída de mensagens, é importante configurar a utilização do padrão 
de segurança: 
 
a) TLS 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
67
80
b) SMTP 
c) IMAP  
d) POP3 
e) HTTP 
 
Comentários: 
 
Para garantir a segurança da comunicação do cliente de correio eletrônico com os servidores de 
correio eletrônico de entrada e de saída de mensagens, é importante configurar a utilização do 
padrão de segurança TLS. 
 
TLS (Transport Layer Security) é um protocolo de segurança que criptografa o tráfego de dados 
entre o cliente de correio eletrônico e os servidores de correio eletrônico. Isso garante que ninguém, 
exceto as partes autorizadas, possa interceptar e ler as mensagens enviadas. Além disso, TLS 
também fornece autenticação e verificação de integridade de mensagens, o que garante que as 
mensagens sejam entregues ao destinatário correto. 
 
Gabarito: Letra A  
 
7. (CESGRANRIO / Banco do Brasil - 2021) Apesar de os navegadores serem as ferramentas 
dominantes na internet, vários serviços possuem ferramentas próprias mais adequadas e, 
inclusive, mais otimizadas para protocolos específicos. Um desses protocolos foi desenvolvido 
para a transferência de arquivos, sendo usado a partir de programas como FileZilla. Esse 
protocolo é conhecido como: 
 
a) ftp 
b) imap 
c) pop3 
d) ssh 
e) telnet 
 
Comentários:  
 
(a) Correto, trata-se de um protocolo para transferência de arquivos; (b) Errado, trata-se de um 
protocolo para recebimento de e-mail; (c) Errado, trata-se de um protocolo para recebimento de e-
mail; (d) Errado, trata-se de um protocolo para acesso remoto com criptografia; (e) Errado, trata-se 
de um protocolo para acesso remoto sem criptografia. 
 
Gabarito: Letra A   
 
8. (CESGRANRIO / Banco do Brasil - 2021) Sabendo que o banco em que trabalha vai colocar 
centenas de ATMs em shoppings e postos de gasolina, um funcionário de TI propôs que cada 
ATM mandasse periodicamente um sinal de status, por meio do protocolo UDP. Esse protocolo 
do conjunto TCP/IP é considerado como parte da camada: 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
68
80
 
a) de aplicações 
b) de transporte 
c) de rede 
d) de enlace de dados 
e) física 
 
Comentários: 
 
UDP (User Datagram Protocol) é um protocolo da camada de transporte – assim como TCP 
(Transport Layer Protocol). Lembrando que o UDP é um protocolo sem conexão que fornece um 
sistema de entrega de melhor esforço que é usado principalmente para transmitir mensagens em 
uma rede. O UDP é mais rápido que o TCP, mas não fornece a confiabilidade e ordenação do TCP. 
 
Gabarito: Letra B  
 
9. (CESGRANRIO / Banco do Brasil - 2021) Ao chegar para seu primeiro dia de emprego no banco, 
um novo gerente de TI percebeu que era demandado muito esforço no setor para controle do 
número IP de cada computador, o que causava, também, alguns erros por uso múltiplo do 
mesmo IP nas redes. 
 
Percebendo uma oportunidade de melhoria, o novo gerente decidiu que os computadores 
passariam a obter automaticamente um número IP, por meio do protocolo: 
 
a) DHCP 
b) DNS 
c) HTTP  
d) IMAP 
e) SMTP 
 
Comentários: 
 
O protocolo que permite obter um número de endereço IP de forma automática é o DHCP. O DHCP 
(Dynamic Host Configuration Protocol) é um protocolo que permite que computadores e outros 
dispositivos na rede obtenham automaticamente configurações de IP, como endereço IP, máscara 
de sub-rede, gateway padrão e outras configurações de rede. O DHCP ajuda a simplificar o processo 
de configuração de rede, pois elimina a necessidade de configurar manualmente cada dispositivo. 
 
DNS é um protocolo para tradução de endereços IP em nome de domínio e vice-versa; HTTP é um 
protocolo para transferência de hipertexto geralmente utilizado em navegadores; e IMAP/SMTP 
são protocolos de correio eletrônico. 
 
Gabarito: Letra A 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
69
80
==6306a==
10. (IDIB / Ministério da Economia – 2021) Quando utilizamos a Internet é importante que nossos 
dados estejam seguros, de preferência criptografados. Existem alguns protocolos que são 
utilizados para os vários serviços da Internet e cada um deles faz uso de diferentes protocolos. 
Assinale a alternativa que apresenta um dos protocolos de comunicação que garante a 
comunicação segura através da Internet:  
 
a) TELNET 
b) SSL 
c) HTTP 
d) FTP 
e) IMAP 
 
Comentários: 
 
O único protocolo de comunicação listado na questão que garante a comunicação segura é o SSL 
(Secure Socket Layer). 
 
Gabarito: Letra B 
 
11. (IDIB / Ministério da Economia – 2021) Dentre os vários protocolos utilizados na Internet, um 
pode ser considerado como principal, pois é o que permite a navegação nas páginas eletrônicas 
da Internet, permitindo a transferência de dados como hipertexto. Assinale a alternativa que 
identifica corretamente esse protocolo: 
 
a) FTP 
b) SSL 
c) HTTP 
d) NMAP 
e) SMTP 
 
Comentários: 
 
O protocolo para transferência de hipertexto é o HTTP (HyperText Transfer Protocol). 
 
Gabarito: Letra C 
 
12. (CS-UFG / APARECIDAPREV – 2018) Há sites na Internet que são acessados por meio do 
protocolo HTTPS, como, por exemplo, o site https://cs.ufg.br. 
  
Qual é a função do HTTPS? 
 
a) Tornar mais rápida a navegação pelo site. 
b) Bloquear as janelas pop-up. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
70
80
c) Garantir que o navegador apresente uma única página por aba. 
d) Fazer com que os dados sejam transmitidos de forma criptografada. 
 
Comentários: 
 
O protocolo da camada de aplicação (HTTPS) tem a mesma finalidade do HTTP. Ele é responsável 
pela transferência, formatação e apresentação de páginas web com conteúdo multimídia (textos, 
áudio, imagens, etc) entre um servidor e um cliente. No entanto, ele realiza transferências de forma 
segura e criptografada, oferecendo autenticação e integridade às páginas de um Servidor Web. 
Sendo assim, ele possui a função de transmitir os dados de forma segura, criptografada.  
 
Gabarito: Letra D 
 
13. (IADES / ARCON PA – 2018) [...] é um tipo de rede local que utiliza sinais de rádio para 
comunicação. 
 
CERT.br. Centro de Estudos, Resposta e Tratamento de Incidentes de 
Segurança no Brasil. Cartilha de Segurança para Internet. Disponível em: 
<https://cartilha.cert.br/livro/cartilha_segurança_internet.pdf>. 
Acesso em: 28 jun. 2018. 
 
A definição apresentada refere-se a: 
 
a) IP: Internet Protocol. 
b) DNS: Domain Name Server. 
c) SMTP: Simple Mail Transfer Protocol. 
d) URL: Universal Resource Locator. 
e) Wi-Fi: Wireless Fidelity. 
 
Comentários: 
 
(a) Errado. O IP é o protocolo de comunicação da Internet responsável por endereçar os dispositivos 
em uma rede; (b) Errado. O DNS é o sistema e protocolo responsável pela resolução de nomes da 
Internet, isto é, por traduzir os endereços IPs numéricos em nomes; (c) Errado. O SMTP é um 
protocolo utilizado para envios de correio eletrônico; (d) Errado. A URL é o identificador único usado 
para localizar um recurso na Internet; (e) Correto. O Wi-Fi é a tecnologia composta por um conjunto 
de especificações (IEEE802.11) para redes locais sem fio (WLAN). A ideia do Wi-Fi é possibilitar a 
comunicação de dispositivos sem necessidade de cabos, utilizando a propagação das ondas de 
rádio através de antenas.  
 
Gabarito: Letra E 
 
14. (IDECAN / IPC – 2018) Considerando os recursos que podem ser consumidos ou acessados na 
Internet, analise as seguintes informações. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
71
80
 
I. O FTP é o protocolo utilizado para a transferência de arquivos entre duas máquinas ligadas à 
Internet. 
 
II. Um correio eletrônico permite a troca de mensagens que um usuário de Internet pode fazer 
para outras pessoas conectados à Internet. 
 
III. O HTTP é o protocolo utilizado para controlar a comunicação entre o servidor de Internet e 
o browser ou navegador. 
 
IV. O ICMP é o protocolo responsável por estabelecer a comunicação entre os computadores 
emissores e receptores de maneira na qual a informação não se perca na rede. 
 
De acordo com as afirmativas acima, marque a alternativa correta. 
 
a) Apenas as afirmativas I e II estão corretas. 
b) Apenas as afirmativas I, II e III estão corretas. 
c) Apenas as afirmativas II e III estão corretas. 
d) Apenas as afirmativas I, II e IV estão corretas. 
 
Comentários:  
 
(I) Correto, ele é realmente um protocolo para transferência de arquivos entre duas máquinas 
conectadas à Internet; (II) Correto, ele realmente permite a troca de mensagens entre pessoas na 
internet; (III) Correto, ele é utilizado para controlar a comunicação a comunicação entre servidor de 
Internet (é um nome ruim, o ideal seria chamar de Servidor Web) e navegador; (IV) Errado, a função 
do ICMP é fornecer relatórios de erros e, não, estabelecer a comunicação. 
 
Gabarito: Letra B 
 
15. (AOCP / ITEP-RN – 2018) Em relação à transferência de arquivos pela internet, assinale a 
alternativa correta. 
 
a) Quando uma pessoa envia um arquivo de seu computador para um site na internet, a 
operação de transferência que está sendo executada é conhecida como Download. 
 
b) FTP é um protocolo que pode ser utilizado para transferir arquivos entre computadores 
conectados à internet. 
 
c) Podemos considerar os termos Upload e Download como análogos, ou seja, possuem o 
mesmo significado. 
 
d) O protocolo FTP é utilizado exclusivamente para se realizar o acesso a websites na internet. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
72
80
 
e) O termo Upload se refere à velocidade na qual um computador conectado à internet consegue 
receber os dados de um website qualquer. 
 
Comentários:  
 
(a) Errado, está sendo executado um Upload; (b) Correto, o Protocolo FTP é comumente utilizado 
para transferência de arquivos entre computadores via internet; (c) Errado, eles possuem 
significados diametralmente opostos: download para recebimento de dados e upload para envio de 
dados; (d) Errado, ele é utilizado exclusivamente para a transferência de arquivos na internet – a 
questão trata do Protocolo HTTP; (e) Errado, upload é a operação de transferência de dados do 
computador do usuário para um servidor na internet. 
 
Gabarito: Letra B 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
73
80
LISTA DE QUESTÕES – DIVERSAS BANCAS 
 
1. (REIS&REIS / PREFEITURA DE POTIM-SP – 2022) No contexto da manipulação de arquivos na 
Internet, o termo que corresponde à ação de transferir dados de um computador remoto para 
um computador local é conhecida como: 
 
a) Copy. 
b) Paste. 
c) Download. 
d) Upload. 
 
2. (QUADRIX / CRF-GO – 2022) O FTP (File Transfer Protocol) é o protocolo de transferência de 
hipertexto. É ele que permite a navegação na Word Wide Web. 
 
3. (FADESP / SEFA-PA – 2022) O algoritmo de roteamento que mantém uma tabela com a melhor 
distância conhecida a cada destino, determina qual enlace deve ser utilizado, bem como atualiza 
as tabelas por meio de troca de informações com os roteadores vizinhos, fazendo com que, no 
final, cada roteador saiba o melhor enlace para alcançar cada destino é o: 
 
a) caminho mais curto 
b) inundação 
c) vetor de distância 
d) estado de enlace 
e) controle de congestionamento 
 
4. (FADESP / SEFA-PA – 2022) Considerando as Redes de Datagrama, analise as afirmativas a 
seguir, julgando-as verdadeiras (V) ou falsas (F). 
 
I. Em uma rede de comutação de pacotes não existe reserva de recursos, pois os recursos são 
alocados sob demanda. 
 
II. O endereço de destino no cabeçalho de um pacote em uma rede de datagrama permanece o 
mesmo durante toda a jornada do pacote. 
 
III. A comutação na Internet é realizada usando a metodologia de datagrama para a comutação 
de pacotes na camada de transporte.  
 
A sequência que expressa corretamente o julgamento das afirmativas é: 
 
a) I - F; II - V; III - F. 
b) I - F; II - F; III - V.  
c) I - V; II - V; III - F. 
d) I - V; II - F; III - F. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
74
80
e) I - F; II - V; III - V. 
 
5. (FADESP / SEFA-PA – 2022) Considerando o modelo em camadas OSI utilizado para o projeto 
de sistemas de redes de computadores, julgue verdadeira (V) ou falsa (F) cada uma das 
afirmativas a seguir. 
 
I. A camada de Rede é responsável por transferir os pacotes da origem ao destino, fornecer 
ligação entre as redes e recuperar erros. 
 
II. A camada de Enlace de dados é responsável por organizar bits em frames, comprimir os dados 
e fornecer entrega nó a nó. 
 
III. A camada de Transporte é responsável por prover a entrega confiável de mensagens de 
processo a processo, criptografar e comprimir os dados. 
 
A sequência correta é: 
 
a) I - F; II - V; III - V. 
b) I - V; II - F; III - V.  
c) I - V; II - V; III - F.  
d) I - F; II - F; III - F.  
e) I - V; II - V; III - V. 
 
6. (CESGRANRIO / Banco do Brasil - 2021) O serviço de correio eletrônico é uma ferramenta 
essencial para o trabalho do dia a dia dos colaboradores de uma empresa. Para garantir a 
segurança da comunicação do cliente de correio eletrônico com os servidores de correio 
eletrônico de entrada e de saída de mensagens, é importante configurar a utilização do padrão 
de segurança: 
 
a) TLS 
b) SMTP 
c) IMAP  
d) POP3 
e) HTTP 
 
7. (CESGRANRIO / Banco do Brasil - 2021) Apesar de os navegadores serem as ferramentas 
dominantes na internet, vários serviços possuem ferramentas próprias mais adequadas e, 
inclusive, mais otimizadas para protocolos específicos. Um desses protocolos foi desenvolvido 
para a transferência de arquivos, sendo usado a partir de programas como FileZilla. Esse 
protocolo é conhecido como: 
 
a) ftp 
b) imap 
c) pop3 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
75
80
==6306a==
d) ssh 
e) telnet 
 
8. (CESGRANRIO / Banco do Brasil - 2021) Sabendo que o banco em que trabalha vai colocar 
centenas de ATMs em shoppings e postos de gasolina, um funcionário de TI propôs que cada 
ATM mandasse periodicamente um sinal de status, por meio do protocolo UDP. Esse protocolo 
do conjunto TCP/IP é considerado como parte da camada: 
 
a) de aplicações 
b) de transporte 
c) de rede 
d) de enlace de dados 
e) física 
 
9. (CESGRANRIO / Banco do Brasil - 2021) Ao chegar para seu primeiro dia de emprego no banco, 
um novo gerente de TI percebeu que era demandado muito esforço no setor para controle do 
número IP de cada computador, o que causava, também, alguns erros por uso múltiplo do 
mesmo IP nas redes. 
 
Percebendo uma oportunidade de melhoria, o novo gerente decidiu que os computadores 
passariam a obter automaticamente um número IP, por meio do protocolo: 
 
a) DHCP 
b) DNS 
c) HTTP  
d) IMAP 
e) SMTP 
 
10. (IDIB / Ministério da Economia – 2021) Quando utilizamos a Internet é importante que nossos 
dados estejam seguros, de preferência criptografados. Existem alguns protocolos que são 
utilizados para os vários serviços da Internet e cada um deles faz uso de diferentes protocolos. 
Assinale a alternativa que apresenta um dos protocolos de comunicação que garante a 
comunicação segura através da Internet:  
 
a) TELNET 
b) SSL 
c) HTTP 
d) FTP 
e) IMAP 
 
11. (IDIB / Ministério da Economia – 2021) Dentre os vários protocolos utilizados na Internet, um 
pode ser considerado como principal, pois é o que permite a navegação nas páginas eletrônicas 
da Internet, permitindo a transferência de dados como hipertexto. Assinale a alternativa que 
identifica corretamente esse protocolo: 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
76
80
 
a) FTP 
b) SSL 
c) HTTP 
d) NMAP 
e) SMTP 
 
12. (CS-UFG / APARECIDAPREV – 2018) Há sites na Internet que são acessados por meio do 
protocolo HTTPS, como, por exemplo, o site https://cs.ufg.br. 
  
Qual é a função do HTTPS? 
 
a) Tornar mais rápida a navegação pelo site. 
b) Bloquear as janelas pop-up. 
c) Garantir que o navegador apresente uma única página por aba. 
d) Fazer com que os dados sejam transmitidos de forma criptografada. 
 
13.  (IADES / ARCON PA – 2018) [...] é um tipo de rede local que utiliza sinais de rádio para 
comunicação. 
 
CERT.br. Centro de Estudos, Resposta e Tratamento de Incidentes de 
Segurança no Brasil. Cartilha de Segurança para Internet. Disponível em: 
<https://cartilha.cert.br/livro/cartilha_segurança_internet.pdf>. 
Acesso em: 28 jun. 2018. 
 
A definição apresentada refere-se a: 
 
a) IP: Internet Protocol. 
b) DNS: Domain Name Server. 
c) SMTP: Simple Mail Transfer Protocol. 
d) URL: Universal Resource Locator. 
e) Wi-Fi: Wireless Fidelity. 
 
14. (IDECAN / IPC – 2018) Considerando os recursos que podem ser consumidos ou acessados na 
Internet, analise as seguintes informações. 
 
I. O FTP é o protocolo utilizado para a transferência de arquivos entre duas máquinas ligadas à 
Internet. 
 
II. Um correio eletrônico permite a troca de mensagens que um usuário de Internet pode fazer 
para outras pessoas conectados à Internet. 
 
III. O HTTP é o protocolo utilizado para controlar a comunicação entre o servidor de Internet e 
o browser ou navegador. 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
77
80
 
IV. O ICMP é o protocolo responsável por estabelecer a comunicação entre os computadores 
emissores e receptores de maneira na qual a informação não se perca na rede. 
 
De acordo com as afirmativas acima, marque a alternativa correta. 
 
a) Apenas as afirmativas I e II estão corretas. 
b) Apenas as afirmativas I, II e III estão corretas. 
c) Apenas as afirmativas II e III estão corretas. 
d) Apenas as afirmativas I, II e IV estão corretas. 
 
15.  (AOCP / ITEP-RN – 2018) Em relação à transferência de arquivos pela internet, assinale a 
alternativa correta. 
 
a) Quando uma pessoa envia um arquivo de seu computador para um site na internet, a 
operação de transferência que está sendo executada é conhecida como Download. 
 
b) FTP é um protocolo que pode ser utilizado para transferir arquivos entre computadores 
conectados à internet. 
 
c) Podemos considerar os termos Upload e Download como análogos, ou seja, possuem o 
mesmo significado. 
 
d) O protocolo FTP é utilizado exclusivamente para se realizar o acesso a websites na internet. 
 
e) O termo Upload se refere à velocidade na qual um computador conectado à internet consegue 
receber os dados de um website qualquer. 
 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
78
80
GABARITO – DIVERSAS BANCAS
1. 
LETRA C 
2. 
ERRADO 
3. 
LETRA C 
4. 
LETRA C 
5. 
LETRA D 
6. 
LETRA A 
7. 
LETRA A 
8. 
LETRA B 
9. 
LETRA A 
10. 
LETRA B 
11. 
LETRA C 
12. 
LETRA D 
13. 
LETRA E 
14. 
LETRA B 
15. 
LETRA B 
 
 
 
 
 
Diego Carvalho, Renato da Costa, Equipe Informática e TI
Aula 01
TJs - Curso Regular (Analista Judiciário - Área Administrativa) Informática
www.estrategiaconcursos.com.br
95298789153 - Sibeli Maria Linhares Santos
79
80
