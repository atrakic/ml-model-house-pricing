FROM python:3-slim AS build-env
COPY . /app
WORKDIR /app

FROM gcr.io/distroless/python3 AS final
COPY --from=build-env /app /app
WORKDIR /app
CMD ["app.py"]
