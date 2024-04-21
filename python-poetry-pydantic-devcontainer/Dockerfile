FROM python:3.10 as base
ENV PIP_DISABLE_PIP_VERSION_CHECK=1


FROM base as poetry
RUN pip install --no-cache-dir poetry==1.8.2


FROM poetry as builder
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-ansi

FROM base
WORKDIR /app

COPY --from=builder /app ./
COPY ./app ./

# Create a new group `app` with Group ID `1000`.
RUN addgroup --gid 1000 app
# Create a new user `app`, sets home directory to `/app`, User ID `1000`, in
# the group `app`. The `-DH` option results in a system account.
RUN adduser app -h /app -u 1000 -G app -DH
# Change the user for subsequent commands in Dockerfile to the user with ID
# `1000`.
USER 1000

WORKDIR /

EXPOSE 80

CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]