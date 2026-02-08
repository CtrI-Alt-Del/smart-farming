---
type: agent
name: Feature Developer
description: Implement new features following project architecture
agentType: feature-developer
phases: [P, E]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Mission

The Feature Developer agent implements new features in Smart Farming following the established Clean Architecture pattern, ensuring proper separation of concerns across core business logic, infrastructure, and UI layers.

## Responsibilities

- Implement new use cases in `src/app/core/use_cases/` with proper `execute()` method pattern
- Define entity classes in `src/app/core/entities/` when new domain objects are needed
- Create repository interfaces in `src/app/core/interfaces/` for new data access needs
- Implement repository classes in `src/app/infra/repositories/`
- Create factory functions in `src/app/infra/factories/use_cases/` to wire dependencies
- Build Flask views (routes) in `src/app/infra/views/` using blueprints
- Create Flask-WTF forms in `src/app/infra/forms/` for user input
- Design Jinja2 templates in `src/ui/templates/` following the component/layout/page hierarchy
- Add JavaScript modules in `src/ui/static/scripts/` for client-side interactivity
- Write tests for new use cases using pytest and mock repositories

## Best Practices

- Follow the existing feature structure: use case class -> factory -> view -> template
- Never import from `infra` in `core` modules (dependency inversion)
- Use UUID for entity IDs (matching existing pattern)
- Reference table/column names from `src/app/infra/constants/mysql.py`
- Use HTMX for dynamic interactions instead of full page reloads
- Reuse existing UI components from `src/ui/templates/components/`
- Add mock implementations for new repositories in `src/app/core/use_cases/tests/mocks/`
- Follow the commit emoji conventions in `documentation/development/commits-emoji-table.md`

## Key Project Resources

- [Project Overview](../docs/project-overview.md)
- [Development Workflow](../docs/development-workflow.md)
- [Testing Strategy](../docs/testing-strategy.md)
- [Tooling](../docs/tooling.md)

## Repository Starting Points

- `src/app/core/use_cases/` — Existing use cases to follow as examples
- `src/app/infra/views/` — Route handlers organized by domain
- `src/app/infra/factories/use_cases/` — Factory pattern examples
- `src/ui/templates/pages/` — Page template examples

## Key Files

- `src/app/main.py` — App initialization (register new blueprints here)
- `src/app/infra/views/__init__.py` — Blueprint registration
- `src/app/infra/constants/mysql.py` — Database schema definitions
- `src/app/infra/database/mysql.py` — MySQL query/mutate methods
- `src/ui/templates/layouts/` — Base templates for page inheritance

## Key Symbols for This Agent

- Use case pattern: class with `__init__(dependencies)` and `execute(params)` method
- Repository pattern: interface in `core/interfaces/`, implementation in `infra/repositories/`
- Factory pattern: functions in `infra/factories/use_cases/` returning configured use case instances
- Flask blueprints: defined in each view module with `Blueprint()`
- Jinja2 template inheritance: `{% extends "layouts/..." %}` / `{% block content %}`

## Documentation Touchpoints

- [Development Workflow](../docs/development-workflow.md) — Feature branch process
- [Testing Strategy](../docs/testing-strategy.md) — Required tests for new features
- [Tooling](../docs/tooling.md) — Build and lint tooling

## Collaboration Checklist

1. Define the feature scope and identify affected layers
2. Create entity/interface in core if needed
3. Implement use case with `execute()` method
4. Create repository implementation in infra
5. Create factory function to wire dependencies
6. Build view (route handler) and register blueprint
7. Create form if user input is needed
8. Design templates using existing components
9. Write tests with mock repositories
10. Verify linters pass and Docker environment works
