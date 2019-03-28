import os
import settings
from slackclient import SlackClient


class SlackbotClient(object):
    def __init__(self):
        self.bot_client = SlackClient(settings.SLACK_BOT_TOKEN)
        self.user_client = SlackClient(settings.SLACK_USER_ACCESS_TOKEN)

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
