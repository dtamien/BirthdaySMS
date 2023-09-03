import json
import logging

filename = "birthdays.json"
security = "enabled"

match security:
    case "enabled":
        logging.warning("Security is enabled. Please disable it if you want to regenerate the file.")
    case _:
        data = {}
        for m in range(1, 13):
            month = str(m).zfill(2)
            for d in range(1, 32):
                day = str(d).zfill(2)
                date = f"{day}-{month}"
                data[date] = ""
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logging.warning(f"{filename} writen.")
