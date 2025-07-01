FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv

RUN mkdir /app
WORKDIR /app

COPY ["./uv.lock", "./pyproject.toml", "./"]

RUN uv venv && uv sync

COPY ./scripts ./scripts
COPY ./src ./src

EXPOSE 8000

RUN chmod +x /app/scripts/start.sh
CMD ["sh", "-c", "/app/scripts/start.sh"]
