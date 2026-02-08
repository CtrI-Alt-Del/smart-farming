---
type: skill
name: Documentation
description: Generate and update technical documentation
skillSlug: documentation
phases: [P, C]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

# Documentation

## When to Use

Use this skill when creating or updating documentation for the Smart Farming project. This covers inline code documentation, architecture docs, sprint reports, and context files.

## Documentation Locations

| Type | Location | Format |
|------|----------|--------|
| Project README | `README.md` | Markdown (Portuguese) |
| Architecture | `documentation/development/archtecture.md` | Markdown |
| Design guidelines | `documentation/development/design.md` | Markdown |
| Commit conventions | `documentation/development/commits-emoji-table.md` | Markdown |
| Sprint reports | `documentation/reports/sprint-{n}.md` | Markdown |
| Context docs | `.context/docs/` | Markdown with frontmatter |
| Agent playbooks | `.context/agents/` | Markdown with frontmatter |

## Documentation Standards

### Language

- **README and user-facing docs**: Portuguese (project language)
- **Code comments and docstrings**: English or Portuguese (follow existing file convention)
- **Context files**: English (for AI tool compatibility)

### Python Docstrings

Use docstrings for complex use cases and public methods:

```python
class CreateSensorRecord:
    """Creates a new sensor record from form or CSV data.
    
    Dependencies:
        repository: SensorsRecordsRepository interface
        plants_repository: PlantsRepository interface
    """
    
    def execute(self, data: dict) -> SensorRecord:
        """Execute the use case.
        
        Args:
            data: Dictionary with sensor values (soil_humidity, temperature, etc.)
            
        Returns:
            The created SensorRecord entity
            
        Raises:
            InvalidSensorDataError: If required fields are missing or invalid
        """
```

### Template Documentation

Add comments for complex Jinja2 template logic:

```html
{# Dashboard chart container - receives data via HTMX partial update #}
<div id="temperature-chart" 
     hx-get="/sensors-records/chart/temperature" 
     hx-trigger="load">
</div>
```

### SQL Documentation

Comment complex queries in repository implementations:

```python
def find_by_date_range(self, start_date, end_date):
    """Fetch records between two dates, ordered by creation date descending."""
    query = f"""
        SELECT * FROM {SENSORS_RECORDS_TABLE['name']}
        WHERE created_at BETWEEN %s AND %s
        ORDER BY created_at DESC
    """
```

## Documentation Update Checklist

When modifying code:

1. [ ] Update docstrings if function signature or behavior changed
2. [ ] Update architecture docs if structural changes were made
3. [ ] Update README if setup process changed
4. [ ] Update `.context/docs/` if workflows or tooling changed
5. [ ] Add sprint report entry for significant features or fixes

## Sprint Report Template

```markdown
# Sprint {N} Report

## Period
DD/MM/YYYY - DD/MM/YYYY

## Completed
- (list of completed user stories/tasks)

## Burndown Chart
![Burndown](../images/sprint-{n}-burndown-chart.png)

## Challenges
- (issues encountered)

## Next Sprint
- (planned work)
```
