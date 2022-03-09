
# run #

python3 pi-sensor

# auto #

/etc/rc.local

screen -m -d /usr/bin/python3 /home/pi/pi-sensor/pi-sensor/ /home/pi/pi-sensor/config.json

# requirements #

requests - python3-requests

flask - python3-flask

# web #

export FLASK_APP=web
flask run --host=0.0.0.0

