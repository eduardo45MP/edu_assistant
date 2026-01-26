# Casos de Uso - edu_assistant

Este documento descreve os **principais casos de uso explorados** pelo projeto **edu_assistant**.  
Os cenários aqui apresentados não representam funcionalidades finais garantidas, mas **direções de aplicação** que orientam decisões arquiteturais, técnicas e éticas do sistema.

Todos os casos de uso respeitam os princípios fundamentais do projeto:

- humano no controle por padrão  
- intenção explícita antes de execução  
- separação entre decisão, orquestração e ação  
- transparência e auditabilidade  

---

## 1. Gestão de agenda e compromissos

### Descrição
O assistente auxilia o usuário na criação, modificação e consulta de compromissos, sempre a partir de comandos em linguagem natural.

### Exemplos
- “Marca uma reunião amanhã às 14h com o time.”
- “Reagenda aquela reunião para sexta de manhã.”
- “O que eu tenho hoje à tarde?”

### Fluxo típico
1. Usuário expressa a intenção
2. Orquestrador interpreta e desambigua data/horário
3. Validação de permissões
4. Execução via ferramenta de calendário
5. Confirmação clara ao usuário

### Observações
- Ações de criação ou alteração exigem autorização explícita
- O sistema não assume contexto sensível sem confirmação

---

## 2. Continuidade de interação e contexto

### Descrição
O sistema mantém **contexto de curto prazo** para permitir interações naturais e contínuas, sem exigir repetição constante de informações.

### Exemplos
- “Reagenda aquela reunião.”
- “Continua a pesquisa que começámos antes.”
- “Resume isso.”

### Limites
- O contexto é temporário
- Não há persistência automática de memória
- Ambiguidades geram pedidos de esclarecimento

---

## 3. Pesquisa técnica e científica assistida

### Descrição
O assistente apoia pesquisas em fontes técnicas, científicas ou documentais autorizadas, atuando como **curador e sintetizador**, não como fonte primária.

### Exemplos
- “Pesquisa artigos recentes sobre LLM orchestration.”
- “Resume os pontos principais desse paper.”
- “Compara essas duas abordagens.”

### Capacidades
- busca em múltiplas fontes
- síntese estruturada
- comparação conceitual
- explicitação de fontes

---

## 4. Busca e correlação em comunicações autorizadas

### Descrição
O edu_assistant pode auxiliar na busca e organização de informações em e-mails, mensagens ou documentos, **desde que explicitamente autorizado**.

### Exemplos
- “Procura e-mails importantes de hoje.”
- “Tem alguma mensagem do João sobre o contrato?”
- “Resume os tópicos recorrentes dessa conversa.”

### Restrições
- acesso somente a fontes autorizadas
- nenhuma resposta automática sem aprovação
- logs e auditoria obrigatórios

---

## 5. Redação assistida (com aprovação humana)

### Descrição
O assistente auxilia na **redação de textos**, mas nunca envia comunicações externas sem validação humana.

### Exemplos
- “Rascunha uma resposta educada para esse e-mail.”
- “Escreve uma mensagem profissional confirmando a reunião.”

### Fluxo
1. Geração de rascunho
2. Apresentação ao usuário
3. Ajustes manuais (se desejado)
4. Aprovação explícita antes de qualquer envio

---

## 6. Automação de tarefas repetitivas

### Descrição
O sistema pode executar automações **limitadas, explícitas e revogáveis**, sempre dentro de escopos bem definidos.

### Exemplos
- “Toda sexta, resume meus compromissos da semana.”
- “Quando chegar um e-mail com esse assunto, me avisa.”

### Limites
- automações exigem consentimento explícito
- escopo claramente definido
- possibilidade de cancelamento a qualquer momento

---

## 7. Recomendações contextuais

### Descrição
O edu_assistant pode sugerir opções com base em contexto fornecido pelo usuário, sem assumir preferências implícitas.

### Exemplos
- “Sugere restaurantes próximos.”
- “Me dá opções de ferramentas para esse problema.”

### Princípio
Recomendação ≠ decisão.  
A escolha final é sempre do usuário.

---

## 8. Integração com dispositivos vestíveis (exploratório)

### Descrição
Exploração de interações discretas por meio de dispositivos vestíveis, como fones de condução óssea.

### Exemplos
- alertas contextuais
- lembretes pontuais
- respostas auditivas curtas

### Observação
Este caso de uso é **experimental** e depende de validações técnicas e éticas adicionais.

---

## 9. Alertas e notificações inteligentes

### Descrição
O assistente pode emitir alertas baseados em eventos, regras ou contexto previamente definidos.

### Exemplos
- “Me avisa se essa reunião atrasar.”
- “Notifica se houver mudanças nesse documento.”

### Limites
- alertas são opt-in
- nenhuma vigilância implícita
- regras claras e transparentes

---

## Fora de escopo (explicitamente)

O edu_assistant **não** se propõe a:

- agir como agente autônomo irrestrito
- tomar decisões estratégicas pelo usuário
- executar ações sensíveis sem autorização
- operar como sistema clínico, médico ou legal
- armazenar dados pessoais sem consentimento

---

## Nota final

Os casos de uso apresentados servem como **guia de intenção**, não como promessa de produto.

O objetivo do edu_assistant não é maximizar automação,  
mas **reduzir fricção entre intenção humana e ação computacional**,  
mantendo controle, clareza e responsabilidade.

Este documento deve evoluir junto com o projeto.