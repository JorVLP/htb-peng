from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from gpiozero import Button
import requests

url = "https://penguu.azurewebsites.net/DeviceData"
myobj = {'SensorUserId': 'somevalue',}
factory = PiGPIOFactory(host="192.168.62.107")
# pins http://abyz.me.uk/rpi/pigpio/index.html#Type_3
# ST7735
# https://www.youtube.com/watch?v=SYdGNpfLxKw
# for i in range(1,30):
blue = PWMLED(2, pin_factory=factory)

button = Button(17,  pin_factory=factory, pull_up=True)

def write():
    
while True:
    button.wait_for_press()

    x = requests.post(url, json = myobj)
    print(x.status_code)
    print("The button was pressed!")
    blue.on()
    sleep(1)
    blue.value = 0.01