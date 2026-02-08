---
type: skill
name: Bug Investigation
description: Systematic bug investigation and root cause analysis
skillSlug: bug-investigation
phases: [E, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Bug Investigation

## When to Use

Use this skill when investigating bugs in the Smart Farming application. It provides a systematic approach to trace issues through the Clean Architecture layers.

## Investigation Process

### Step 1: Classify the Bug

Determine the category:
- **UI/Template Bug** — Visual issues, broken layouts, HTMX not updating
- **Route/View Bug** — 404s, 500s, wrong redirects, incorrect responses
- **Business Logic Bug** — Use case producing wrong results
- **Database Bug** — Data not saving, wrong queries, connection errors
- **Authentication Bug** — Login failures, session issues, unauthorized access
- **Scheduled Job Bug** — Backup failures, APScheduler errors
- **CSV Import/Export Bug** — File parsing issues, data corruption

### Step 2: Trace the Request Flow

Follow the data path through the architecture:

```
User Action (browser)
  → HTMX request / form submission
    → Flask View (src/app/infra/views/{domain}_views/)
      → Factory (src/app/infra/factories/use_cases/)
        → Use Case (src/app/core/use_cases/{domain}/)
          → Repository (src/app/infra/repositories/{domain}/)
            → MySQL (src/app/infra/database/mysql.py)
              → Database
```

### Step 3: Key Debugging Locations

| Symptom | Where to Look |
|---------|---------------|
| Page not loading | `infra/views/` — check route registration, blueprint |
| Form validation error | `infra/forms/` — check WTForms validators |
| Data not displaying | `infra/repositories/` — check SQL query |
| Wrong calculation | `core/use_cases/` — check business logic |
| Chart not rendering | `src/ui/static/scripts/` — check JavaScript |
| HTMX not working | Template — check `hx-*` attributes and target IDs |
| Login failing | `infra/authentication/` — check Flask-Login config |
| Database error | `infra/database/mysql.py` — check connection, query syntax |
| Template error | `src/ui/templates/` — check Jinja2 syntax, variable names |
| Scheduled job failing | `infra/jobs/` — check APScheduler config |

### Step 4: Check Common Causes

1. **Environment variables** — Is `.env` configured? Check `MYSQL_DATABASE_*`, `SECRET_KEY`
2. **Database schema** — Does the table match `infra/constants/mysql.py`?
3. **Import errors** — Are module paths correct? (uses relative imports within `src/app/`)
4. **Docker networking** — Is `database` hostname resolving? (Docker Compose service name)
5. **HTMX targets** — Does the `hx-target` ID exist in the DOM?
6. **Form CSRF** — Is `{{ form.hidden_tag() }}` included in form templates?

### Step 5: Reproduce and Fix

1. Reproduce in Docker environment: `docker compose up`
2. Check Flask console output for errors/tracebacks
3. If database-related, connect to MySQL and inspect data
4. Implement the fix in the appropriate layer
5. Run `pytest` to verify no regressions
6. Test the fix end-to-end in the browser

## Bug Report Template

```markdown
## Bug Report

**Summary**: (one-line description)
**Layer**: UI / View / Use Case / Repository / Database / Auth
**Steps to Reproduce**:
1. ...

**Expected Behavior**: ...
**Actual Behavior**: ...
**Root Cause**: ...
**Fix Applied**: ...
**Tests Added**: Yes / No
```
