# Contexto: Gandalf Hardening (Narvi Principles)

## Objetivo
Evoluir o framework Gandalf injetando o rigor técnico e a disciplina de engenharia da skill "Narvi", mas de forma agnóstica (sem referências à Altave).

## Stakeholders
- Desenvolvedores que utilizam Gandalf para orquestrar agentes.
- Mantenedores do framework Gandalf.

## Problema
Gandalf possui uma filosofia sólida (Grey/White), mas carece de uma implementação tática de "Harness" (arreio) que garanta memória persistente, carregamento rápido de contexto e provas automatizadas de sucesso.

## Hipóteses de Melhoria
1. Se adicionarmos um "Wizard Probe" obrigatório, o agente errará menos por falta de contexto.
2. Se formalizarmos a "Fase de Contexto" antes da codificação, o desperdício de tokens e tempo com implementações erradas diminuirá.
3. Se fornecermos templates genéricos de "Wizard Harness", facilitaremos a adoção do método disciplinado.

## Métrica Alvo
- Todos os projetos Gandalf devem iniciar com um `wizard-bootstrap.sh` e `QUEST_PROGRESS.md`.
- 100% das tarefas não-triviais devem ter um `docs/contexto.md` validado.

## Não-Objetivos
- Não utilizar o nome "Altave" ou "Método Ancestral".
- Não alterar a metáfora "Grey/White/Wizard" original do Gandalf.
- Não reescrever o core do Gandalf, apenas estendê-lo.
