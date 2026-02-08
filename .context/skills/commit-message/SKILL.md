---
type: skill
name: Commit Message
description: Generate commit messages following conventional commits with scope detection
skillSlug: commit-message
phases: [E, C]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Commit Message

## When to Use

Use this skill when creating git commits for the Smart Farming project. The project uses an emoji-based commit convention documented in `documentation/development/commits-emoji-table.md`.

## Commit Format

```
<emoji> <type>(<scope>): <description>
```

### Emoji Table

| Emoji | Type | Usage |
|-------|------|-------|
| :sparkles: | feat | New feature |
| :bug: | fix | Bug fix |
| :recycle: | refactor | Code refactoring (no behavior change) |
| :art: | style | Code formatting, styling |
| :memo: | docs | Documentation changes |
| :white_check_mark: | test | Adding or updating tests |
| :wrench: | chore | Build, config, tooling changes |
| :rocket: | perf | Performance improvement |
| :lock: | security | Security fix or improvement |
| :package: | deps | Dependency updates |
| :fire: | remove | Removing code or files |
| :construction: | wip | Work in progress |

### Scope Detection

Determine the scope from the files changed:

| Files Changed | Scope |
|---------------|-------|
| `src/app/core/use_cases/plants/` | `plants` |
| `src/app/core/use_cases/sensors_records/` | `sensors` |
| `src/app/core/use_cases/checklist_records/` | `checklist` |
| `src/app/infra/authentication/` | `auth` |
| `src/app/infra/database/` | `database` |
| `src/app/infra/views/` | `views` |
| `src/app/infra/forms/` | `forms` |
| `src/ui/templates/` | `templates` |
| `src/ui/static/scripts/` | `scripts` |
| `src/ui/static/styles/` | `styles` |
| `docker-compose.yml`, `Dockerfile` | `docker` |
| `documentation/` | `docs` |
| `*_test.py`, `tests/` | `tests` |
| Multiple domains | `global` |

## Examples

```bash
# New feature
git commit -m ":sparkles: feat(sensors): add temperature filter to dashboard"

# Bug fix
git commit -m ":bug: fix(checklist): correct date parsing in CSV import"

# Refactoring
git commit -m ":recycle: refactor(database): extract query builder into utility"

# Tests
git commit -m ":white_check_mark: test(plants): add tests for create plant use case"

# Documentation
git commit -m ":memo: docs(global): update README with new setup instructions"

# Docker/Config
git commit -m ":wrench: chore(docker): update MySQL version to 8.1"
```

## Guidelines

1. Keep the description concise (50 chars or less for the subject line)
2. Use imperative mood ("add", "fix", "update", not "added", "fixed", "updated")
3. Don't end the subject line with a period
4. One logical change per commit
5. Reference issue numbers if applicable
6. Never commit `.env` files or secrets
