FROM python:3.12-slim

WORKDIR /app

COPY requirements requirements

RUN apt-get update && \
    xargs -a requirements/apt-packages.txt apt-get install -y --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements/requirements.txt

COPY src src

COPY configs/birthdays.csv configs/birthdays.csv 