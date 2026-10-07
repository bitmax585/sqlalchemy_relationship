FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

COPY README.md ./
COPY alembic.ini ./
COPY alembic ./alembic

RUN pip install uv

COPY src ./src

RUN uv sync --frozen

CMD ["uv", "run", "python", "-m", "sqlalchemy_relationship.main"]

