from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from gpiozero import Button
import requests
from signal import pause
from time import perf_counter

url = "https://penguu.azurewebsites.net/api/DeviceData"
myobj = {"somekey": "somevalue"}
factory = PiGPIOFactory(host="192.168.62.107")
# pins http://abyz.me.uk/rpi/pigpio/index.html#Type_3
# ST7735
# https://www.youtube.com/watch?v=SYdGNpfLxKw
# for i in range(1,30):


def call_api(type: int, value):
    x = requests.post(
        url, json={"SensorUserID": 1, "AlertType": type, "Payload": value}
    )
    print(x.status_code)
    print(value)
    print(f"The button was pressed! {perf_counter():2.1f}")


last_water_alert = 0


def send_water_alert():
    global last_water_alert
    if perf_counter() - last_water_alert > 2:
        last_water_alert = perf_counter()
        call_api(2, f"Bath is overflowing! ({perf_counter():.0f})")


def send_red_button_alert():
    call_api(3, "User is in distress!")


last_disarmed_alert = 0


def send_correct_pin_alert():
    global last_disarmed_alert
    if perf_counter() - last_disarmed_alert > 5:
        last_disarmed_alert = perf_counter()
        call_api(4, "User disarmed Alarm!")


def send_wrong_pin_alert():
    call_api(5, "User entered pin incorrectly!!")


last_motion_alert = 0


def send_motion_alert():
    global last_motion_alert
    if perf_counter() - last_motion_alert > 5:
        last_motion_alert = perf_counter()
        call_api(6, "Movement detected in the bathroom")


button4 = Button(4, pin_factory=factory, pull_up=False)
button4.when_activated = send_water_alert
button14 = Button(14, pin_factory=factory, pull_up=False)
button14.when_activated = send_red_button_alert
button15 = Button(15, pin_factory=factory, pull_up=False)
button15.when_activated = send_correct_pin_alert
button18 = Button(18, pin_factory=factory, pull_up=False)
button18.when_activated = send_wrong_pin_alert
button24 = Button(24, pin_factory=factory, pull_up=False)
button24.when_activated = send_wrong_pin_alert
# while True:
# button.wait_for_press()


pause()
