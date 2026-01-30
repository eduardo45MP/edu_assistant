#
# Project: edu_assistant
# Component: interface-client Docker image
# Responsibility:
#   Package the interface-client service runtime for container execution.
#
# Architectural Notes:
#   - Containerizes the interface layer; it captures input and forwards it.
#   - It does not execute tools or interpret intent.
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
EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
