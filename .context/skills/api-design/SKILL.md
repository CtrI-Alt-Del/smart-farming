---
type: skill
name: Api Design
description: Design RESTful APIs following best practices
skillSlug: api-design
phases: [P, R]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# API Design

## When to Use

Use this skill when designing new routes or modifying existing endpoints in the Smart Farming application. The project uses Flask blueprints with server-rendered HTML (Jinja2 + HTMX), not a traditional REST JSON API.

## Route Design Principles

### URL Convention

The project uses these URL patterns:

| Action | Method | URL Pattern | Example |
|--------|--------|-------------|---------|
| List/Dashboard | GET | `/{domain}` | `/sensors-records` |
| Create form | GET | `/{domain}/create` | `/checklist-records/create` |
| Create submit | POST | `/{domain}` | `POST /plants` |
| Edit form | GET | `/{domain}/{id}/edit` | `/sensors-records/{id}/edit` |
| Edit submit | PUT/POST | `/{domain}/{id}` | `PUT /plants/{id}` |
| Delete | DELETE | `/{domain}/{id}` | `DELETE /checklist-records/{id}` |
| Dashboard | GET | `/{domain}/dashboard` | `/sensors-records/dashboard` |

### Blueprint Organization

Each domain has its own blueprint in `src/app/infra/views/{domain}_views/`:

```python
from flask import Blueprint

{domain}_views_bp = Blueprint("{domain}", __name__, url_prefix="/{domain}")
```

Register new blueprints in `src/app/infra/views/__init__.py`.

### View Pattern

Views follow this standard pattern:

```python
@bp.route("/path", methods=["GET"])
@login_required  # if admin-only
def view_name():
    # 1. Get use case from factory
    use_case = create_{action}_use_case()
    
    # 2. Extract params from request
    params = request.args.get("param")
    
    # 3. Execute use case
    result = use_case.execute(params)
    
    # 4. Render template with data
    return render_template("pages/{domain}/page.html", data=result)
```

### HTMX Endpoints

For partial page updates via HTMX:

- Return HTML fragments, not full pages
- Use appropriate `hx-target` and `hx-swap` attributes
- Return status code 200 for successful partial updates
- Use `hx-trigger` for custom events after mutations

### Response Patterns

| Scenario | Response |
|----------|----------|
| Page render | `render_template("pages/...")` |
| HTMX partial | `render_template("components/...")` |
| Redirect after mutation | `redirect(url_for("blueprint.view"))` |
| Error page | `render_template("pages/error/...")`, status 4xx/5xx |
| CSV download | `Response(csv_data, mimetype="text/csv")` |

## Checklist for New Routes

1. [ ] Define URL pattern following existing conventions
2. [ ] Create or use existing blueprint
3. [ ] Add `@login_required` for admin-only operations
4. [ ] Use factory to get use case (never instantiate repositories in view)
5. [ ] Validate input through Flask-WTF forms
6. [ ] Render appropriate template
7. [ ] Register blueprint in `infra/views/__init__.py`
8. [ ] Create corresponding template in `src/ui/templates/pages/`
