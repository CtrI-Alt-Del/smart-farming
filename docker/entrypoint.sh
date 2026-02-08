#!/usr/bin/env sh

set -eu

MAX_RETRIES="${DB_MIGRATION_MAX_RETRIES:-30}"
RETRY_DELAY_SECONDS="${DB_MIGRATION_RETRY_DELAY_SECONDS:-3}"
RUN_DB_SEED_DEFAULTS_ON_START="${RUN_DB_SEED_DEFAULTS_ON_START:-false}"

echo "Applying database migrations before app startup..."

ATTEMPT=1
while [ "$ATTEMPT" -le "$MAX_RETRIES" ]; do
  if flask --app ./src/app/main.py:init_app db upgrade; then
    if [ "$RUN_DB_SEED_DEFAULTS_ON_START" = "true" ]; then
      echo "RUN_DB_SEED_DEFAULTS_ON_START=true: applying default seed data..."
      flask --app ./src/app/main.py:init_app db-seed-defaults
    fi

    echo "Migrations applied successfully. Starting application..."
    exec npm start
  fi

  echo "Migration attempt ${ATTEMPT}/${MAX_RETRIES} failed. Retrying in ${RETRY_DELAY_SECONDS}s..."
  ATTEMPT=$((ATTEMPT + 1))
  sleep "$RETRY_DELAY_SECONDS"
done

echo "Could not apply migrations after ${MAX_RETRIES} attempts. Exiting."
exit 1
