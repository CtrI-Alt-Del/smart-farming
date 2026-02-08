---
type: doc
name: tooling
description: Scripts, IDE settings, automation, and developer productivity tips
category: tooling
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Tooling & Productivity Guide

This guide covers the tools, scripts, and automation used in the Smart Farming project to keep development efficient and consistent.

## Required Tooling

- **Docker** (latest) — Container runtime for running the full stack. Powers `docker compose up`.
- **Git** — Version control. Required for cloning and contributing.
- **Python 3.12** — Backend runtime. Installed via the Docker image `nikolaik/python-nodejs:python3.12-nodejs22`.
- **Node.js 22** — JavaScript toolchain for TailwindCSS builds and Biome linting.
- **pip** — Python package manager. Installs from `requirements.txt`.
- **npm** — Node.js package manager. Installs from `package.json`.

## Recommended Automation

### Linting & Formatting

- **Ruff** (Python) — Fast linter configured in `pyproject.toml`. Run with `ruff check .`
- **Biome** (JavaScript) — Linter and formatter configured in `biome.json`. Run with `npx biome check .`

### CSS Build

- TailwindCSS is used for styling. The build is managed via npm scripts defined in `package.json`.
- Use watch mode during development to auto-rebuild CSS on file changes.

### Scheduled Jobs

- **Flask-APScheduler** handles background tasks like daily database backups to Google Drive.
- Job configuration is in `src/app/infra/jobs/`.

### Database Tooling

- Versioned schema migrations live in `migrations/` (Alembic + Flask-Migrate)
- Migration models/metadata live in `src/app/infra/database/models.py`
- Primary commands:
  - `flask --app ./src/app/main.py:init_app db current`
  - `flask --app ./src/app/main.py:init_app db upgrade`
  - `flask --app ./src/app/main.py:init_app db downgrade -1`
  - `flask --app ./src/app/main.py:init_app db-seed-defaults`
- Legacy SQL helper scripts remain in `src/app/infra/database/scripts/` for ad-hoc inspection only

## IDE / Editor Setup

- **Python extension** — For Flask/Python intellisense and debugging
- **TailwindCSS IntelliSense** — Autocomplete for utility classes in templates
- **HTMX extension** — Syntax support for HTMX attributes
- **Jinja2 extension** — Template syntax highlighting
- **Biome extension** — JavaScript linting integration

## Productivity Tips

- Use `docker compose -f docker-compose.database.yml up` to start only the database when developing locally without Docker for the app
- The `gunicorn.config.py` file configures the production server with gevent workers
- Check `documentation/development/commits-emoji-table.md` for the project's commit emoji conventions
- Environment variables are loaded from `.env` via `python-dotenv`
- Flask migration CLI depends on `FLASK_APP=./src/app/main.py:init_app` (or passing `--app` inline)
- See [Development Workflow](./development-workflow.md) for the full local setup guide
