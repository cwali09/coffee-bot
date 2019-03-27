import time
import sys
import RPi.GPIO as GPIO

sys.path.insert(0, './hx711')
from hx711 import HX711

sys.path.insert(1, './slackbot/')
from slack import SlackClient
from dispatcher import Dispatcher


def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()
hx.tare()
print("Tare done! Add weight now...")

while True:
    try:

        val = hx.get_weight(5)
        print(val)

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
