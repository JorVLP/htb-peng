from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import gpiozero.spi_devices
gpiozero.spi_devices
import adafruit_ssd1351
adafruit_ssd1351.SSD1351()

factory = PiGPIOFactory(host="192.168.62.107")
# pins http://abyz.me.uk/rpi/pigpio/index.html#Type_3
# ST7735
# https://www.youtube.com/watch?v=SYdGNpfLxKw
# for i in range(1,30):
blue = PWMLED(2, pin_factory=factory)

blue.on()
sleep(1)
blue.value = 0.01