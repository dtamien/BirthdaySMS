## Getting started

Follow these steps to set up BirthdaySMS and start receiving birthday reminders.

## Step 1: Clone the repository

```bash
git clone git@github.com:dtamien/BirthdaySMS.git
```

## Step 2: Configure your credentials

Sign up for a free Twilio account at https://www.twilio.com/try-twilio.

Update the `config.py` file with your Twilio account information, including your <ins>Account SID</ins>, <ins>Auth Token</ins>, and <ins>Twilio phone number</ins>.

## Step 3: Set up a cronjob
BirthdaySMS is designed to run periodically to check for birthdays and send reminders. You can achieve this by setting up a cron job.

```bash
(echo "0 */1 * * * cd /path/to/BirthdaySMS/ && /usr/bin/python3 main.py") | crontab -
```
This will run the BirthdaySMS script every hour. Make sure to replace `/path/to/BirthdaySMS` with the actual path of BirthdaySMS directory.

Now you're all set to receive reminders on the dates you can configure in `birthdays.json`!
