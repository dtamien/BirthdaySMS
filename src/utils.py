import logging
import os

from datetime import datetime
import pandas as pd
from twilio.rest import Client


def set_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='/var/log/birthdaysms.log',
    )
    logging.getLogger('twilio.http_client').setLevel(logging.WARNING)
    

def get_date(date_format):
    return datetime.now().strftime(date_format)


def get_last_run_date():
    with open('src/last_run_date.txt', 'r') as f:
        return f.read()


def get_born_on_today():
    month, day = get_date('%m-%d').split('-')
    all_birthdays = pd.read_csv("configs/birthdays.csv")
    return all_birthdays[(all_birthdays['month'] == int(month)) & (all_birthdays['day'] == int(day))]


def send_sms(sms_body):
    client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    client.messages.create(
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        body=sms_body,
        to=os.getenv('PERSONAL_PHONE_NUMBER'),
    )


def update_run_date(ran_date):
    with open('src/last_run_date.txt', 'w') as f:
        f.write(ran_date)
