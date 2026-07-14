#!/bin/sh

set -e

echo "Running migrations..."
alembic upgrade head

echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}