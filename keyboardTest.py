# import time
# import RPi.GPIO as GPIO
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import gpiozero.spi_devices

factory = PiGPIOFactory(host="192.168.62.107")
pinOutput = gpiozero.DigitalOutputDevice()
pinInput = gpiozero.DigitalInputDevice()

#gpiozero.DigitalInputDevice(pin, *, pull_up=False, active_state=None, bounce_time=None, pin_factory=None)
# Keypad - Row Pins, output
row1 = pinOutput(35)
row2 = pinOutput(31)
row3 = pinOutput(32)
row4 = pinOutput(33)

##gpiozero.DigitalOutputDevice(pin, *, active_high=True, initial_value=False, pin_factory=None)[source]
# Keypad - Column Pins, input
col1 = pinInput(36, pull_up=True)
col2 = pinInput(37, pull_up=True)
col3 = pinInput(38, pull_up=True)
col4 = pinInput(40, pull_up=True)

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
        time.sleep(0.2) # adjust this per your own setup
except KeyboardInterrupt:
    print("\nKeypad Application Interrupted!")
    GPIO.cleanup()