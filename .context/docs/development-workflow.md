---
type: doc
name: development-workflow
description: Day-to-day engineering processes, branching, and contribution guidelines
category: workflow
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Development Workflow

The Smart Farming project follows a feature-branch workflow with Docker-based development. All backend code lives in `src/app/` (Python/Flask), frontend templates in `src/ui/`, and infrastructure configuration at the project root. The application uses Clean Architecture, so new features typically touch multiple layers: core (use cases, entities), infrastructure (repositories, views, forms), and UI (templates, scripts).

## Branching & Releases

- **Main branch**: `main` — Production-ready code
- **Feature branches**: Created from `main` with descriptive names (e.g., `feature/add-sensor-filter`)
- **Refactor branches**: Prefixed with `refactor/` for structural changes
- **Bug fix branches**: Prefixed with `fix/` for bug corrections
- Development follows Scrum methodology with sprint-based releases
- Refer to `documentation/development/commits-emoji-table.md` for commit message conventions

## Local Development

- Start full stack (app + MySQL): `docker compose up`
- Start only the database: `docker compose -f docker-compose.database.yml up`
- Install Python dependencies: `pip install -r requirements.txt`
- Install Node dependencies: `npm install`
- Build TailwindCSS: `npm run build:css` (or watch mode via npm scripts)
- Run the Flask app directly: `gunicorn -c gunicorn.config.py src.app.wsgi:app`
- Apply schema migrations in local/dev: `flask --app ./src/app/main.py:init_app db upgrade`
- Create a new migration revision after model changes: `flask --app ./src/app/main.py:init_app db migrate -m "describe change"`
- Apply default seed data explicitly: `flask --app ./src/app/main.py:init_app db-seed-defaults`
- Run tests: `pytest`
- Application runs at `http://localhost:8000`

## Database Migration Workflow

- New database: run `flask --app ./src/app/main.py:init_app db upgrade`, then `flask --app ./src/app/main.py:init_app db-seed-defaults`
- Existing database with matching legacy schema (baseline adoption): run `flask --app ./src/app/main.py:init_app db stamp head`
- Existing database that needs schema changes: run `flask --app ./src/app/main.py:init_app db upgrade`
- Rollback one migration step if needed: `flask --app ./src/app/main.py:init_app db downgrade -1`

## Code Review Expectations

- All changes should follow the Clean Architecture pattern: business logic in `core/`, infrastructure concerns in `infra/`
- Use cases must be created via factory pattern (`infra/factories/use_cases/`)
- Views should only call use case factories, never access repositories directly
- Forms should use Flask-WTF for validation
- Database queries should go through the repository layer
- Templates should follow the component/layout/page hierarchy
- New features need corresponding tests in `core/use_cases/*/tests/`
- See [Testing Strategy](./testing-strategy.md) for testing requirements

## Onboarding Tasks

- Read the [Project Overview](./project-overview.md) to understand the system
- Review the [architecture documentation](../../documentation/development/archtecture.md)
- Set up `.env` from `.env.example` with required environment variables
- Run `docker compose up` and verify the app loads at `http://localhost:8000`
- Explore `src/app/core/use_cases/` to understand the business logic
- Review `src/app/infra/views/` to understand how routes map to use cases
