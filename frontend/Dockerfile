FROM python:3.11-slim-buster
LABEL org.opencontainers.image.description="Flask API with ML prediction"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./src .

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ARG PORT=5000
ENV PORT $PORT
EXPOSE $PORT

CMD exec gunicorn --bind :$PORT --workers 1 --threads 2 app:app
