COFFEE_SLACK_CHANNEL = "coffee"
COFFEE_UPDATE_INTERVAL_IN_MS = 10000

COFFEE_FULL_THRESHOLD = 1020000
COFFEE_EMPTY_OR_LOW_THRESHOLD = 810000
COFFEE_FULL_FILENAME = "coffee-full.png"
COFFEE_FULL_MESSAGE = "*HOT COFFEE IS READY!*"
COFFEE_NEEDS_ATTENTION_FILENAME = "coffee-low.png"
COFFEE_NEEDS_ATTENTION_MESSAGE = "**** *WARNING! COFFEE POT IS LOW OR EMPTY* ****"

class Dispatcher():
    def __init__(self, slack_client):
        self.slack_client = slack_client
        
    def get_weight():
        # TODO: Implement this, queue up 20 values and take average of them
            # And see if each value is within 20,000 of the other before 
            # taking the average, if not, trash the whole queue and restart. (Means someone is pumping)
        return 0

    def is_level_low():
        return weight <= COFFEE_EMPTY_OR_LOW_THRESHOLD


    def is_level_high():
        return weight >= COFFEE_FULL_THRESHOLD

    def notify_full():
        self.slack_client.upload_file_to_channel(channelId, COFFEE_FULL_FILENAME)
        self.slack_client.send_message(channelId, COFFEE_FULL_MESSAGE)

    def notify_empty():
        self.slack_client.upload_file_to_channel(channelId, COFFEE_NEEDS_ATTENTION_FILENAME)
        self.slack_client.send_message(channelId, COFFEE_NEEDS_ATTENTION_MESSAGE)
        