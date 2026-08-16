# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

# Stage 1: Build the application.
FROM python:3.14-slim AS builder

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy source code.
COPY . /app

# Install the dependencies and build the app.
WORKDIR /app
RUN uv lock && \
    uv sync --frozen --no-cache && \
    uv clean && \
    uv build && \
    pip install dist/*.whl

# Stage 2: Create the final image.
FROM python:3.14-slim
WORKDIR /tmp
COPY --from=builder /usr/local/bin/andexor-grass-spider-soa-service /usr/local/bin/
COPY --from=builder /usr/local/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/

# CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]

# Run the application.
CMD ["/usr/local/bin/andexor-grass-spider-soa-service"]
