import logging

from utils import (
    set_logging,
    get_date,
    get_last_run_date,
    get_born_on_today,
    send_sms,
    update_run_date,
)


def main():    
    run_date = get_date('%m-%d')
    if get_last_run_date() == run_date:
        return logging.info('The program has already run today')
    
    born_on_today = get_born_on_today()
    if born_on_today.empty:
        return logging.info("No birthdays on today")
    
    names, birth_years = born_on_today['name'].tolist(), born_on_today['year'].tolist()
    current_year = int(get_date('%Y'))
    sms_body = " ".join([f"{name} turns {current_year - birth_year} today." for name, birth_year in zip(names, birth_years)])
    logging.info(sms_body)

    try:
        send_sms(sms_body)
        return logging.info('SMS sent successfully')
    except Exception as e:
        return logging.error(f"Error sending SMS: {e}")
    finally:
        update_run_date(run_date)


if __name__ == "__main__":
    set_logging()
    main()
