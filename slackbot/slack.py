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

'''

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
    slackClient.upload_file_to_channel(channelId, COFFEE_FULL_FILENAME)
    slackClient.send_message(channelId, COFFEE_FULL_MESSAGE)


def notify_empty():
    slackClient.upload_file_to_channel(channelId, COFFEE_NEEDS_ATTENTION_FILENAME)
    slackClient.send_message(channelId, COFFEE_NEEDS_ATTENTION_MESSAGE)


slackClient = SlackAPIClient()
channelId = slackClient.get_channel_id(COFFEE_SLACK_CHANNEL)

is_high = True
is_low = False
weight = 0

# TODO:
    # New up the HX711 then tare it
    
while True:
    weight = get_weight()

    if is_level_low():
        is_high = False
        is_low = True
        notify_empty()

    if is_level_high():
        is_low = False
        is_high = True
        notify_full()

    time.sleep(COFFEE_UPDATE_INTERVAL_IN_MS)

'''