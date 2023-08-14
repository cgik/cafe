FROM python:3.11

ENV POETRY_VERSION=1.1.11

WORKDIR /app

RUN pip install poetry==${POETRY_VERSION}

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

COPY . /app/

CMD ["poetry", "run", "start"]