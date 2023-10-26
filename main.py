from config import args, config, logger   
from datetime import datetime
from twilio.rest import Client
import json

# if not specified, date is today's
if args.date:
    date = args.date
else:
    date = format(datetime.now(), "%d-%m")

# checks if the program has ran on date
# if not: seeks for people born on date
# if people and sms are enabled: sends one
# if ran: rewrites currentDate.txt
with open("currentDate.txt", 'r+') as stream:
    if (stream.read() != date) or args.date:
        logger.info(f"Seeking for birthdays.")
        with open("birthdays.json", 'r') as stream2:
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
                        from_ = config['TWILIO_NUMBER'],
                        body = msg,
                        to = config['PERSONAL_NUMBER']
                    )
                else:
                    logger.info(f"Confer to config.yaml to enable SMS.")
            else:
                logger.info(f"It seems like you don't know anyone who was born on the {date}.")
        stream.seek(0)
        stream.truncate()
        stream.write(date)
        logger.info(f"currentDate.txt has been updated.")
    else:
        logger.info(f"BirthdaySMS has already been ran today.")
