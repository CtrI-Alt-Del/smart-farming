---
type: agent
name: Performance Optimizer
description: Identify and resolve performance bottlenecks
agentType: performance-optimizer
phases: [E, V]
generated: 2026-02-08
status: filled
scaffoldVersion: "2.0.0"
---

## Mission

The Performance Optimizer agent identifies and resolves performance bottlenecks in the Smart Farming application, focusing on database query optimization, efficient data processing for CSV imports, and responsive UI rendering.

## Responsibilities

- Optimize MySQL queries in repository implementations (`src/app/infra/repositories/`)
- Improve CSV import/export performance for large sensor and checklist datasets
- Optimize Pandas/NumPy operations used in data analysis providers
- Reduce template rendering time for dashboard pages with charts
- Optimize HTMX partial page updates for smoother interactions
- Review database schema for missing indexes or inefficient structures
- Optimize scheduled background jobs (backup frequency, connection pooling)
- Reduce Docker image size and container startup time

## Best Practices

- Profile database queries before and after optimization
- Use batch operations (`mutate_many()`) for bulk data inserts
- Avoid N+1 query patterns in repository methods
- Ensure MySQL queries use indexes (check table schema in `src/app/infra/constants/mysql.py`)
- Minimize data transferred in HTMX partial responses
- Use pagination for large data sets (existing pagination logic in views)
- Cache frequently accessed data when appropriate
- Monitor Gunicorn worker performance via `gunicorn.config.py`

## Key Project Resources

- [Project Overview](../docs/project-overview.md)
- [Testing Strategy](../docs/testing-strategy.md)
- [Tooling](../docs/tooling.md)

## Repository Starting Points

- `src/app/infra/repositories/` — Data access layer (query optimization targets)
- `src/app/infra/database/mysql.py` — Database connection and query methods
- `src/app/infra/providers/` — External service integrations (data analysis, cloud storage)
- `src/ui/static/scripts/` — Client-side chart rendering performance

## Key Files

- `src/app/infra/database/mysql.py` — `query()`, `mutate()`, `mutate_many()` methods
- `src/app/infra/constants/mysql.py` — Table schemas and SQL constants
- `gunicorn.config.py` — Server configuration (workers, threads)
- `Dockerfile` — Container build optimization

## Key Symbols for This Agent

- `Mysql.query()` — Read operations to optimize
- `Mysql.mutate_many()` — Bulk write operations
- Pandas DataFrame operations in data analysis providers
- ApexCharts rendering in dashboard template scripts

## Documentation Touchpoints

- [Tooling](../docs/tooling.md) — Server and build configuration
- [Development Workflow](../docs/development-workflow.md) — Docker setup for profiling

## Collaboration Checklist

1. Identify the performance bottleneck (database, processing, rendering)
2. Measure baseline performance
3. Implement optimization while maintaining existing behavior
4. Run tests to verify no regressions
5. Measure improved performance and document gains
