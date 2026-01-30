#
# Project: edu_assistant
# Component: orchestrator Docker image
# Responsibility:
#   Package the orchestrator service runtime for container execution.
#
# Architectural Notes:
#   - Containerizes the orchestration layer without defining its logic.
#   - Execution remains delegated to tools/connectors and governed by policies.
#
# Related Documentation:
#   - docs/*/architecture.md
#   - docs/*/vision.md
#   - AGENTS.md
#
# Important Constraints:
#   - Do not bake secrets or environment-specific policies.
#   - Keep the image minimal and reproducible.
#
FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml /app/pyproject.toml

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir .

COPY src /app/src

ENV PYTHONPATH=/app
EXPOSE 8002

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8002"]
