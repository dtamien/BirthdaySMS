import argparse
import logging
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Log level.")
parser.add_argument("--config-file", default="config.yaml", help="Path to the configuration file.")
parser.add_argument("--date", help="Date to use for processing (optional). Expected format: 'dd-mm'. Warning: rewrites currentDate.txt.")
args = parser.parse_args()

logging.basicConfig(level=args.log_level)
logging.getLogger('twilio.http_client').setLevel(logging.WARNING)
logger = logging.getLogger()
logger.info("Logger set.")

with open(args.config_file) as stream:
    config = yaml.safe_load(stream)
logger.info("Configuration file read.")
