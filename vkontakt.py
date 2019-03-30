import requests
import random
import logging
import json

class bot:
    url = "https://api.vk.com/method/"
    server = ""
    key = ""
    ts = ""
    wait = 25
    token = ""
    group_id = ""
    def __init__(self, token, server = None, group_id = None):
        self.server = server
        self.token = token
        self.group_id = group_id

    def getLogpollServer(self):
        r = requests.get(self.url + "groups.getLongPollServer?group_id=" + self.group_id + "&access_token=" + self.token + "&v=5.92")
        print(r.json())
        self.key = r.json()["response"]["key"]
        self.ts = r.json()["response"]["ts"]

    def setToken(self, token):
        self.token = token

    def waitForEvent(self):
        r = requests.get(self.server + "?act=a_check&key=" + self.key + "&ts=" + self.ts + "&wait=" + str(self.wait))
        if r.text.find("failed") != -1:
            self.getLogpollServer()
        else:
            if len(r.json()["updates"]) != 0:
                self.ts = r.json()["ts"]
                return r.text

    def changeWaitTime(self, waitTime):
        self.wait = waitTime

    def sendMsg(self, chatId, message):
        rand_id = str(random.randint(1, 18446744073709551615))
        r = requests.get(self.url + "messages.send?" + "random_id=" + rand_id + "&peer_id=" + chatId + "&message=" + message + "&access_token=" + self.token + "&v=5.92")
        print(r.json())

    def getNameById(self, user_id):
        name = []
        r = requests.get(self.url + "users.get?user_ids=" + str(user_id) + "&access_token=" + self.token + "&v=5.92")
        if(r.text.find('error', 0, 10)) != -1:
            name.append("Error")
            name.append("Name")
            return name
        name.append(r.json()["response"][0]["first_name"])
        name.append(r.json()["response"][0]["last_name"])
        return name