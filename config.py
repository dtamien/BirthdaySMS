import argparse
import logging
import yaml

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Log level.")
parser.add_argument("--config-file", default="config.yaml", help="Path to the configuration file.")
parser.add_argument("--date", help="Date to use for processing (optional). Expected format: 'dd-mm'. Warning: rewrites currentDate.txt.")
args = parser.parse_args()

# set logger
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M', level=args.log_level)
logging.getLogger('twilio.http_client').setLevel(logging.WARNING)
logger = logging.getLogger()
logger.info("Logger set.")

# read config file
with open(args.config_file) as stream:
    config = yaml.safe_load(stream)
    required_keys = ['ACCOUNT_SID', 'AUTH_TOKEN', 'TWILIO_NUMBER', 'PERSONAL_NUMBER']
    for key in required_keys:
        if (key not in config) or (config[key] == None):
            logger.info(f"'{key}' not set in {args.config_file}.")
            exit()
logger.info("Configuration loaded.")
