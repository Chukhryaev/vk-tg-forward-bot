import requests
# import json


class Bot:
    url = 'https://api.telegram.org/bot'
    offset = '0'

    def __init__(self, token):
        self.url = self.url + token + '/'

    def get_me(self):
        r = requests.get(self.url + 'getMe')
        print(r.text)

    def event_listener(self, timeout=20):
        r = requests.get(self.url + 'getUpdates?offset=' + self.offset + '&timeout=' + str(timeout))
        ans = r.text
        r = r.json()
        if r.get('ok'):
            number_of_updates = len(r['result'])
            if number_of_updates != 0:
                self.offset = str(r['result'][number_of_updates - 1]['update_id'] + 1)
                return ans
        else:
            print('Something went wrong!')
            self.event_listener(timeout)

    def send_message(self, chat_id, text):
        r = requests.get(self.url + 'sendMessage?chat_id=' + str(chat_id) + '&text=' + str(text))
        return r
