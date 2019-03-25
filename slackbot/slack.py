import os
from datetime import datetime
import calendar
from slackclient import SlackClient

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_USER_ACCESS_TOKEN = os.environ.get('SLACK_USER_ACCESS_TOKEN')

class SlackAPIClient(object):
    def __init__(self):
        self.bot_client = SlackClient(SLACK_BOT_TOKEN)
        self.user_client = SlackClient(SLACK_USER_ACCESS_TOKEN)

    def get_bot_auth_token(self):
        return os.environ.get('SLACK_BOT_TOKEN')

    def send_text_message_to_channel(self, message, channel):
        self.bot_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
        )

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

    def mark_message(self, user, time):
        return self.bot_client.api_call("im.mark", channel=user, ts=time)

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
        with open(file_url, errors='ignore') as file_content:
            self.bot_client.api_call(
                "files.upload",
                channels=channel_id,
                file=file_content
            )

    def upload_file_to_user(self):
        pass


doods = ['U9FN8T04D', 'U9FNFPJD6', 'U9F5653J5', 'U9FRS7QBU']

slackClient = SlackAPIClient()



conversations = slackClient.get_direct_messages()

for conversation in conversations["ims"]:
    dmId = conversation["id"]
    convo = slackClient.get_unread_conversations(dmId)
    z = slackClient.get_unread_conversations(conversation["id"])
    count = z["unread_count_display"]

    if count > 0:
        d = datetime.utcnow()
        unixtime = calendar.timegm(d.utctimetuple())
        aa = slackClient.mark_message(dmId, unixtime)
        print("")

    z2 = slackClient.get_unread_conversations(conversation["id"])
    count2 = z["unread_count_display"]
    print("")

print("hello")


# slackClient = SlackAPIClient()
# channelId = slackClient.get_channel_id("doods")
# slackClient.send_text_message_to_channel("yoooo", channelId)
