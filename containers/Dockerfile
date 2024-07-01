FROM python:3.10.0-slim-bullseye

# Set environment variables for Python
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.2.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/opt/poetry' \
    PATH="${POETRY_HOME}/bin:$PATH"

WORKDIR /tmp

RUN mkdir -p /opt/app
WORKDIR /opt/app

# Copy the src folder into the container
COPY ./src /opt/app/src

RUN adduser --disabled-password --gecos '' appuser
USER appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"

RUN pip install --upgrade pip && \
    pip install poetry==$POETRY_VERSION

COPY poetry.lock pyproject.toml /opt/app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY src /opt/app

ENTRYPOINT ["python"]
