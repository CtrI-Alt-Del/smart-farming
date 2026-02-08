---
type: skill
name: Pr Review
description: Review pull requests against team standards and best practices
skillSlug: pr-review
phases: [R, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# PR Review

## When to Use

Use this skill when reviewing pull requests for the Smart Farming project. It provides a structured checklist tailored to the project's Clean Architecture, Flask stack, and coding conventions.

## PR Review Checklist

### Architecture Compliance

- [ ] Core layer (`src/app/core/`) does NOT import from infrastructure (`src/app/infra/`)
- [ ] Views only access use cases through factory functions, never instantiating repositories directly
- [ ] New use cases follow the class pattern with `__init__(dependencies)` and `execute(params)`
- [ ] Repository implementations are in `infra/repositories/`, not mixed into views or use cases
- [ ] Factory functions in `infra/factories/use_cases/` properly wire all dependencies

### Code Quality

- [ ] No hardcoded SQL table/column names — must use constants from `infra/constants/mysql.py`
- [ ] No hardcoded environment values — must use `os.getenv()` or `.env`
- [ ] No `print()` statements left in production code (remove debug statements)
- [ ] Python code passes Ruff linter (`ruff check .`)
- [ ] JavaScript code passes Biome linter (`npx biome check .`)
- [ ] No unused imports or variables

### Database & Security

- [ ] SQL queries use parameterized values (no string concatenation for user input)
- [ ] New database operations use `Mysql.query()` for reads and `Mysql.mutate()` / `mutate_many()` for writes
- [ ] Password handling uses Flask-Bcrypt (never plain text)
- [ ] Protected routes have `@login_required` decorator
- [ ] Form validation uses Flask-WTF validators

### UI & Templates

- [ ] Templates extend the correct layout (`layouts/root.html` or domain-specific)
- [ ] Reuses existing components from `templates/components/` where possible
- [ ] HTMX attributes are correct (hx-get, hx-post, hx-target, hx-swap)
- [ ] Responsive design considered (TailwindCSS responsive classes)
- [ ] No inline styles — use TailwindCSS utility classes

### Testing

- [ ] New use cases have corresponding tests in `core/use_cases/{domain}/tests/`
- [ ] Tests use mock repositories, not real database connections
- [ ] Tests cover both success and error paths
- [ ] All existing tests still pass (`pytest`)

### Commit Standards

- [ ] Commit messages follow the emoji convention in `documentation/development/commits-emoji-table.md`
- [ ] Commits are focused — one logical change per commit
- [ ] No `.env` files or secrets committed

## Review Response Template

```markdown
## Review Summary

**Status**: Approved / Changes Requested / Needs Discussion

### What's Good
- (positive observations)

### Issues Found
- [ ] (issue 1 — severity: high/medium/low)
- [ ] (issue 2)

### Suggestions
- (optional improvements)
```
