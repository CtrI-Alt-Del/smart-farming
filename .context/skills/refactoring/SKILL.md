---
type: skill
name: Refactoring
description: Safe code refactoring with step-by-step approach
skillSlug: refactoring
phases: [E]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Refactoring

## When to Use

Use this skill when restructuring existing code in the Smart Farming application. Refactoring must preserve behavior while improving code structure, readability, or maintainability.

## Safety Protocol

Before ANY refactoring:

1. **Run tests**: `pytest` — Establish the baseline (all tests must pass)
2. **Understand scope**: Identify all files affected by the change
3. **Make incremental changes**: One logical change at a time
4. **Re-run tests after each change**: Catch regressions immediately
5. **Commit after each safe step**: Easy to revert if needed

## Common Refactoring Patterns

### Extract Shared Logic to Commons

**When**: Two or more use cases contain duplicate logic.

**Where**: `src/app/core/commons/`

```python
# Before: duplicated in multiple use cases
class CreateSensorRecord:
    def execute(self, data):
        # validation logic here...
        
class EditSensorRecord:
    def execute(self, data):
        # same validation logic here...

# After: extracted to commons
# core/commons/validate_sensor_data.py
def validate_sensor_data(data):
    # shared validation logic

# Use in both use cases
from core.commons.validate_sensor_data import validate_sensor_data
```

### Split Large Use Case

**When**: A use case has too many responsibilities (> 100 lines or multiple distinct operations).

**Steps:**
1. Identify distinct operations within the use case
2. Create new use case classes for each operation
3. Update the factory function to wire new dependencies
4. Update the view to use the appropriate use case
5. Move/create tests for each new use case

### Consolidate Repository Methods

**When**: Multiple repository methods have similar SQL with minor variations.

```python
# Before: separate methods with similar queries
def find_by_plant_id(self, plant_id): ...
def find_by_date_range(self, start, end): ...
def find_by_plant_and_date(self, plant_id, start, end): ...

# After: flexible query method
def find(self, filters: dict): ...
```

### Rename for Clarity

**When**: Names don't clearly communicate intent.

**Checklist:**
- [ ] Update class/function name
- [ ] Update all imports
- [ ] Update factory functions
- [ ] Update test references
- [ ] Update mock class names if interface changed

### Move to Correct Layer

**When**: Code is in the wrong architectural layer.

| Code Type | Correct Location |
|-----------|-----------------|
| Business rules | `core/use_cases/` |
| Data validation | `core/commons/` or `infra/forms/` |
| SQL queries | `infra/repositories/` |
| HTTP handling | `infra/views/` |
| Configuration | `infra/constants/` |

## Refactoring Checklist

1. [ ] All tests pass BEFORE starting
2. [ ] Change is isolated to one concern
3. [ ] No architectural boundary violations introduced
4. [ ] Interfaces updated if contracts change
5. [ ] Factory functions updated if dependencies change
6. [ ] Mock repositories updated if interfaces change
7. [ ] All tests pass AFTER the change
8. [ ] No unused imports or dead code left behind
9. [ ] Commit with `:recycle: refactor(scope): description`

## Risky Refactors (Extra Caution)

- **Changing entity structure** — Affects repositories, use cases, views, templates, and tests
- **Changing database schema** — Requires SQL migration and may affect all layers
- **Renaming blueprints** — Affects URL routing and template links
- **Modifying `init_database()`** — Can destroy development data
