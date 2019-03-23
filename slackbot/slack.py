import os
from chardet import detect
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

    def send_slack_message_to_user(self, message, user_id):
        print(self.bot_client.api_call(
            "conversations.open",
            users=user_id
        ))

    def get_all_users(self):
        return self.bot_client.api_call("users.list")
    
    def get_user_id(self, user_name):
        users = self.get_all_users()['members']
        for user in users:
            if (user["name"] == user_name):
                return user["id"]
        return ""

    
    def get_channel_id(self, channel_name):
        channel_id = None
        channels = self.bot_client.api_call("channels.list")["channels"]
        for channel in channels:
            if (channel['name'] == channel_name):
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

SlackAPIClient().send_slack_message_to_user("hi", "UB53BPB44")

#print(SlackAPIClient().client.token)