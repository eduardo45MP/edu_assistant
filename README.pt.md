# edu_assistant

**edu_assistant** é um projeto conceitual e experimental que investiga a criação de um **assistente inteligente orientado por intenção**, projetado para atuar como uma camada contínua de suporte cognitivo e operacional entre humanos e sistemas computacionais.

Mais do que um chatbot, o edu_assistant explora a ideia de **simbiose funcional homem–máquina**, onde a linguagem natural se torna o principal meio de orquestração de ações, sistemas e decisões.

---

## Visão

O maior avanço recente da computação não foi apenas a evolução dos modelos de IA, mas a viabilidade prática da **tradução bidirecional entre linguagem humana e execução computacional**.

O edu_assistant parte da seguinte premissa:

> Humanos não precisam mais falar a linguagem das máquinas.  
> As máquinas agora conseguem interpretar, estruturar e executar intenções humanas.

Esse projeto explora essa mudança como base para uma nova classe de sistemas: 
**assistentes orientados por intenção, com controle humano explícito e execução auditável**.

---

## O que é o edu_assistant

O edu_assistant é concebido como um **orquestrador cognitivo**, capaz de:

- interpretar comandos em linguagem natural
- compreender intenção e contexto
- planejar ações de forma estruturada
- coordenar ferramentas, APIs e serviços externos
- executar ações com segurança, limites e autorização explícita

Ele **não é**:
- um chatbot tradicional
- um sistema autônomo irrestrito
- uma IA que substitui decisões humanas

Ele é um **mediador entre intenção humana e ação computacional**.

---

## Assis - a identidade do assistente

Dentro do projeto, o assistente assume uma identidade própria: **Assis**.

O nome remete tanto a *assistente* quanto a um sobrenome humano, reforçando:
- proximidade
- continuidade
- personalização
- interação natural

Assis é ativado de forma **explícita**, operando sempre dentro de limites claros de permissão e controle.

---

## Princípios fundamentais

O projeto é guiado por princípios claros:

- **Humano no controle por padrão**  
  Nenhuma ação sensível ocorre sem autorização explícita.

- **Intenção antes da execução**  
  Compreender o que deve ser feito é mais importante do que agir rapidamente.

- **Separação de responsabilidades**  
  Orquestração, execução, integração e interface evoluem de forma independente.

- **Transparência e rastreabilidade**  
  O sistema deve ser capaz de explicar o que foi feito, por quê e por qual componente.

- **Evolução incremental**  
  O sistema cresce em camadas, sem refatorações disruptivas.

---

## Visão arquitetural (alto nível)

O edu_assistant adota uma arquitetura **distribuída baseada em microservices**, organizada em camadas bem definidas:

- **Interface / Cliente**  
  Captura comandos (voz ou texto) e apresenta respostas.

- **Orquestrador (LLM Core)**  
  Interpreta intenção, gera planos e coordena ações.

- **Serviços de Execução (Tools)**  
  Executam ações concretas de forma segura e previsível.

- **Serviços de Integração (Connectors)**  
  Conectam sistemas externos e normalizam dados.

- **Memória e Contexto**  
  Gerenciam contexto de curto prazo e memória persistente (opt-in).

- **Políticas, Permissões e Segurança**  
  Controlam riscos, autorizações e limites de execução.

- **Auditoria e Observabilidade**  
  Garantem rastreabilidade, logs e transparência.

> O orquestrador **nunca executa ações diretamente**.  
> Execução e decisão são sempre separadas.

---

## Estrutura do repositório (resumo)

```text
edu_assistant/
├─ README.md
├─ README.pt-BR.md
├─ AGENTS.md
├─ docs/
│  ├─ en-GB/
│  └─ pt-BR/
├─ shared/
├─ services/
│  ├─ orchestrator/
│  ├─ interface-client/
│  ├─ memory/
│  ├─ policy-permissions/
│  ├─ audit-observability/
│  ├─ tools/
│  └─ connectors/
├─ infra/
├─ scripts/
└─ tests/
````

A documentação detalhada de visão, arquitetura, setup e roadmap está disponível em `docs/`.

---

## Casos de uso explorados

O projeto investiga, entre outros:

* gestão de agenda e compromissos
* busca e correlação em e-mails e mensagens autorizadas
* pesquisa técnica e científica
* automação de tarefas repetitivas
* redação assistida com aprovação humana
* recomendações contextuais
* integração com dispositivos vestíveis
* alertas e notificações inteligentes

Todas as ações são condicionadas a **permissão explícita**.

---

## Roadmap (visão resumida)

* **Fase 1:** núcleo funcional e comandos explícitos
* **Fase 2:** contexto e continuidade de interação
* **Fase 3:** expansão de ferramentas e automação
* **Fase 4:** interação multimodal e wearables
* **Fase 5:** agentes especializados coordenados
* **Fase 6:** exploração de longo prazo (opt-in)

O roadmap completo está documentado em `docs/pt-BR/roadmap.md`.

---

## Status do projeto

🚧 **Projeto em evolução ativa**
O edu_assistant é experimental, iterativo e conceitualmente ambicioso.
O foco atual é **validar arquitetura, padrões de interação e limites seguros** antes de avançar para automações mais profundas.

---

## Licença

Este projeto é distribuído sob a licença especificada no arquivo `LICENSE`.

---

## Autor

Criado e mantido por **Eduardo Peixoto**
CEO da **Innoforge.tech**

> O objetivo não é criar uma IA que substitua o humano,
> mas um sistema que **potencialize sua capacidade de decidir, agir e compreender**
> em um mundo digital cada vez mais complexo.