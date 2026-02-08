---
type: skill
name: Code Review
description: Review code quality, patterns, and best practices
skillSlug: code-review
phases: [R, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Code Review

## When to Use

Use this skill when reviewing code changes (not full PRs — for PR reviews, use the `pr-review` skill). This skill focuses on code-level quality, patterns, and adherence to project conventions.

## Review Dimensions

### 1. Clean Architecture Compliance

**Critical — these are hard rules:**

- `src/app/core/` must NEVER import from `src/app/infra/`
- Use cases only depend on interfaces, not concrete implementations
- Entities in `core/entities/` are pure data objects with no infrastructure dependencies
- Repository interfaces in `core/interfaces/` define contracts without implementation details

**Check for violations:**
```python
# BAD - core importing from infra
from infra.database.mysql import Mysql

# GOOD - core uses interface
from core.interfaces.plants_repository import PlantsRepository
```

### 2. Use Case Pattern

Every use case should follow this structure:

```python
class UseCaseName:
    def __init__(self, dependency1, dependency2):
        self.__dependency1 = dependency1
        self.__dependency2 = dependency2
    
    def execute(self, params):
        # Business logic here
        return result
```

**Check:**
- [ ] Uses double-underscore for private dependencies
- [ ] Has a single `execute()` method as entry point
- [ ] Business logic is in the use case, not in views or repositories

### 3. Repository Pattern

```python
# Interface (core/interfaces/)
class PlantsRepository:
    def find_all(self): ...
    def find_by_id(self, id): ...

# Implementation (infra/repositories/)
class PlantsRepositoryImpl(PlantsRepository):
    def __init__(self, database):
        self.__database = database
```

**Check:**
- [ ] Implementation follows the interface contract
- [ ] Uses parameterized queries (no SQL injection risk)
- [ ] References table/column names from `infra/constants/mysql.py`

### 4. View/Route Quality

**Check:**
- [ ] Uses factory to create use case
- [ ] Extracts parameters from request properly
- [ ] Returns appropriate response (template, redirect, error)
- [ ] Has `@login_required` where needed
- [ ] No business logic in the view

### 5. Template Quality

**Check:**
- [ ] Extends correct layout
- [ ] Uses `{{ form.hidden_tag() }}` for CSRF in forms
- [ ] HTMX attributes are correct
- [ ] No raw user data without escaping
- [ ] Uses TailwindCSS classes (no inline styles)

### 6. Testing Quality

**Check:**
- [ ] Tests use mocks, not real database
- [ ] BDD-style with `describe_` and descriptive names
- [ ] Covers happy path and error scenarios
- [ ] Fixtures properly set up and torn down

## Common Issues to Flag

1. **God use case** — Too many responsibilities; should be split
2. **Leaky abstraction** — Repository exposing SQL details to use case
3. **Missing error handling** — Use case not catching expected exceptions
4. **Hardcoded values** — Magic strings instead of constants
5. **Untested code** — New use case without tests
6. **Debug code** — `print()` statements or commented-out code left in
