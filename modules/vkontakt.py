import requests
import random
import logging
# import json

log = logging.getLogger(__name__)


class Bot:
    url = 'https://api.vk.com/method/'
    server = ''
    key = ''
    ts = ''
    wait = 25
    token = ''
    group_id = ''

    def __init__(self, token, server=None, group_id=None):
        self.server = server
        self.token = token
        self.group_id = group_id

    def get_long_poll_server(self):
        r = requests.get(f"{self.url}groups.getLongPollServer?group_id={self.group_id}&access_token={self.token}&v=5.92")
        print(r.json())
        self.key = r.json().get('response').get('key')
        self.ts = r.json().get('response').get('ts')

    def set_token(self, token):
        self.token = token

    def wait_for_event(self):
        r = requests.get(f"{self.server}?act=a_check&key={self.key}&ts={self.ts}&wait={self.wait}")
        if r.text.find("failed") != -1:
            self.get_long_poll_server()
        else:
            if len(r.json().get('updates')) != 0:
                self.ts = r.json().get('ts')
                return r.text

    def change_wait_time(self, wait_time):
        self.wait = wait_time

    def send_message(self, chat_id, message):
        rand_id = str(random.randint(1, 18446744073709551615))
        r = requests.get(f"{self.url}messages.send?random_id={rand_id}&peer_id={chat_id}&message={message}&access_token={self.token}&v=5.92")
        print(r.json())

    def get_name_by_id(self, user_id):
        name = []
        r = requests.get(f"{self.url}users.get?user_ids={user_id}&access_token={self.token}&v=5.92")
        if(r.text.find('error', 0, 10)) != -1:
            name.append("Error")
            name.append("Name")
            return name
        name.append(r.json().get('response')[0].get('first_name'))
        name.append(r.json().get('response')[0].get('last_name'))
        return name
