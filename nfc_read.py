#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

url = "https://penguu.azurewebsites.net/api/DeviceData"
reader = SimpleMFRC522()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

try:
    while True:
        GPIO.output(16, 0)
        id, text = reader.read()
        GPIO.output(16, 0.5)
        if id not in {658266036468, 184645526600} and text == "":
            if id == 567633569746:
                text = "Laura's Access Card"
            elif id == 1022001716616:
                text = "Pauline's Access Card"
            else:
                text = "Access Card"
        x = requests.post(
            url, json={"SensorUserID": 1, "AlertType": 1, "Payload": text}
        )
        print(x.status_code)
        print(id)
        print(f"{text}")
finally:
    GPIO.cleanup()
