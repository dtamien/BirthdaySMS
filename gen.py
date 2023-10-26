import json
import logging

# avoid accidental generation
security = "enabled"

if security == "enabled":
    logging.warning("Security is enabled. Please disable it if you want to regenerate the file.")
else:
    # generate all date as empty
    data = {}
    for m in range(1, 13):
        month = str(m).zfill(2)
        for d in range(1, 32):
            day = str(d).zfill(2)
            date = f"{day}-{month}"
            data[date] = ""
    # write dates dictionnary into birthdays.json
    with open("birthdays.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    logging.warning(f"birthdays.json writen.")
