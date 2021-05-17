FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN addgroup --system fastapi \
    && adduser --system --ingroup fastapi fastapi

COPY --chown=fastapi:fastapi ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=fastapi:fastapi ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=fastapi:fastapi . /app

WORKDIR /app
