---
type: skill
name: Security Audit
description: Security review checklist for code and infrastructure
skillSlug: security-audit
phases: [R, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Security Audit

## When to Use

Use this skill when auditing security aspects of the Smart Farming application, especially before deploying changes that affect authentication, database access, user input handling, or external integrations.

## Security Checklist

### Authentication & Authorization

- [ ] Login uses Flask-Login with proper session management
- [ ] Passwords are hashed with Flask-Bcrypt before storage (never plain text)
- [ ] `@login_required` decorator protects all admin-only routes
- [ ] `SECRET_KEY` is set via environment variable, not hardcoded
- [ ] Session cookies have appropriate security flags
- [ ] Password reset flow uses time-limited tokens
- [ ] Failed login attempts don't reveal whether email exists

### Database Security

- [ ] All SQL queries use parameterized values via `Mysql.query()` and `Mysql.mutate()`
- [ ] No string concatenation or f-strings used to build SQL queries with user input
- [ ] Database credentials are loaded from environment variables (`MYSQL_DATABASE_*`)
- [ ] Database connection uses the internal Docker network (`app-network`), not exposed publicly
- [ ] `init_database()` (which drops/recreates tables) is only used in development

### Input Validation

- [ ] All user input goes through Flask-WTF forms with appropriate validators
- [ ] CSV file uploads are validated before processing (file type, size, content structure)
- [ ] Form data is validated server-side even if client-side validation exists
- [ ] File paths are sanitized to prevent directory traversal
- [ ] Email inputs use `email_validator` for proper validation

### Template Security

- [ ] Jinja2 autoescaping is enabled (Flask default) — no `| safe` on user-provided data
- [ ] HTMX responses don't include unsanitized user content
- [ ] No sensitive data (passwords, tokens) rendered in HTML source
- [ ] Error pages don't expose stack traces or internal paths in production

### Infrastructure Security

- [ ] `.env` file is in `.gitignore` and never committed
- [ ] Docker containers run with minimal privileges
- [ ] MySQL port (3306) is only exposed when needed for development
- [ ] Google Drive API credentials are stored securely
- [ ] `SUPPORT_EMAIL_APP_PASSWORD` is not logged or exposed

### Dependencies

- [ ] Python dependencies in `requirements.txt` don't have known vulnerabilities
- [ ] npm dependencies in `package.json` are up to date
- [ ] No unnecessary packages installed

## Common Vulnerabilities to Check

1. **SQL Injection** — Search for string formatting in SQL queries
2. **XSS** — Check for `| safe` filter usage in Jinja2 templates
3. **CSRF** — Ensure Flask-WTF CSRF protection is active on all forms
4. **Sensitive Data Exposure** — Check logs and error responses for secrets
5. **Insecure Direct Object Reference** — Verify UUID-based resource access has authorization checks
6. **Broken Authentication** — Ensure session handling is secure

## Audit Report Template

```markdown
## Security Audit Report

**Date**: YYYY-MM-DD
**Scope**: (files/features audited)

### Critical Issues
- (none / list)

### High Priority
- (findings)

### Medium Priority
- (findings)

### Recommendations
- (improvements)
```
