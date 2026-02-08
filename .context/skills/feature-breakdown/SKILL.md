---
type: skill
name: Feature Breakdown
description: Break down features into implementable tasks
skillSlug: feature-breakdown
phases: [P]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Feature Breakdown

## When to Use

Use this skill when planning a new feature for the Smart Farming application. It helps decompose a feature request into concrete, implementable tasks following the project's Clean Architecture.

## Process

### 1. Identify the Domain

Determine which domain the feature belongs to:
- **Plants** — Plant management (CRUD, listing)
- **Sensors Records** — Sensor data collection, dashboards, charts
- **Checklist Records** — Checklist data, forms, dashboards
- **Authentication** — Login, password reset, session management

### 2. Map Required Layers

For each feature, identify what needs to be created or modified in each layer:

#### Core Layer (`src/app/core/`)
- [ ] **Entity** — Does this feature need a new domain entity or modification to existing ones in `core/entities/`?
- [ ] **Use Case** — Create a new use case class with `execute()` method in `core/use_cases/{domain}/`
- [ ] **Interface** — Does this feature need a new repository interface in `core/interfaces/`?
- [ ] **Errors** — Define custom exceptions in `core/errors/` if needed
- [ ] **Commons** — Any shared utilities needed in `core/commons/`?

#### Infrastructure Layer (`src/app/infra/`)
- [ ] **Repository** — Implement the data access in `infra/repositories/{domain}/`
- [ ] **Factory** — Create a factory function in `infra/factories/use_cases/` to wire the use case
- [ ] **View** — Create or update Flask route handler in `infra/views/{domain}_views/`
- [ ] **Form** — Create Flask-WTF form in `infra/forms/` if user input is needed
- [ ] **Constants** — Add SQL table/column definitions to `infra/constants/mysql.py` if schema changes
- [ ] **Database Script** — Update `infra/database/scripts/schema.sql` for new tables

#### UI Layer (`src/ui/`)
- [ ] **Template** — Create page template in `templates/pages/{domain}/`
- [ ] **Components** — Reuse or create components in `templates/components/`
- [ ] **JavaScript** — Add client-side scripts in `static/scripts/` for charts or interactions
- [ ] **Styles** — TailwindCSS classes (no separate CSS file needed usually)

#### Testing
- [ ] **Unit Tests** — Create `*_test.py` in `core/use_cases/{domain}/tests/`
- [ ] **Mocks** — Add mock repositories in `core/use_cases/tests/mocks/` if new interfaces were created

### 3. Define Task Order

Follow this implementation order for dependencies:

1. Core entities and interfaces (no dependencies)
2. Core use cases (depend on interfaces)
3. Infrastructure repositories (implement interfaces)
4. Infrastructure factories (wire use cases with repositories)
5. Infrastructure forms (if needed)
6. Infrastructure views (use factories, render templates)
7. UI templates and scripts
8. Tests (can start in parallel with step 2)

### 4. Estimate Complexity

Reference the project's backlog estimation scale:
- **1-2 points** — Simple CRUD, single layer change
- **3-5 points** — Multi-layer feature, forms + views + templates
- **8 points** — Complex feature with charts, CSV handling, or authentication logic
- **13 points** — Cross-cutting feature affecting multiple domains

## Example Breakdown

**Feature: "Add new sensor type"**

1. Update `SensorsRecord` entity in `core/entities/`
2. Update `SENSORS_RECORDS_TABLE` constants in `infra/constants/mysql.py`
3. Update `schema.sql` with new column
4. Update `SensorsRecordsRepository` interface and implementation
5. Update affected use cases (create, edit, dashboard)
6. Update forms in `infra/forms/`
7. Update view templates to include new field
8. Update chart scripts in `static/scripts/`
9. Update mock repositories and add tests
