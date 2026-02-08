---
type: skill
name: Test Generation
description: Generate comprehensive test cases for code
skillSlug: test-generation
phases: [E, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Test Generation

## When to Use

Use this skill when writing tests for Smart Farming use cases, utilities, or entities. The project uses pytest with pytest-describe for BDD-style structure and mock repositories for isolation.

## Test File Structure

### Location

- Use case tests: `src/app/core/use_cases/{domain}/tests/{use_case_name}_test.py`
- Common utility tests: `src/app/core/commons/tests/{utility_name}_test.py`
- Mocks: `src/app/core/use_cases/tests/mocks/`

### Template

```python
import pytest
from core.use_cases.{domain}.{use_case_name} import {UseCaseClass}
from core.use_cases.tests.mocks.repositories import Mock{Domain}Repository
# import other mocks as needed


def describe_{use_case_name}():
    @pytest.fixture
    def mock_repository():
        return Mock{Domain}Repository()

    @pytest.fixture
    def use_case(mock_repository):
        return {UseCaseClass}(repository=mock_repository)

    def should_succeed_when_valid_input(use_case, mock_repository):
        # Arrange
        # ... set up test data in mock repository

        # Act
        result = use_case.execute(params)

        # Assert
        assert result is not None
        # ... specific assertions

    def should_raise_error_when_invalid_input(use_case):
        # Arrange & Act & Assert
        with pytest.raises(ExpectedError):
            use_case.execute(invalid_params)

    def should_handle_empty_data(use_case, mock_repository):
        # Test edge case with no data
        result = use_case.execute(params)
        assert result == expected_empty_result
```

## Mock Repository Pattern

Mocks are in-memory implementations of repository interfaces:

```python
class MockPlantsRepository:
    def __init__(self):
        self._plants = []

    def find_all(self):
        return self._plants

    def find_by_id(self, plant_id):
        return next((p for p in self._plants if p.id == plant_id), None)

    def create(self, plant):
        self._plants.append(plant)

    def update(self, plant):
        self._plants = [p if p.id != plant.id else plant for p in self._plants]

    def delete(self, plant_id):
        self._plants = [p for p in self._plants if p.id != plant_id]
```

## Test Scenarios to Cover

For each use case, generate tests for:

1. **Happy path** — Valid input produces expected output
2. **Invalid input** — Missing or malformed data raises appropriate error
3. **Empty state** — Behavior when no data exists
4. **Edge cases** — Boundary values, maximum lengths, special characters
5. **Authorization** — Verify that protected actions check permissions
6. **Side effects** — Verify data is persisted/deleted in the repository

## Running Tests

```bash
# All tests
pytest

# Specific domain
pytest src/app/core/use_cases/plants/tests/

# Specific test file
pytest src/app/core/use_cases/sensors_records/tests/create_sensor_record_test.py

# Verbose with output
pytest -v -s

# Stop on first failure
pytest -x
```

## Checklist

1. [ ] Test file follows `*_test.py` naming convention
2. [ ] Uses `describe_` prefix for BDD-style grouping
3. [ ] Dependencies injected via `pytest.fixture`
4. [ ] Mock repositories used instead of real database
5. [ ] Covers success, error, and edge cases
6. [ ] Uses meaningful assertion messages
7. [ ] Tests are independent (no shared mutable state)
