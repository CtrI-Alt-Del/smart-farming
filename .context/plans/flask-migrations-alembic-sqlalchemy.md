# Adicionar migrations com Flask-Migrate (Alembic) e SQLAlchemy Plan

> Definir e implementar um fluxo de migrations versionadas no backend Flask com SQLAlchemy e Alembic, cobrindo configuracao, criacao de migracoes iniciais, integracao com ambiente local/CI e documentacao operacional.

## Task Snapshot
- **Primary goal:** Remover a inicializacao destrutiva de schema em runtime e adotar migrations versionadas com `Flask-Migrate` + `SQLAlchemy` para evolucao segura do banco.
- **Success signal:** Banco novo e banco existente conseguem seguir o mesmo fluxo com `flask db upgrade`, sem `DROP TABLE` na subida da aplicacao.
- **Key references:**
  - [Documentation Index](../docs/README.md)
  - [Agent Handbook](../agents/README.md)
  - [Plans Index](./README.md)

## Goal & Scope

### In Scope
1. Adicionar dependencias para migrations (`Flask-SQLAlchemy`, `Flask-Migrate`, `SQLAlchemy`, `alembic` quando necessario).
2. Criar bootstrap de banco no app factory para inicializar `db` e `migrate`.
3. Criar modelos SQLAlchemy equivalentes ao schema atual (`plants`, `sensors_records`, `checklist_records`, `user`) com constraints, FKs e defaults.
4. Gerar baseline de migration e definir procedimento para ambientes ja existentes (`stamp`/baseline sem perda de dados).
5. Substituir a rotina atual de recriacao de tabelas em `src/app/infra/database/__init__.py` por fluxo nao destrutivo.
6. Documentar comando operacional para evolucao de schema local e CI.

### Out of Scope
1. Reescrever todos os repositorios para ORM nesta entrega.
2. Redesenhar o modelo de dominio ou regras de negocio.
3. Refatorar jobs, providers e camada de views fora do necessario para bootstrap do banco.

## Current State (Codebase-Specific)
- O app inicializa banco em `src/app/main.py` via `init_database()`.
- `init_database()` em `src/app/infra/database/__init__.py` executa `DROP TABLE` + `CREATE TABLE` + inserts default, o que inviabiliza evolucao incremental.
- O schema atual esta centralizado em SQL string literal (`src/app/infra/constants/mysql.py`).
- A conexao atual usa `mysql-connector-python` em `src/app/infra/database/mysql.py`.
- Nao ha uso atual de `SQLAlchemy`/`Alembic` no codigo Python.

## Agent Lineup
| Agent | Role in this plan | Playbook | First responsibility focus |
| --- | --- | --- | --- |
| Feature Developer | Implementar bootstrap de SQLAlchemy/Alembic e baseline migration | [Feature Developer](../agents/feature-developer.md) | Criar `db`, `migrate`, modelos e primeira revisao de migration |
| Refactoring Specialist | Remover caminho destrutivo de init e adaptar pontos de acoplamento | [Refactoring Specialist](../agents/refactoring-specialist.md) | Isolar responsabilidade de setup versus seed de dados |
| Test Writer | Garantir cobertura para upgrade/downgrade e smoke de inicializacao | [Test Writer](../agents/test-writer.md) | Criar testes para migration em banco limpo e banco preexistente |
| Code Reviewer | Revisar riscos de schema, defaults e backward compatibility | [Code Reviewer](../agents/code-reviewer.md) | Validar consistencia entre schema legado e migration baseline |
| Bug Fixer | Tratar regressao em constraints/tipos (ENUM, FK, datetime) | [Bug Fixer](../agents/bug-fixer.md) | Atuar em erros de runtime apos upgrade/downgrade |
| Documentation Writer | Atualizar guias de operacao e troubleshooting | [Documentation Writer](../agents/documentation-writer.md) | Documentar fluxo `flask db` para dev e CI |
| Performance Optimizer | Revisar impacto de indices e queries apos migration | [Performance Optimizer](../agents/performance-optimizer.md) | Sinalizar necessidade de indices adicionais no baseline |

## Documentation Touchpoints
| Guide | File | Updates needed |
| --- | --- | --- |
| Project Overview | [project-overview.md](../docs/project-overview.md) | Atualizar secao de stack de dados: de SQL literal para migrations versionadas |
| Development Workflow | [development-workflow.md](../docs/development-workflow.md) | Adicionar fluxo de alteracao de schema (`revision`, `upgrade`, `downgrade`) |
| Testing Strategy | [testing-strategy.md](../docs/testing-strategy.md) | Definir testes obrigatorios para migration e baseline em CI |
| Tooling & Productivity Guide | [tooling.md](../docs/tooling.md) | Registrar comandos Flask CLI, variaveis de ambiente e troubleshooting |

## Success Criteria
1. `init_app()` nao executa mais recriacao destrutiva de tabelas na inicializacao.
2. Existe diretorio `migrations/` versionado com baseline funcional.
3. `flask db upgrade` cria o schema completo esperado em banco vazio.
4. Existe procedimento documentado para bancos existentes (baseline/stamp) sem perda de dados.
5. Testes automatizados passam com `npm run test` e incluem verificacao de caminho de migration.
6. Build e testes em fluxo local seguem verde com `npm run build && npm run test`.

## Risk Assessment

### Identified Risks
| Risk | Probability | Impact | Mitigation Strategy | Owner |
| --- | --- | --- | --- | --- |
| Divergencia entre schema SQL literal e modelos ORM | Medium | High | Fazer mapeamento campo-a-campo antes de gerar baseline; revisar diff Alembic manualmente | Feature Developer + Code Reviewer |
| Quebra em bancos ja populados | Medium | High | Definir estrategia oficial com `flask db stamp` e checklist pre-upgrade | Refactoring Specialist |
| Incompatibilidade MySQL para ENUM/defaults/UUID | Medium | Medium | Validar tipos dialect-specific no migration script e rodar smoke real contra MySQL | Bug Fixer |
| Seed default nao idempotente | Low | Medium | Separar seed em comando dedicado com upsert/verificacao de existencia | Feature Developer |

### Dependencies
- **Internal:** Disponibilidade da equipe para validar impacto nos repositorios SQL atuais.
- **External:** Dependencia de pacote `Flask-Migrate` e `Flask-SQLAlchemy` em versoes compativeis com Flask 3.x.
- **Technical:** Acesso a instancia MySQL local para validar `upgrade`/`downgrade` real.

### Assumptions
- O projeto continuara em MySQL como banco primario nesta entrega.
- O app pode operar em modo hibrido temporario (repositorios SQL manual + SQLAlchemy para metadata/migrations).
- A tabela `user` permanece com esse nome nesta fase (sem rename para `users`).

## Resource Estimation

### Time Allocation
| Phase | Estimated Effort | Calendar Time | Team Size |
| --- | --- | --- | --- |
| Phase 1 - Discovery & Design | 1.5 person-days | 1-2 days | 1-2 people |
| Phase 2 - Implementation | 3 person-days | 3-4 days | 2 people |
| Phase 3 - Validation & Handoff | 1.5 person-days | 1-2 days | 1-2 people |
| **Total** | **6 person-days** | **5-8 days** | **-** |

### Required Skills
- Flask app factory e extensoes.
- SQLAlchemy ORM/core mapping para MySQL.
- Alembic migration lifecycle (`revision`, `upgrade`, `downgrade`, `stamp`).
- Testes de integracao com banco.

### Resource Availability
- **Available:** Feature Developer, Test Writer, Code Reviewer (pool de agentes do projeto).
- **Blocked:** Nenhum bloqueio conhecido no momento.
- **Escalation:** Maintainer responsavel pelo backend Flask (definir nome no kickoff).

## Working Phases

### Phase 1 - Discovery & Alignment (PREVC: P)
**Objective:** consolidar estrategia tecnica sem risco de perda de dados.

**Steps**
1. Mapear schema atual em `src/app/infra/constants/mysql.py` para entidades SQLAlchemy equivalentes (owner: Feature Developer).
2. Definir estrategia de transicao para bancos existentes (`stamp head` vs baseline aplicada) com criterios de escolha (owner: Refactoring Specialist).
3. Levantar variaveis e entrypoint Flask para comandos de migration (`FLASK_APP`, app factory) (owner: Feature Developer).
4. Registrar decisoes e trade-offs no plano (owner: Documentation Writer).

**Deliverables**
- Documento de mapeamento tabela/coluna/default/constraint.
- Estrategia de baseline aprovada para ambiente novo e existente.

**Evidence of completion**
- Checklist de schema validado por reviewer.
- Decisao registrada em markdown com comandos aprovados.

**Commit Checkpoint**
- `chore(plan): alinhar estrategia de migrations com baseline`

### Phase 2 - Implementation & Iteration (PREVC: E)
**Objective:** colocar migrations para funcionar de ponta a ponta no projeto.

**Steps**
1. Adicionar dependencias no ambiente Python e atualizar lock/processo de instalacao (owner: Feature Developer).
2. Criar modulo de extensoes de banco (`db`, `migrate`) e inicializar no app factory (`src/app/main.py`) (owner: Feature Developer).
3. Criar modelos SQLAlchemy para as tabelas atuais mantendo nomes e constraints compativeis (owner: Feature Developer).
4. Inicializar Alembic e gerar migration baseline; revisar script para MySQL (owner: Feature Developer + Code Reviewer).
5. Desativar fluxo destrutivo de `init_database()` e mover seed default para comando explicito e idempotente (owner: Refactoring Specialist).
6. Ajustar bootstrap/test setup para suportar `flask db upgrade` nos ambientes de dev/test (owner: Test Writer).

**Deliverables**
- Codigo de bootstrap SQLAlchemy/Alembic.
- Diretorio `migrations/` com baseline revisada.
- Fluxo de seed separado do schema migration.

**Evidence of completion**
- Execucao local: `flask db upgrade` em banco limpo concluida.
- Execucao local: caminho para banco existente validado sem drop.

**Commit Checkpoint**
- `feat(database): adicionar SQLAlchemy e Flask-Migrate com migration baseline`

### Phase 3 - Validation & Handoff (PREVC: V)
**Objective:** garantir estabilidade operacional e transferir conhecimento para o time.

**Steps**
1. Rodar suite com build+tests (`npm run build && npm run test`) apos aplicar migrations (owner: Test Writer).
2. Validar ciclo `upgrade -> downgrade -> upgrade` em ambiente local controlado (owner: Bug Fixer).
3. Atualizar docs de workflow e troubleshooting de migration (owner: Documentation Writer).
4. Revisao final de consistencia e plano de rollback com evidencias anexadas (owner: Code Reviewer).

**Deliverables**
- Evidencias de execucao de migration e testes.
- Documentacao atualizada para rotina de schema changes.

**Evidence of completion**
- Logs/comandos registrados no PR.
- Docs publicadas nos arquivos de touchpoint.

**Commit Checkpoint**
- `docs(database): documentar operacao de migrations e validacao`

## Rollback Plan

### Rollback Triggers
- Falha de `upgrade` em ambiente homolog/producao.
- Erros de runtime por ausencia/inconsistencia de colunas apos deploy.
- Regressao critica em leitura/escrita de entidades principais.

### Rollback Procedures
#### Phase 1 Rollback
- Action: Descartar apenas alteracoes de planejamento.
- Data Impact: Nenhum.
- Estimated Time: < 1 hour.

#### Phase 2 Rollback
- Action: Reverter commits de bootstrap/migrations e restaurar path anterior temporariamente.
- Data Impact: Se `downgrade` nao for seguro para um caso especifico, congelar escrita e restaurar snapshot antes do deploy.
- Estimated Time: 2-4 hours.

#### Phase 3 Rollback
- Action: Reverter release de docs/comandos e executar playbook de incidente com versao anterior do app.
- Data Impact: Baixo, desde que backup pre-deploy esteja valido.
- Estimated Time: 1-2 hours.

### Post-Rollback Actions
1. Registrar causa raiz e migration que falhou.
2. Abrir correcao com teste de regressao obrigatorio.
3. Atualizar este plano com ajuste de estrategia (tipos, constraints ou baseline).

## Evidence & Follow-up
- Artefatos esperados no PR:
  - Diff de dependencias Python.
  - Novos arquivos de migration (incluindo baseline).
  - Captura de execucao dos comandos `flask db current`, `flask db upgrade`, `flask db downgrade`.
  - Resultado de `npm run build && npm run test`.
- Follow-up recomendado:
  1. Fase 2 futura para migrar repositorios SQL manuais para sessao SQLAlchemy.
  2. Adicionar validacao automatica de migration drift em CI.
