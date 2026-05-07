---
slug: deployment
category: operations
generatedAt: 2026-05-07T15:18:53.341Z
relevantFiles:
  - Dockerfile
  - docker-compose.database.yml
  - docker-compose.yml
  - .devcontainer/docker-compose.yml
  - .github/workflows/cd.yaml
  - .github/workflows/ci.yaml
---

# How do I deploy this project?

## Deployment

### Docker

This project includes Docker configuration.

```bash
docker build -t app .
docker run -p 3000:3000 app
```

### CI/CD

CI/CD pipelines are configured for this project.
Check `.github/workflows/` or equivalent for pipeline configuration.