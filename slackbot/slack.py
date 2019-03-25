import os
import time
from slackclient import SlackClient

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_USER_ACCESS_TOKEN = os.environ.get('SLACK_USER_ACCESS_TOKEN')

class SlackAPIClient(object):
    def __init__(self):
        self.bot_client = SlackClient(SLACK_BOT_TOKEN)
        self.user_client = SlackClient(SLACK_USER_ACCESS_TOKEN)

    def get_bot_auth_token(self):
        return os.environ.get('SLACK_BOT_TOKEN')

    def send_message(self, channel, message):
        self.bot_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
        )

    def join_channel(self, name):
        return self.bot_client.api_call("channels.join", name=name)

    def get_direct_messages(self):
        return self.bot_client.api_call("im.list")

    def open_conversation(self, user):
        return self.bot_client.api_call("im.open", user=user)

    def leave_conversation(self, channel):
        return self.bot_client.api_call("im.close", channel=channel)

    def get_unread_conversations(self, channel):
        return self.bot_client.api_call("im.history", channel=channel, unreads=True)

    def get_direct_message_history(self, channel):
        return self.bot_client.api_call("conversations.history", channel=channel)

    def get_all_users(self):
        return self.bot_client.api_call("users.list")
    
    def get_user_id(self, user_name):
        users = self.get_all_users()['members']
        for user in users:
            if user["name"] == user_name:
                return user["id"]
        return ""

    
    def get_channel_id(self, channel_name):
        channel_id = None
        channels = self.bot_client.api_call("channels.list")["channels"]
        for channel in channels:
            if channel['name'] == channel_name:
                channel_id = channel['id']
                break
        return channel_id

    def upload_file_to_channel(self, channel_id, file_url):
        with open(file_url, 'rb') as file_content:
            self.bot_client.api_call(
                "files.upload",
                channels=channel_id,
                file=file_content
            )

    def upload_content(self, channel, filename, file):
        return self.bot_client.api_call("files.upload", channel=channel, filename=filename, file=file)

    def upload_file_to_user(self):
        pass

def update():
    # TODO:
    #     1) Check reading from device & if reading > threshold display message && hasn't notified channel about this
    slackClient.send_message(COFFEE_SLACK_CHANNEL, "Wali/Glen Coffee Bot v1.0")
    return

def notify_full():
    channel = slackClient.get_channel_id(COFFEE_SLACK_CHANNEL)
    slackClient.upload_file_to_channel(channel, COFFEE_FULL_FILENAME)

def notify_empty():
    channel = slackClient.get_channel_id(COFFEE_SLACK_CHANNEL)
    slackClient.upload_file_to_channel(channel, COFFEE_NEEDS_ATTENTION_FILENAME)


COFFEE_FULL_THRESHOLD = 50000000
COFFEE_EMPTY_OR_LOW_THRESHOLD = 0
COFFEE_FULL_FILENAME = "coffee-full.png"
COFFEE_NEEDS_ATTENTION_FILENAME="coffee-low.png"

COFFEE_SLACK_CHANNEL = "coffee"
COFFEE_UPDATE_INTERVAL_IN_MS = 10000

slackClient = SlackAPIClient()

while True:
    #
    # read scale, if reading is empty or full, send notification.
    #
    # var weight = get_weight();
    # if (IsLow(weight) && is_high)     if is_high initial value is true
    #    is_high = false;
    #    is_low = true
    #    notify_empty();
    #
    # if (IsHigh(weight) && is_low)
    #    is_low = false;
    #    is_high = true;
    #    notify_full();
    #



    time.sleep(COFFEE_UPDATE_INTERVAL_IN_MS)
