FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY birthdays.json .
COPY config.py .
COPY config.yaml .
COPY main.py .
COPY currentDate.txt .

CMD ["python", "main.py"]