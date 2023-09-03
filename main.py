from config import args, config, logger   
from datetime import datetime
from twilio.rest import Client
import json

DATEFORMAT = "%d-%m"

if args.date:
    date = args.date
else:
    date = format(datetime.now(), DATEFORMAT)

with open(config['DATE_FILE'], 'r+') as stream:
    if (stream.read() != date) or args.date:
        logger.info(f"Seeking for birthdays.")
        with open(config['BIRTHDAYS_FILE'], 'r') as stream2:
            try:
                people = json.load(stream2)[date]
            except:
                logger.error("Invalid date format. Please use the format DD-MM.")
                exit(1)
            if people:
                msg = f"{config['SMS_BODY']} {people}"
                logger.info(msg)
                if config['SEND_SMS']:
                    logger.info(f"An SMS is on its way.")
                    client = Client(config['ACCOUNT_SID'], config['AUTH_TOKEN'])
                    client.messages.create(
                        from_ = config['MY_TWILIO_NUMBER'],
                        body = msg,
                        to = config['MY_PERSONAL_NUMBER']
                    )
                else:
                    logger.info(f"Confer to config.yaml to enable SMS.")
            else:
                logger.info(f"It seems you don't know anyone who was born on the {date}.")
        stream.seek(0)
        stream.truncate()
        stream.write(date)
        logger.info(f"{config['DATE_FILE']} has been updated.")
    else:
        logger.info(f"The process has already been run today.")
