
import logging
import requests
import json

class Thinger(object):
    uriformat = "https://api.thinger.io/v1/users/{user}/buckets/{bucket_id}/data?authorization={auth_key}"
    def __init__(self, user, bucket_id, auth_key):
        self.rest_uri = self.uriformat.format(user=user, bucket_id=bucket_id, auth_key=auth_key)
    def store(self, payload):
        try:
            for name in payload:
                logging.info("Stored: {0} {1}".format(name, payload[name]))
            header = { 'content-type': 'application/json' }
            response = requests.post(self.rest_uri, data=json.dumps(payload), headers=header)
            logging.info("Status: {0}".format(response.status_code))
            logging.info("Response: {0}".format(response.text))
        except Exception as e:
            logging.error(e)

