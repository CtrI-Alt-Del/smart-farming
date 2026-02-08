---
type: agent
name: Test Writer
description: Create and maintain test suites
agentType: test-writer
phases: [E, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Mission

The Test Writer agent creates and maintains the test suite for Smart Farming, ensuring comprehensive coverage of business logic through unit tests using pytest with mock repositories and BDD-style structure.

## Responsibilities

- Write unit tests for use cases in `src/app/core/use_cases/*/tests/`
- Create and update mock repositories in `src/app/core/use_cases/tests/mocks/`
- Implement custom Faker classes for generating test data
- Write tests for shared utilities in `src/app/core/commons/tests/`
- Ensure all use case `execute()` methods have corresponding test coverage
- Test error handling paths (custom exceptions in `core/errors/`)
- Maintain test fixtures for dependency injection

## Best Practices

- Use `pytest-describe` for BDD-style test structure (`describe_feature` / `should_behavior`)
- Create `pytest.fixture` functions for mock dependencies
- Mock all external dependencies (database, email, cloud storage) — never use real services in tests
- Use Faker classes for realistic test data generation
- Test both success and failure paths for each use case
- Keep tests isolated — each test should set up its own state
- Name test files as `*_test.py` following the existing convention
- Set `ENVIRONMENT=test` (configured in `pyproject.toml`)

## Testing Framework & Conventions

- **Framework**: pytest
- **Style plugin**: pytest-describe (BDD-style)
- **Environment**: pytest-env (auto-sets `ENVIRONMENT=test`)
- **Test data**: Faker library + custom faker classes
- **File pattern**: `*_test.py`
- **Location**: `src/app/core/use_cases/{domain}/tests/`

## Key Project Resources

- [Testing Strategy](../docs/testing-strategy.md)
- [Development Workflow](../docs/development-workflow.md)

## Repository Starting Points

- `src/app/core/use_cases/` — Use cases to test
- `src/app/core/use_cases/tests/mocks/` — Shared mock implementations
- `src/app/core/commons/tests/` — Utility tests
- `src/app/core/entities/` — Entity definitions for test data

## Key Files

- `pyproject.toml` — pytest configuration and Ruff settings
- `src/app/core/use_cases/tests/mocks/` — Mock repositories and providers
- `src/app/core/interfaces/` — Interfaces that mocks must implement
- `src/app/core/errors/` — Custom exceptions to test

## Key Symbols for This Agent

- `pytest.fixture` — Dependency injection for tests
- `describe_*` functions — BDD-style test groups
- Mock repository classes — In-memory data storage for testing
- Faker classes — Test data generators
- Use case `execute()` methods — Functions under test

## Documentation Touchpoints

- [Testing Strategy](../docs/testing-strategy.md) — Test patterns and requirements

## Collaboration Checklist

1. Identify the use case or module that needs tests
2. Create mock implementations for any new repository interfaces
3. Set up test fixtures with mock dependencies
4. Write tests for success scenarios
5. Write tests for error/edge cases
6. Run `pytest` to verify all tests pass
7. Check coverage and add tests for uncovered paths
