
# run #

python3 pi-sensor

# auto #

/etc/rc.local

screen -m -d /usr/bin/python3 /home/pi/pi-sensor/py-sensor/ /home/pi/pi-sensor/config.json

# requirements #

requests - python3-requests

