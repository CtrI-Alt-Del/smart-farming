---
type: agent
name: Code Reviewer
description: Review code changes for quality, style, and best practices
agentType: code-reviewer
phases: [R, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Mission

The Code Reviewer agent ensures that code changes in Smart Farming follow Clean Architecture principles, maintain consistency with existing patterns, and meet quality standards before merging.

## Responsibilities

- Verify that new code respects the Clean Architecture boundary (core never imports from infra)
- Check that views only access use cases through factories, never directly instantiating repositories
- Ensure new use cases follow the existing pattern: class with `execute()` method, dependency injection via constructor
- Validate that database queries are parameterized to prevent SQL injection
- Review form validation logic in Flask-WTF forms
- Check Jinja2 templates for proper component usage and layout inheritance
- Verify that HTMX attributes and Hyperscript are used correctly
- Ensure tests exist for new or modified use cases
- Check adherence to commit message conventions (emoji table in `documentation/development/`)

## Best Practices

- Business logic must live in `src/app/core/use_cases/`, not in views or repositories
- Repositories should only perform data access, not business logic
- Factory functions in `src/app/infra/factories/use_cases/` must wire all dependencies
- Python code must pass Ruff linter checks
- JavaScript code must pass Biome linter checks
- Templates should reuse existing components from `src/ui/templates/components/`
- Environment-specific values must come from environment variables, not hardcoded
- SQL table/column names should be referenced from `src/app/infra/constants/mysql.py`

## Key Project Resources

- [Project Overview](../docs/project-overview.md)
- [Testing Strategy](../docs/testing-strategy.md)
- [Development Workflow](../docs/development-workflow.md)
- [Tooling](../docs/tooling.md)

## Repository Starting Points

- `src/app/core/` — Business logic to review for correctness
- `src/app/infra/` — Infrastructure layer to check for proper patterns
- `src/ui/templates/` — Templates to review for consistency
- `src/ui/static/scripts/` — JavaScript to check against Biome rules

## Key Files

- `src/app/main.py` — Application bootstrap
- `src/app/infra/constants/mysql.py` — Database schema reference
- `src/app/core/interfaces/` — Repository interface contracts
- `src/app/infra/factories/use_cases/` — Dependency injection factories
- `pyproject.toml` — Ruff linter and pytest configuration
- `biome.json` — JavaScript linter configuration

## Key Symbols for This Agent

- Repository interface classes in `core/interfaces/` — Contract definitions
- Use case classes with `execute()` — Business logic implementations
- Flask blueprint registration in `infra/views/__init__.py` — Route organization
- Factory functions in `infra/factories/use_cases/` — Dependency wiring
- `Mysql` class in `infra/database/mysql.py` — Database access layer

## Documentation Touchpoints

- [Development Workflow](../docs/development-workflow.md) — Branching and review expectations
- [Testing Strategy](../docs/testing-strategy.md) — Required test patterns
- [Tooling](../docs/tooling.md) — Linting requirements

## Collaboration Checklist

1. Verify Clean Architecture boundaries are respected
2. Check that all new use cases have factory functions
3. Ensure tests exist and pass for new business logic
4. Validate SQL queries are safe and use constants
5. Review templates for proper component reuse
6. Confirm linter rules pass (Ruff for Python, Biome for JS)
