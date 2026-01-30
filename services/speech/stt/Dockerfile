#
# Project: edu_assistant
# Component: speech-stt Docker image
# Responsibility:
#   Package the speech-to-text service runtime for container execution.
#
# Architectural Notes:
#   - Provides transcription only; it does not interpret intent or execute actions.
#   - Supports the interface layer by normalizing audio into text.
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
EXPOSE 8001

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8001"]
