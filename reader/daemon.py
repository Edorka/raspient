import simpledaemon
import logging
import requests
import Adafruit_DHT
import time


class Ambient:

    def __init__(self, sensor, pin):
        self.sensor = Adafruit_DHT.AM2302
        self.pin = pin
    
    def retrieve(self):
	return Adafruit_DHT.read_retry(self.sensor, self.pin)


class ReaderDaemon(simpledaemon.Daemon):
    default_conf = './reader.conf'
    section = 'reader'
    can_continue = True
    delay = 300

    def run(self):
        api_key = self.config_parser.get(self.section, 'api_key')
        sensor = self.config_parser.get(self.section, 'sensor')
        receiver = self.config_parser.get(self.section, 'receiver')
        pin = self.config_parser.get(self.section, 'pin')
	sensor = Ambient(sensor, pin)
        while self.can_continue:
            humidity, temperature = sensor.retrieve()
            reading = {'humidity': humidity, 'temperature': temperature}
            reading['source_id'] = 1
            logging.info('got %f, %f' % (temperature, humidity) )
            requests.post(receiver, json=reading)
            time.sleep(self.delay)
            

if __name__ == '__main__':
    ReaderDaemon().main()
