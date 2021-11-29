
import logging
import time
from threading import Thread
from datetime import datetime

from sensor import Sensor

class Service(Thread):
    def __init__(self, delay_seconds, sensors_config, storage):
        Thread.__init__(self)
        self.delay_seconds = delay_seconds
        self.sensors = {}
        for sensor_config in sensors_config:
            self.sensors[sensor_config['name']] = Sensor(sensor_config['serial'], sensor_config['temp_adj'])
        self.storage = storage
        self.running = True
    def run(self):
        while self.running:
            logging.info("{0}".format(datetime.now()))
            temperatures = {}
            for name in self.sensors:
                temperature = self.sensors[name].temperature()
                if temperature == None:
                    logging.error("Could not get temperature")
                else:
                    temperatures[name] = temperature
            self.storage.store(temperatures)
            time.sleep(self.delay_seconds)

