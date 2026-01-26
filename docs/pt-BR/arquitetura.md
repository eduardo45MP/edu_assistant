# Arquitetura

## Objetivo do documento

Este documento descreve a arquitetura de alto nível do **edu_assistant**, com foco na organização do sistema, nos principais componentes, nos limites entre responsabilidades e nos princípios que orientam as decisões arquiteturais ao longo do projeto.

O objetivo não é especificar implementações detalhadas, algoritmos internos ou configurações de infraestrutura em nível operacional, mas estabelecer uma visão clara e compartilhada de **como o sistema é estruturado** e **por que certas decisões são tomadas**.

Este documento **não descreve**:

* detalhes de implementação de cada serviço ou módulo
* escolhas definitivas de fornecedores, modelos ou APIs externas
* código, exemplos de uso ou contratos técnicos completos
* decisões de baixo nível que possam mudar com a evolução do projeto

Esses aspectos devem ser tratados em documentos específicos, especificações técnicas ou diretamente no código.

Ao longo do projeto, este documento deve evoluir de forma **incremental e consciente**, acompanhando:

* mudanças relevantes na arquitetura geral
* introdução ou remoção de serviços
* alterações significativas no estilo arquitetural
* amadurecimento do sistema e de seus requisitos

A arquitetura aqui descrita deve servir como **referência viva**, sendo atualizada sempre que decisões estruturais impactarem a forma como o sistema é compreendido, mantido ou expandido.

---

## Visão arquitetural geral

O **edu_assistant** atua como uma camada intermediária entre o usuário humano e o ecossistema digital, com a função principal de **traduzir intenção humana em ações computacionais coordenadas**.

O sistema não substitui o humano nem opera de forma autônoma por padrão. Seu papel é ampliar a capacidade do usuário de interagir com sistemas complexos, reduzir fricção operacional e organizar a execução de tarefas a partir de comandos expressos em linguagem natural.

A relação entre humano, orquestração e execução é explicitamente separada em três níveis:

* **Humano**: define objetivos, expressa intenções, autoriza ações sensíveis e mantém o controle final sobre decisões relevantes.
* **Orquestração**: interpreta a intenção humana, estrutura um plano de ação e coordena os componentes necessários para sua execução.
* **Execução**: realiza ações concretas por meio de serviços, ferramentas e integrações externas, sempre dentro de limites explícitos de permissão e segurança.

Essa separação garante que o raciocínio e o planejamento não estejam acoplados à execução direta, permitindo maior controle, auditabilidade e evolução independente dos componentes.

Os princípios de alto nível que orientam a arquitetura do edu_assistant são:

* **Humano no controle por padrão**: nenhuma ação relevante ocorre sem autorização explícita quando necessário.
* **Intenção antes de execução**: o sistema prioriza entender o que deve ser feito antes de agir.
* **Separação clara de responsabilidades**: orquestração, execução e interfaces evoluem de forma independente.
* **Transparência e rastreabilidade**: o sistema deve ser capaz de explicar o que foi feito, por quê e por qual componente.
* **Evolução incremental**: a arquitetura deve permitir crescimento e refinamento sem refatorações estruturais disruptivas.

---

## Estilo arquitetural

O **edu_assistant** adota um modelo **client–server distribuído**, baseado em **microservices**, desde sua concepção.

O sistema é organizado como um conjunto de serviços independentes, cada um responsável por um domínio funcional específico, comunicando-se por meio de interfaces bem definidas. Um serviço de orquestração atua como coordenador lógico, sem executar ações diretamente, delegando responsabilidades a serviços especializados.

### Justificativa da escolha

A adoção de microservices é motivada por características intrínsecas ao problema que o edu_assistant se propõe a resolver:

* O sistema é **naturalmente distribuído**, envolvendo múltiplas integrações externas, fontes de dados e tipos de execução.
* Diferentes domínios (orquestração, execução, voz, memória, integrações) possuem **ciclos de vida, custos e requisitos distintos**.
* O isolamento entre serviços reduz o impacto de falhas e facilita a aplicação de **políticas de segurança e permissões granulares**.
* A arquitetura favorece a evolução incremental, permitindo adicionar, remover ou substituir capacidades sem reestruturações profundas.
* Serviços especializados são mais adequados para a futura introdução de agentes com responsabilidades bem definidas.

Essa abordagem evita a concentração excessiva de responsabilidades e mantém o sistema alinhado à sua visão de longo prazo.

### Implicações dessa decisão

A escolha por microservices traz consequências arquiteturais explícitas, que são aceitas de forma consciente:

* Maior complexidade operacional em comparação a arquiteturas monolíticas.
* Necessidade de contratos claros, versionamento e governança entre serviços.
* Dependência de mecanismos de comunicação síncrona e assíncrona bem definidos.
* Maior atenção a observabilidade, rastreabilidade e tratamento de falhas.
* Maior esforço inicial de organização, compensado por flexibilidade e escalabilidade futuras.

Essas implicações são consideradas parte do custo necessário para sustentar um sistema distribuído, seguro e evolutivo ao longo do tempo.

---

## Visão lógica do sistema

A visão lógica do **edu_assistant** organiza o sistema em componentes com responsabilidades bem definidas, de forma a manter separação clara entre **interface**, **orquestração**, **execução**, **integrações**, **dados/memória** e **controle**.

A seguir estão os componentes principais, suas responsabilidades e os limites entre eles.

---

### Componentes principais

1. **Cliente / Interface**
2. **Orquestrador (LLM Core)**
3. **Serviços de Execução (Tools)**
4. **Serviços de Integração (Connectors)**
5. **Serviço de Contexto e Memória**
6. **Serviço de Políticas, Permissões e Segurança**
7. **Observabilidade e Auditoria**

---

### Responsabilidades de cada componente

#### 1) Cliente / Interface

Responsável por capturar a intenção do usuário e apresentar o resultado.

Responsabilidades:

* gatilho explícito de ativação
* entrada por texto e/ou voz (quando aplicável)
* apresentação de respostas (texto, áudio, notificações)
* exibição de confirmações quando necessário

---

#### 2) Orquestrador (LLM Core)

Responsável por interpretar intenção e coordenar a execução.

Responsabilidades:

* compreensão e desambiguação de intenção
* geração de plano de execução (passos + ferramentas)
* seleção de ferramentas e conectores apropriados
* produção de comandos estruturados para execução
* geração de explicações/trace do plano e do resultado

---

#### 3) Serviços de Execução (Tools)

Responsáveis por executar ações concretas com segurança e previsibilidade.

Responsabilidades:

* execução de ações idempotentes quando possível
* validação de inputs e outputs (schemas)
* aplicação de limites (timeouts, retries, rate limits)
* retorno de respostas padronizadas para o orquestrador
* registro/auditoria das ações realizadas

Exemplos:

* calendário (criar/alterar compromissos)
* automação (tarefas repetitivas)
* mensageria (rascunhos, respostas assistidas com aprovação)
* computação (cálculos, transformações)

---

#### 4) Serviços de Integração (Connectors)

Responsáveis por acessar sistemas externos e normalizar dados.

Responsabilidades:

* autenticação e autorização com plataformas externas
* coleta e normalização de dados
* controle de limites e políticas específicas do provedor
* entrega de dados ao sistema de forma consistente

Exemplos:

* e-mail
* documentos
* chats/mensagens (quando aplicável)
* busca na web e fontes públicas/privadas

---

#### 5) Serviço de Contexto e Memória

Responsável por armazenar e servir contexto de curto e longo prazo.

Responsabilidades:

* contexto de sessão (memória de curto prazo)
* memória persistente opt-in
* preferências e configurações do usuário
* mecanismos de limpeza, expiração e remoção
* suporte a recuperação (ex.: RAG) quando aplicável

---

#### 6) Serviço de Políticas, Permissões e Segurança

Responsável por controlar o que pode ou não ser executado.

Responsabilidades:

* classificação de risco por ação
* gates de permissão por ferramenta e por domínio
* exigência de aprovação humana em ações sensíveis
* aplicação de regras de privacidade e segurança
* bloqueios e limitações para evitar abuso

---

#### 7) Observabilidade e Auditoria

Responsável por rastreabilidade e transparência do sistema.

Responsabilidades:

* logs estruturados e rastreáveis
* trilha de auditoria de tool calls e resultados
* métricas de desempenho e qualidade
* suporte a debugging e inspeção de falhas
* geração de traces compreensíveis (quando habilitado)

---

### Limites claros entre os componentes

Para manter previsibilidade e segurança, os limites abaixo são considerados invariantes:

* **A interface não executa ações**: ela apenas captura intenção e apresenta resultados/autorizações.
* **O orquestrador não executa ações diretamente**: ele apenas interpreta, planeja e coordena.
* **Tools executam ações**: mas não decidem objetivos nem “inventam” intenções.
* **Connectors acessam dados externos**: mas não executam ações irreversíveis sem passar por políticas.
* **Memória não é implícita**: persistência exige controle e consentimento explícitos.
* **Permissões são transversais e obrigatórias**: nenhuma ação sensível bypassa a camada de políticas.
* **Auditoria é parte do sistema**: não é opcional quando há execução ou acesso a dados sensíveis.

Esses limites garantem que o sistema evolua de forma segura, modular e auditável, mesmo com aumento de complexidade ao longo do roadmap.

---

## Organização dos serviços

A arquitetura do **edu_assistant** é organizada como um conjunto de serviços independentes, cada um responsável por um domínio funcional específico. Essa organização reforça a separação entre **intenção**, **orquestração**, **execução**, **integração**, **persistência** e **controle**, permitindo evolução e escalabilidade por domínio.

---

### Serviço de interface / cliente

Responsável por toda interação direta com o usuário.

Funções principais:

* capturar comandos e intenções do usuário (texto ou voz)
* gerenciar gatilhos explícitos de ativação
* apresentar respostas, confirmações e notificações
* encaminhar solicitações para o serviço de orquestração

Características:

* não executa ações nem acessa sistemas externos
* pode existir em múltiplas formas (CLI, app local, wearable, web)
* mantém estado mínimo, focado na experiência do usuário

---

### Serviço de orquestração (LLM core)

Responsável por interpretar intenção humana e coordenar o sistema.

Funções principais:

* interpretar e desambiguar comandos em linguagem natural
* gerar planos de ação estruturados
* selecionar serviços de execução e integração adequados
* solicitar validação de permissões quando necessário
* consolidar resultados e produzir respostas explicáveis

Características:

* não executa ações diretamente
* não acessa sistemas externos sem intermediação
* atua como coordenador lógico do sistema
* centraliza raciocínio, não efeitos colaterais

---

### Serviços de execução (tools)

Responsáveis por executar ações concretas e controladas.

Funções principais:

* executar operações específicas (ex.: criar evento, enviar mensagem, rodar automação)
* validar schemas de entrada e saída
* aplicar limites de execução (timeout, retries, rate limit)
* registrar ações para auditoria

Características:

* cada serviço é especializado em um domínio de ação
* executa apenas o que foi explicitamente solicitado
* não interpreta intenção nem decide objetivos
* desenhado para ser idempotente sempre que possível

---

### Serviços de integração (connectors)

Responsáveis por comunicação com sistemas e plataformas externas.

Funções principais:

* autenticar e autorizar acesso a serviços externos
* coletar, transformar e normalizar dados
* aplicar políticas e limites específicos de cada provedor
* fornecer dados de forma consistente aos demais serviços

Características:

* isolam dependências externas
* não executam ações irreversíveis sem passar por políticas
* facilitam substituição ou remoção de integrações
* reduzem impacto de mudanças em APIs externas

---

### Serviços de memória

Responsáveis por armazenar e fornecer contexto ao longo do tempo.

Funções principais:

* manter memória de sessão (curto prazo)
* armazenar memória persistente com consentimento explícito
* gerenciar preferências e configurações do usuário
* fornecer mecanismos de consulta, limpeza e remoção

Características:

* nenhum dado é armazenado sem autorização
* memória é sempre auditável e controlável pelo usuário
* projetado para evoluir incrementalmente (curto → longo prazo)

---

### Serviços transversais (políticas, segurança, auditoria)

Responsáveis por garantir operação segura e controlada do sistema.

Funções principais:

* avaliar risco e permissões por ação ou serviço
* exigir aprovação humana para ações sensíveis
* aplicar regras de privacidade e uso
* manter trilhas completas de auditoria
* fornecer visibilidade e rastreabilidade do sistema

Características:

* serviços obrigatórios, não opcionais
* aplicados de forma consistente a todos os fluxos
* independentes da lógica de negócio
* fundamentais para confiança e escalabilidade do sistema

---

Essa organização de serviços estabelece limites claros e reforça a ideia central do edu_assistant: **orquestrar intenção humana com execução segura, controlada e auditável**, sem acoplamentos indevidos entre responsabilidades.

---

## Comunicação entre serviços

A comunicação entre os serviços do **edu_assistant** é baseada em contratos explícitos e padrões bem definidos, de forma a garantir previsibilidade, isolamento de falhas e evolução independente dos componentes.

O sistema combina comunicação **síncrona** e **assíncrona**, escolhidas de acordo com o tipo de interação, latência esperada e impacto operacional.

---

### Padrões de comunicação síncrona

A comunicação síncrona é utilizada quando há necessidade de resposta imediata ou interação direta com o usuário.

Casos típicos:

* interface → orquestrador
* orquestrador → serviços de políticas/permissões
* orquestrador → serviços de consulta de dados
* recuperação de contexto para planejamento

Características:

* baseada em APIs HTTP/REST
* payloads estruturados e validados por schema
* timeouts explícitos e curtos
* respostas determinísticas, sem efeitos colaterais ocultos

Regra:

> Comunicação síncrona **não deve** disparar ações irreversíveis sem passar por validação de permissões.

---

### Padrões de comunicação assíncrona

A comunicação assíncrona é utilizada para execução de ações, automações e tarefas que podem ocorrer fora do fluxo imediato de interação.

Casos típicos:

* execução de ferramentas
* automações e workflows
* tarefas de longa duração
* coleta e processamento de dados externos

Características:

* baseada em filas ou eventos
* desacoplamento entre orquestração e execução
* suporte a retries e backoff
* tolerância a latência e falhas temporárias

Regra:

> Toda execução assíncrona deve ser rastreável e correlacionada a uma intenção e autorização explícitas.

---

### Contratos e versionamento

A comunicação entre serviços é regida por contratos explícitos.

Diretrizes:

* cada serviço expõe contratos claros de entrada e saída
* schemas são versionados de forma explícita
* mudanças incompatíveis exigem nova versão de contrato
* versionamento é preferencialmente semântico

Boas práticas:

* evitar dependência implícita de comportamento
* documentar contratos junto ao código
* manter compatibilidade retroativa sempre que possível

---

### Tratamento de falhas

Falhas são tratadas como parte esperada do sistema distribuído.

Princípios adotados:

* falhas devem ser isoladas e não propagadas em cascata
* timeouts e circuit breakers devem ser explícitos
* retries devem ser controlados e idempotentes
* falhas devem ser visíveis e auditáveis

Comportamento esperado:

* erros de serviços externos não devem comprometer o núcleo de orquestração
* o sistema deve retornar respostas compreensíveis ao usuário quando apropriado
* estados intermediários devem ser consistentes e recuperáveis

O tratamento de falhas é considerado parte integrante da arquitetura e essencial para manter confiabilidade e previsibilidade à medida que o sistema evolui.

---

## Modelo de execução

O modelo de execução do **edu_assistant** descreve como uma solicitação percorre o sistema desde a expressão da intenção pelo usuário até a execução das ações e o retorno dos resultados. Esse modelo enfatiza **controle explícito**, **decisão consciente** e **transparência**.

---

### Fluxo de uma solicitação típica

Uma solicitação segue, de forma geral, as seguintes etapas:

1. **Ativação**
   O usuário aciona explicitamente o sistema por meio da interface (comando, toque, palavra-chave).

2. **Captura da intenção**
   A interface coleta a entrada do usuário em texto ou voz.

3. **Pré-processamento**
   Caso a entrada seja por voz, ocorre a transcrição para texto antes do envio ao orquestrador.

4. **Interpretação**
   O serviço de orquestração analisa a entrada, interpreta a intenção e identifica possíveis ações.

5. **Planejamento**
   O orquestrador gera um plano estruturado contendo os passos necessários, serviços envolvidos e parâmetros.

6. **Validação de políticas**
   O plano é avaliado pelo serviço de políticas e permissões para identificar riscos e exigências de autorização.

7. **Autorização humana**
   Quando necessário, o usuário é solicitado a confirmar ou negar ações sensíveis.

8. **Execução**
   Após validação e autorização, o plano é executado pelos serviços apropriados, de forma síncrona ou assíncrona.

9. **Agregação de resultados**
   Os resultados das execuções são coletados e normalizados.

10. **Resposta ao usuário**
    O sistema apresenta o resultado final por meio da interface.

11. **Registro de contexto**
    O contexto relevante é armazenado como memória de sessão ou persistente, quando autorizado.

---

### Pontos de decisão

Durante o fluxo de execução, o sistema realiza decisões explícitas, como:

* interpretação e desambiguação da intenção
* escolha entre múltiplos planos possíveis
* definição de ferramentas e serviços a serem utilizados
* escolha entre execução síncrona ou assíncrona
* avaliação de risco associada às ações propostas

Essas decisões são centralizadas no serviço de orquestração e validadas pelas camadas de controle quando necessário.

---

### Pontos de autorização humana

O sistema exige autorização humana explícita em situações como:

* execução de ações irreversíveis
* envio de mensagens ou comunicações externas
* publicação de conteúdo em plataformas externas
* acesso ou modificação de dados sensíveis
* automações recorrentes ou de longo prazo

A autorização deve ser clara, contextualizada e compreensível, permitindo ao usuário entender **o que será feito e por quê**.

---

### Retorno de resultados e traces

O retorno ao usuário inclui:

* o resultado principal da solicitação
* mensagens de confirmação ou erro, quando aplicável
* explicações resumidas das ações executadas (trace)

Os traces, quando habilitados, devem:

* descrever os passos executados em linguagem compreensível
* indicar quais serviços foram acionados
* registrar decisões relevantes tomadas pelo sistema

Esse mecanismo garante transparência, facilita auditoria e fortalece a confiança do usuário no funcionamento do sistema.

---

## Dados, contexto e memória

O **edu_assistant** manipula dados em diferentes níveis de duração e sensibilidade. A arquitetura trata **dados, contexto e memória** como conceitos distintos, com regras claras de uso, persistência e controle, evitando acúmulo implícito ou opaco de informações sobre o usuário.

---

### Tipos de dados manipulados

O sistema lida principalmente com os seguintes tipos de dados:

* **Dados de entrada**: comandos em texto ou voz fornecidos pelo usuário.
* **Dados de contexto**: informações temporárias necessárias para interpretar e continuar uma interação.
* **Dados operacionais**: parâmetros, resultados e estados intermediários de execução de ferramentas.
* **Dados de integração**: informações provenientes de sistemas externos autorizados.
* **Dados de memória**: informações armazenadas com o objetivo de melhorar interações futuras.
* **Dados de auditoria**: registros técnicos de ações, decisões e acessos.

Cada tipo de dado possui regras específicas de retenção, visibilidade e acesso.

---

### Contexto de curto prazo

O contexto de curto prazo representa o estado temporário de uma interação ou sessão.

Características:

* limitado à duração de uma sessão ou fluxo específico
* utilizado para manter continuidade entre comandos relacionados
* descartado automaticamente ao final da sessão, salvo autorização explícita

Exemplos:

* referência a ações recém-executadas
* resolução de pronomes e comandos implícitos (“isso”, “aquilo”)
* continuação de uma tarefa iniciada anteriormente

O contexto de curto prazo não é considerado memória persistente.

---

### Persistência de longo prazo

A persistência de longo prazo é opcional e depende de consentimento explícito do usuário.

Características:

* armazena informações relevantes para personalização ou eficiência futura
* pode incluir preferências, padrões recorrentes ou dados aprovados
* é sempre associada a uma finalidade clara

Restrições:

* nenhum dado é persistido sem autorização
* dados persistidos devem ser editáveis e removíveis
* o sistema deve ser capaz de explicar por que determinado dado foi armazenado

---

### Controle e transparência para o usuário

O usuário mantém controle total sobre seus dados e memória.

Princípios adotados:

* visibilidade sobre o que está sendo armazenado
* possibilidade de revisar, editar ou excluir dados persistidos
* distinção clara entre contexto temporário e memória de longo prazo
* explicações compreensíveis sobre o uso de dados em decisões do sistema

A transparência no uso de dados é considerada fundamental para a confiança e para a evolução responsável do edu_assistant.

---

## Segurança, permissões e controle

A segurança no **edu_assistant** é tratada como um elemento estrutural da arquitetura, não como uma camada acessória. O sistema é projetado para operar com **controle explícito**, **privilégios mínimos** e **rastreabilidade completa**, preservando a autonomia do usuário e reduzindo riscos operacionais.

---

### Modelo de permissões

O modelo de permissões é baseado em **autorizações explícitas por ação e por domínio**.

Características:

* permissões são concedidas por tipo de ação, não de forma genérica
* serviços e ferramentas operam com privilégios mínimos
* permissões podem ser temporárias, revogáveis ou condicionais
* nenhuma ação assume autorização implícita

O sistema avalia permissões em tempo de execução, considerando contexto, risco e intenção declarada.

---

### Ações sensíveis

Ações sensíveis são aquelas que podem gerar efeitos irreversíveis, exposição de dados ou impacto externo significativo.

Exemplos:

* envio de mensagens ou comunicações externas
* publicação de conteúdo em plataformas externas
* modificações permanentes em dados do usuário
* automações recorrentes ou de longo prazo
* acesso a informações pessoais ou confidenciais

Essas ações exigem validações adicionais e, em geral, confirmação explícita do usuário antes da execução.

---

### Humano no controle

O **humano no controle** é um princípio central do sistema.

Diretrizes:

* o sistema nunca executa ações sensíveis sem autorização humana
* o usuário pode interromper, cancelar ou negar execuções em andamento
* decisões críticas são sempre comunicadas de forma clara
* a autonomia do sistema é limitada e contextual

Mesmo quando automações são permitidas, elas operam dentro de limites previamente definidos e revogáveis.

---

### Auditoria e rastreabilidade

Todas as ações relevantes do sistema são auditáveis.

Características:

* registro estruturado de intenções, decisões e execuções
* associação entre intenção, autorização e ação executada
* trilhas de auditoria acessíveis para inspeção
* rastreabilidade entre serviços envolvidos em uma solicitação

A auditoria garante transparência, facilita diagnóstico de falhas e reforça a confiança do usuário no funcionamento do edu_assistant.

---

## Stack tecnológica

A stack tecnológica do **edu_assistant** é definida com foco em **interoperabilidade**, **evolução incremental** e **adequação a um sistema distribuído**, evitando dependências excessivamente rígidas. As escolhas descritas a seguir representam uma direção inicial e podem evoluir conforme o projeto amadurece.

---

### Linguagens

* **Python**
  Linguagem principal do sistema, utilizada pela maturidade do ecossistema para IA, automação, integração com APIs e desenvolvimento rápido de serviços.

* **Outras linguagens (quando necessário)**
  Serviços específicos podem ser implementados em outras linguagens, caso requisitos de desempenho, latência ou integração justifiquem, desde que respeitem os contratos definidos.

---

### Frameworks

* **APIs e serviços**
  Frameworks web leves para construção de APIs HTTP, com suporte a validação de schemas, versionamento e documentação.

* **Orquestração e IA**
  Bibliotecas e SDKs para integração com modelos de linguagem, mecanismos de recuperação de contexto e coordenação de ferramentas.

* **Mensageria e execução assíncrona**
  Ferramentas para filas, eventos e processamento assíncrono, adequadas a sistemas distribuídos.

As escolhas específicas de frameworks devem privilegiar simplicidade, clareza e ampla adoção.

---

### Protocolos

* **HTTP/REST**
  Protocolo principal para comunicação síncrona entre serviços.

* **Mensageria baseada em filas ou eventos**
  Utilizada para execução assíncrona, automações e tarefas de longa duração.

* **Protocolos de autenticação e autorização**
  Empregados para controle de acesso entre serviços e integrações externas.

A comunicação entre serviços deve ser sempre explícita, autenticada e versionada.

---

### Infraestrutura (nível conceitual)

A infraestrutura é pensada para suportar um sistema distribuído de forma gradual.

Conceitos adotados:

* serviços executando de forma independente
* isolamento de componentes críticos
* capacidade de escalar por domínio funcional
* uso de containers para padronização de execução
* separação entre ambientes de desenvolvimento, teste e produção

A orquestração de infraestrutura e o grau de automação devem evoluir conforme a complexidade e o uso do sistema aumentem.

---

## Estratégia de evolução

A estratégia de evolução do **edu_assistant** prioriza crescimento contínuo e controlado, evitando rupturas arquiteturais e garantindo que o sistema permaneça utilizável e compreensível ao longo do tempo.

---

### Crescimento incremental

O sistema deve evoluir em pequenas etapas, sempre entregando valor funcional antes de adicionar novas camadas de complexidade.

Diretrizes:

* novas capacidades são introduzidas como serviços ou extensões isoladas
* funcionalidades experimentais não comprometem o núcleo existente
* cada evolução deve ser validável de forma independente
* o sistema deve ser utilizável em todos os estágios de maturidade

Esse modelo permite aprendizado contínuo e ajustes de direção sem necessidade de reestruturações profundas.

---

### Isolamento de mudanças

Mudanças devem ser isoladas ao máximo para reduzir impacto e risco.

Princípios:

* serviços possuem responsabilidades bem definidas
* alterações em um serviço não devem exigir mudanças em outros
* dependências externas são encapsuladas por conectores
* contratos explícitos reduzem acoplamento implícito

O isolamento facilita manutenção, testes e substituição de componentes ao longo do tempo.

---

### Compatibilidade entre versões

A compatibilidade é tratada como requisito arquitetural.

Práticas adotadas:

* versionamento explícito de APIs e contratos
* manutenção de compatibilidade retroativa sempre que possível
* introdução de novas versões sem quebra imediata das anteriores
* descontinuação planejada e documentada de versões antigas

Essas práticas garantem que o sistema possa evoluir sem interromper fluxos existentes e sem gerar dependências frágeis.

---

## Fora de escopo arquitetural

Este documento define explicitamente limites para evitar decisões prematuras ou expectativas incorretas sobre o escopo do **edu_assistant**.

### Decisões explicitamente excluídas

As seguintes decisões **não** fazem parte do escopo arquitetural atual:

* definição de um produto comercial final ou modelo de negócio
* promessas de autonomia total do sistema
* implementação de implantes, próteses ou interfaces invasivas
* garantias de uso clínico, médico ou legal
* otimizações extremas de desempenho em detrimento de clareza e segurança
* dependência obrigatória de um fornecedor específico de IA ou infraestrutura

Essas decisões podem ser revisitadas no futuro, mas não orientam a arquitetura neste momento.

---

### Limites conscientes do sistema

O edu_assistant reconhece limites arquiteturais deliberados:

* o sistema atua como **orquestrador**, não como agente autônomo irrestrito
* decisões críticas permanecem sob controle humano
* persistência de dados é limitada e opt-in
* o sistema prioriza previsibilidade e auditabilidade sobre “mágica”
* a arquitetura evita acoplamentos que dificultem evolução ou inspeção

Esses limites são considerados fundamentais para manter o projeto sustentável e responsável.

---

## Princípios arquiteturais

Os princípios a seguir orientam decisões presentes e futuras no **edu_assistant**.

### Princípios que guiam decisões

* **Humano no controle por padrão**
* **Intenção antes de execução**
* **Separação clara de responsabilidades**
* **Contratos explícitos entre serviços**
* **Transparência e rastreabilidade**
* **Evolução incremental e consciente**

---

### Trade-offs aceitos

O projeto aceita conscientemente os seguintes trade-offs:

* maior complexidade operacional em troca de modularidade e isolamento
* menor velocidade inicial de desenvolvimento em favor de escalabilidade futura
* custos adicionais de observabilidade e segurança para garantir confiança
* decisões explícitas e verificáveis em vez de automações opacas

Esses trade-offs refletem a prioridade por um sistema confiável e evolutivo.

---

### Critérios para mudanças futuras

Mudanças arquiteturais devem ser avaliadas com base em:

* impacto na segurança e no controle do usuário
* preservação da separação entre intenção, orquestração e execução
* compatibilidade com contratos existentes
* clareza e auditabilidade do sistema resultante
* benefícios concretos frente à complexidade introduzida

Qualquer alteração significativa deve ser documentada e refletida neste documento, mantendo a arquitetura como uma referência viva do projeto.

## Árvore Sugerida Para o projeto
    edu_assistant/
    ├─ README.md
    ├─ README.pt.md
    ├─ AGENTS.md
    ├─ LICENSE
    ├─ .gitignore
    ├─ .env.example
    ├─ docker-compose.yml
    ├─ docs/
    │  ├─ en-GB/
    │  │  ├─ README.md
    │  │  ├─ vision.md
    │  │  ├─ architecture.md
    │  │  ├─ setup.md
    │  │  ├─ use-cases.md
    │  │  └─ roadmap.md
    │  └─ pt-BR/
    │     ├─ README.md
    │     ├─ visao.md
    │     ├─ arquitetura.md
    │     ├─ setup.md
    │     ├─ casos-de-uso.md
    │     └─ roadmap.md
    │
    ├─ shared/
    │  ├─ contracts/
    │  │  ├─ openapi/
    │  │  ├─ schemas/
    │  │  └─ versions.md
    │  ├─ libs/
    │  │  ├─ logging/
    │  │  ├─ tracing/
    │  │  ├─ auth/
    │  │  ├─ errors/
    │  │  └─ utils/
    │  └─ README.md
    │
    ├─ services/
    │  ├─ interface-client/
    │  │  ├─ src/
    │  │  ├─ tests/
    │  │  ├─ Dockerfile
    │  │  └─ pyproject.toml
    │  │
    │  ├─ orchestrator/
    │  │  ├─ src/
    │  │  │  ├─ api/
    │  │  │  ├─ planner/
    │  │  │  ├─ prompts/
    │  │  │  ├─ tool_selection/
    │  │  │  └─ trace/
    │  │  ├─ tests/
    │  │  ├─ Dockerfile
    │  │  └─ pyproject.toml
    │  │
    │  ├─ policy-permissions/
    │  │  ├─ src/
    │  │  │  ├─ api/
    │  │  │  ├─ risk/
    │  │  │  ├─ rules/
    │  │  │  └─ approvals/
    │  │  ├─ tests/
    │  │  ├─ Dockerfile
    │  │  └─ pyproject.toml
    │  │
    │  ├─ memory/
    │  │  ├─ src/
    │  │  │  ├─ api/
    │  │  │  ├─ session/
    │  │  │  ├─ persistent/
    │  │  │  └─ rag/
    │  │  ├─ tests/
    │  │  ├─ Dockerfile
    │  │  └─ pyproject.toml
    │  │
    │  ├─ audit-observability/
    │  │  ├─ src/
    │  │  │  ├─ api/
    │  │  │  ├─ audit_log/
    │  │  │  ├─ metrics/
    │  │  │  └─ correlation/
    │  │  ├─ tests/
    │  │  ├─ Dockerfile
    │  │  └─ pyproject.toml
    │  │
    │  ├─ tools/
    │  │  ├─ tool-calendar/
    │  │  │  ├─ src/
    │  │  │  ├─ tests/
    │  │  │  ├─ Dockerfile
    │  │  │  └─ pyproject.toml
    │  │  ├─ tool-messaging/
    │  │  │  ├─ src/
    │  │  │  ├─ tests/
    │  │  │  ├─ Dockerfile
    │  │  │  └─ pyproject.toml
    │  │  ├─ tool-automation/
    │  │  │  ├─ src/
    │  │  │  ├─ tests/
    │  │  │  ├─ Dockerfile
    │  │  │  └─ pyproject.toml
    │  │  └─ tool-computation/
    │  │     ├─ src/
    │  │     ├─ tests/
    │  │     ├─ Dockerfile
    │  │     └─ pyproject.toml
    │  │
    │  ├─ connectors/
    │  │  ├─ connector-email/
    │  │  │  ├─ src/
    │  │  │  ├─ tests/
    │  │  │  ├─ Dockerfile
    │  │  │  └─ pyproject.toml
    │  │  ├─ connector-docs/
    │  │  │  ├─ src/
    │  │  │  ├─ tests/
    │  │  │  ├─ Dockerfile
    │  │  │  └─ pyproject.toml
    │  │  └─ connector-web-search/
    │  │     ├─ src/
    │  │     ├─ tests/
    │  │     ├─ Dockerfile
    │  │     └─ pyproject.toml
    │  │
    │  └─ speech/
    │     ├─ stt/
    │     │  ├─ src/
    │     │  ├─ tests/
    │     │  ├─ Dockerfile
    │     │  └─ pyproject.toml
    │     └─ tts/
    │        ├─ src/
    │        ├─ tests/
    │        ├─ Dockerfile
    │        └─ pyproject.toml
    │
    ├─ infra/
    │  ├─ docker/
    │  ├─ k8s/
    │  ├─ observability/
    │  └─ README.md
    │
    ├─ scripts/
    │  ├─ dev_up.sh
    │  ├─ dev_down.sh
    │  ├─ lint.sh
    │  ├─ test.sh
    │  └─ format.sh
    │
    └─ tests/
    ├─ integration/
    └─ e2e/
