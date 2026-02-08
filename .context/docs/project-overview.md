---
type: doc
name: project-overview
description: High-level overview of the project, its purpose, and key components
category: overview
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Project Overview

Smart Farming is a web application built to monitor and manage a smart greenhouse at FATEC Sao Jose dos Campos. It replaces manual CSV-based workflows for sensor data collection and checklist verification with an automated, web-based system featuring interactive dashboards, data management (CRUD), and user authentication.

> **Detailed Analysis**: For complete symbol counts, architecture layers, and dependency graphs, see [`codebase-map.json`](./codebase-map.json).

## Quick Facts

- **Root**: `/home/petros/projects/smart-farming`
- **Languages**: Python (~375 files), JavaScript, HTML/Jinja2, CSS
- **Entry**: `src/app/main.py` (Flask app factory), `src/app/wsgi.py` (WSGI)
- **Framework**: Flask 3.0.2 with Gunicorn
- **Database**: MySQL 8 with SQLAlchemy metadata and Alembic migrations (via Flask-Migrate)
- **Full analysis**: [`codebase-map.json`](./codebase-map.json)

## Entry Points

- [`src/app/main.py`](../../src/app/main.py) — Flask application factory (`init_app()`)
- [`src/app/wsgi.py`](../../src/app/wsgi.py) — WSGI entry point for Gunicorn
- [`gunicorn.config.py`](../../gunicorn.config.py) — Gunicorn server configuration

## Key Exports

The application does not export a library API. It exposes HTTP routes via Flask blueprints organized by domain:

- **Authentication views** — Login, password reset
- **Sensors records views** — Sensor data dashboard, tables, CRUD
- **Checklist records views** — Checklist dashboard, tables, CRUD
- **Plants views** — Plant management
- **Error views** — Custom error pages

## File Structure & Code Organization

- `src/app/core/` — Business logic following Clean Architecture (entities, use cases, interfaces, errors)
- `src/app/infra/` — Infrastructure layer (database, views, repositories, forms, providers, jobs, authentication)
- `src/ui/templates/` — Jinja2 templates organized as components, layouts, and pages
- `src/ui/static/` — Static assets (JavaScript, CSS, images)
- `documentation/` — Sprint reports, presentations, architecture docs, and images
- `docker-compose.yml` — Multi-container setup (app + MySQL)
- `Dockerfile` — Application container (Python 3.12 + Node.js 22)

## Technology Stack Summary

- **Backend**: Python 3.12, Flask 3.0.2, Gunicorn (WSGI server)
- **Database**: MySQL 8 with `mysql-connector-python` (repository queries) and SQLAlchemy/Alembic (schema migrations)
- **Frontend**: Jinja2 templates, HTMX, Hyperscript, TailwindCSS, ApexCharts
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Forms**: Flask-WTF / WTForms
- **Scheduling**: Flask-APScheduler (database backups)
- **Testing**: pytest, pytest-describe, Faker
- **Containerization**: Docker, Docker Compose
- **Linting**: Ruff, Biome (JavaScript)

## Core Framework Stack

- **Backend**: Flask handles routing, Jinja2 renders server-side templates, and MySQL stores all persistent data. The app follows a Clean Architecture pattern with clear separation between core business logic and infrastructure.
- **Frontend**: HTMX enables dynamic interactions without full page reloads, Hyperscript handles client-side scripting, and TailwindCSS provides utility-first styling. ApexCharts renders interactive dashboard graphs.
- **Data Processing**: Pandas and NumPy are used for CSV import/export and data analysis operations.

## UI & Interaction Libraries

- **TailwindCSS** — Utility-first CSS framework for responsive design
- **HTMX** — HTML-over-the-wire for dynamic partial page updates
- **Hyperscript** — Client-side scripting for simple UI interactions
- **ApexCharts** — Interactive charts for sensor and checklist dashboards
- **Custom JavaScript modules** — Chart rendering, CSV handling, datepicker, filters, pagination

## Getting Started Checklist

1. Install [Docker](https://www.docker.com/products/docker-desktop/) and [Git](https://git-scm.com/).
2. Clone the repository: `git clone https://github.com/CtrI-Alt-Del/smart-farming.git`
3. Copy `.env.example` to `.env` and configure environment variables.
4. Start the application: `docker compose up`
5. Access the app at `http://localhost:8000`.
6. Review [Development Workflow](./development-workflow.md) for day-to-day tasks.

## Next Steps

- See [architecture documentation](../../documentation/development/archtecture.md) for system design details
- See [design documentation](../../documentation/development/design.md) for UI/UX guidelines
- Review sprint reports in `documentation/reports/` for project history
