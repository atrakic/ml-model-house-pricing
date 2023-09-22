#FROM python:3.11-slim-buster as build-venv
FROM debian:11-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt


# Copy the virtualenv into a distroless image
FROM gcr.io/distroless/python3-debian11 as final
LABEL org.opencontainers.image.description="Machine Learning model to predict house prices"
COPY --from=build-venv /venv /venv
COPY . /app
WORKDIR /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/venv/bin/python3", "app.py"]
