
import json
import logging
import sys

from service import Service
from thinger import Thinger

config_path = 'config.json'
if len(sys.argv) == 2:
    config_path = sys.argv[1]
print("Config: {0}".format(config_path))

config = {}
with open(config_path) as config_file:
    config = json.load(config_file)

logging.basicConfig(level=logging.DEBUG)

srv = Service(
    config['delay_seconds'], config['sensors'],
    Thinger(config['thinger']['user'], config['thinger']['bucket_id'], config['thinger']['auth_key'])
)
#srv.daemon = True
srv.start()

