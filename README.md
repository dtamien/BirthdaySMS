# BirthdaySMS

BirthdaySMS is a Python appication that sends you SMS reminders for the birthdays you configure.

## Table of contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Debug](#debug)
- [License](#license)

## Prerequisites

- Docker and Docker Compose installed on your machine (https://docs.docker.com/get-docker/).
- A Twilio account with credits and an active phone number (https://www.twilio.com/try-twilio).

*Nota bene: Twilio offers a free trial with a $15.50 credit, which is enough to send 100 SMS messages in France.*

## Setup

1. Clone and navigate to the repository.

    ```bash
    git clone https://github.com/dtamien/BirthdaySMS && cd BirthdaySMS
    ```

2. Set the birthdays you want to be reminded of in the [configs/birthdays.csv](configs/birthdays.csv) file. For instance:

    ```csv
    month,day,year,name
    02,24,2005,Mathias
    08,30,2000,Damien
    11,20,2002,Raphaël
    ```

3. Update the [configs/credentials.env](configs/credentials.env) file with your personal phone number and Twilio account information. For instance:

    ```env
    PERSONAL_PHONE_NUMBER=+33689XXXXXX
    TWILIO_ACCOUNT_SID=AC9109XXXXXXXXXXXXXXXXXXXXXXXXXXXX
    TWILIO_AUTH_TOKEN=49e813XXXXXXXXXXXXXXXXXXXXXXXXXX
    TWILIO_PHONE_NUMBER=+13343XXXXXX
    ```

4. Build the Docker image and start a container based on it.

    ```bash
    docker compose -f docker/docker-compose.yml up -d
    ```

You should now receive reminders for the birthdays you configured.

## Debug

- To check the logs of the application, either print the logs of the running container:

    ```bash
    docker logs -f birthdaysms
    ```

    or restart a new container, not in detached mode:

    ```bash
    docker compose -f docker/docker-compose.yml up
    ```

- If you were to update the code, you'd have to rebuild the Docker image:

    ```bash
    docker compose -f docker/docker-compose.yml up --build -d
    ```

## License

This project is released under a custom license. For full terms and conditions, please refer to the [LICENSE](LICENSE) file.
