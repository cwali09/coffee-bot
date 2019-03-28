import time
import sys
import settings
import RPi.GPIO as GPIO

from hx711 import HX711
from slackbot import SlackbotClient


def get_weight():
    return hx.get_steady_weight()


def is_level_low():
    return weight <= settings.COFFEE_EMPTY_OR_LOW_THRESHOLD


def is_level_high():
    return weight >= settings.COFFEE_FULL_THRESHOLD


def notify_full():
    slackbotClient.upload_file_to_channel(channelId, settings.COFFEE_FULL_FILENAME)
    slackbotClient.send_message(channelId, settings.COFFEE_FULL_MESSAGE)


def notify_empty():
    slackbotClient.upload_file_to_channel(channelId, settings.COFFEE_NEEDS_ATTENTION_FILENAME)
    slackbotClient.send_message(channelId, settings.COFFEE_NEEDS_ATTENTION_MESSAGE)


def cleanup():
    GPIO.cleanup()
    print("Exiting...")
    sys.exit()


print(f'Coffeebot v{settings.VERSION} by Wali and Glen')

slackbotClient = SlackbotClient()
channelId = slackbotClient.get_channel_id(settings.COFFEE_SLACK_CHANNEL)

is_high = True
is_low = True
weight = -1

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()

print("Taring scale... make sure nothing is on it.")
hx.tare()
print("Tare complete...")
print("Coffeebot started.")


while True:
    try:
        weight = get_weight()

        print(weight)

        if weight == -1:
            continue

        if is_level_low() and is_high:
            is_high = False
            is_low = True
            notify_empty()

        if is_level_high() and is_low:
            is_low = False
            is_high = True
            notify_full()

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanup()
