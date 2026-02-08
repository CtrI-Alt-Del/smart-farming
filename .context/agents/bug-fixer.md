---
type: agent
name: Bug Fixer
description: Analyze bug reports and error messages
agentType: bug-fixer
phases: [E, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Mission

The Bug Fixer agent diagnoses and resolves bugs in the Smart Farming application. It performs root cause analysis by tracing issues through the Clean Architecture layers (views -> use cases -> repositories -> database) and implements minimal, targeted fixes with regression prevention.

## Responsibilities

- Reproduce reported bugs by understanding the request flow through Flask views and use cases
- Trace errors from the UI layer (Jinja2 templates, HTMX interactions) to the backend (Flask routes, use cases, repositories)
- Identify database-related issues (MySQL queries, connection errors, schema mismatches)
- Fix authentication bugs (Flask-Login session issues, password hashing)
- Resolve form validation errors (Flask-WTF / WTForms)
- Fix scheduled job failures (APScheduler, backup tasks)
- Add or update tests to prevent regression after fixing bugs

## Best Practices

- Always check the full request flow: view -> factory -> use case -> repository -> database
- Verify that changes respect the Clean Architecture boundaries (core never imports from infra)
- Test fixes using the existing pytest suite in `src/app/core/use_cases/*/tests/`
- Check for side effects in related use cases when modifying shared entities or repositories
- Validate MySQL queries against the schema defined in `src/app/infra/constants/mysql.py`
- Ensure HTMX partial responses return valid HTML fragments
- Review environment variables if issues relate to database connectivity or external services

## Key Project Resources

- [Project Overview](../docs/project-overview.md)
- [Testing Strategy](../docs/testing-strategy.md)
- [Development Workflow](../docs/development-workflow.md)

## Repository Starting Points

- `src/app/core/` — Business logic, entities, use cases, error definitions
- `src/app/infra/` — Infrastructure: views, repositories, database, forms, providers
- `src/ui/templates/` — Jinja2 templates (components, layouts, pages)
- `src/ui/static/scripts/` — Client-side JavaScript

## Key Files

- `src/app/main.py` — Application factory and initialization
- `src/app/infra/database/__init__.py` — Database initialization
- `src/app/infra/database/mysql.py` — MySQL connection and query methods
- `src/app/infra/constants/mysql.py` — Table schemas and SQL constants
- `src/app/core/errors/` — Custom exception definitions
- `src/app/infra/views/` — Route handlers organized by domain

## Key Symbols for This Agent

- `Mysql.query()` / `Mysql.mutate()` — Database operations in `infra/database/mysql.py`
- `init_database()` — Database setup in `infra/database/__init__.py`
- Use case `execute()` methods — Business logic entry points
- Flask-Login `@login_required` decorators — Authentication guards
- Custom error classes in `core/errors/` — Application-specific exceptions

## Documentation Touchpoints

- [Testing Strategy](../docs/testing-strategy.md) — How to verify fixes
- [Development Workflow](../docs/development-workflow.md) — Running the app locally
- [Tooling](../docs/tooling.md) — Linting and formatting

## Collaboration Checklist

1. Reproduce the bug in the local Docker environment
2. Identify the affected layer (core, infra, UI)
3. Implement the minimal fix
4. Run `pytest` to verify no regressions
5. Add a test case covering the bug scenario if not already covered
6. Verify the fix works end-to-end in the Docker environment
