# import time
# import RPi.GPIO as GPIO
from gpiozero import PWMLED, DigitalInputDevice, DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import gpiozero.spi_devices

factory = PiGPIOFactory(host="192.168.62.107")
pinOutput = DigitalOutputDevice(pin_factory=factory)
pinInput = DigitalInputDevice(pin_factory=factory)

#gpiozero.DigitalInputDevice(pin, *, pull_up=False, active_state=None, bounce_time=None, pin_factory=None)
# Keypad - Row Pins, output
row1 = DigitalOutputDevice(35, pin_factory=factory)
row2 = DigitalOutputDevice(31, pin_factory=factory)
row3 = DigitalOutputDevice(32, pin_factory=factory)
row4 = DigitalOutputDevice(33, pin_factory=factory)

##gpiozero.DigitalOutputDevice(pin, *, active_high=True, initial_value=False, pin_factory=None)[source]
# Keypad - Column Pins, input
col1 = DigitalInputDevice(36, pull_up=True, pin_factory=factory)
col2 = DigitalInputDevice(37, pull_up=True, pin_factory=factory)
col3 = DigitalInputDevice(38, pull_up=True, pin_factory=factory)
col4 = DigitalInputDevice(40, pull_up=True, pin_factory=factory)

blue = PWMLED(2, pin_factory=factory)


# # Set column pins as input and Pulled up high by default
# GPIO.setup(col1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(col2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(col3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(col4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnOnLED():
    blue.on()


# function to read each row and each column
def readRow():
    if col1.pull_up == False:
        if row1.active_high == False:
            turnOnLED()
        elif row2.active_high == False:
            next        
        elif row3.active_high == False:
            next
        elif row4.active_high == False:
            next
    elif col2.pull_up == False:
        if row1.active_high == False:
            turnOnLED()
        elif row2.active_high == False:
            next        
        elif row3.active_high == False:
            next
        elif row4.active_high == False:
            next
    elif col4.pull_up == False:
        if row1.active_high == False:
            turnOnLED()
        elif row2.active_high == False:
            next        
        elif row3.active_high == False:
            next
        elif row4.active_high == False:
            next
    elif col1.pull_up == False:
        if row1.active_high == False:
            turnOnLED()
        elif row2.active_high == False:
            next        
        elif row3.active_high == False:
            next
        elif row4.active_high == False:
            next

# Endless loop by checking each row 
try:
    while True:
        readRow()
        time.sleep(2) # adjust this per your own setup
        blue.value = 0.01
except KeyboardInterrupt:
    print("\nKeypad Application Interrupted!")
    GPIO.cleanup()