---
type: doc
name: testing-strategy
description: Test frameworks, patterns, coverage requirements, and quality gates
category: testing
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Testing Strategy

Quality is maintained through unit testing of core business logic (use cases and shared utilities). The project follows a mock-based testing approach where repository interfaces are replaced with in-memory implementations, ensuring tests remain fast and isolated from the database.

## Test Types

- **Unit**: pytest + pytest-describe, files named `*_test.py` in `src/app/core/use_cases/*/tests/` and `src/app/core/commons/tests/`
- **Integration**: Migration workflow validation (`upgrade`, `downgrade`, `stamp`) on local MySQL before release
- **E2E**: Not yet implemented; frontend interactions are tested manually

## Running Tests

- All tests: `pytest`
- Watch mode: `pytest --watch` (requires pytest-watch if installed)
- Specific module: `pytest src/app/core/use_cases/sensors_records/tests/`
- Verbose output: `pytest -v`
- Environment: Tests automatically use `ENVIRONMENT=test` (configured in `pyproject.toml`)
- Migration smoke (manual): `flask --app ./src/app/main.py:init_app db upgrade` then `flask --app ./src/app/main.py:init_app db downgrade -1`

## Test Patterns

- **BDD-style**: Tests use `pytest-describe` for behavior-driven structure (`describe_feature` / `should_do_something`)
- **Fixtures**: `pytest.fixture` for dependency injection (mock repositories, providers)
- **Mocks**: Located in `src/app/core/use_cases/tests/mocks/` — includes:
  - Repository mocks (plants, sensors records, checklist records, users)
  - Provider mocks (cloud storage, data analysis, email)
  - Authentication mocks
- **Faker classes**: Custom fakers generate realistic test data for entities
- **Isolation**: Each test creates its own mock dependencies, no shared mutable state

## Quality Gates

- All existing tests must pass before merging
- New use cases should include corresponding test files
- Mock repositories should be updated when interfaces change
- Ruff linter must pass (configured in `pyproject.toml`)
- Biome linter for JavaScript files (configured in `biome.json`)

## Troubleshooting

- If tests fail with import errors, ensure `ENVIRONMENT=test` is set (normally handled by `pyproject.toml`)
- Database-dependent features are not tested in unit tests; use Docker Compose for manual integration testing
- If migration commands fail on an already populated legacy database, use `flask --app ./src/app/main.py:init_app db stamp head` only after validating schema parity
- See [Development Workflow](./development-workflow.md) for setting up the local environment
