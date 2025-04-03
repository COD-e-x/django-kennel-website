FROM python:3.13-slim

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc \
    libjpeg-dev libxslt-dev \
    libpq-dev python3-dev gettext \
    neovim && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

WORKDIR /app

COPY --chown=appuser:appuser . .

RUN pip install -r requirements.txt

USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kennel.wsgi:application"]
