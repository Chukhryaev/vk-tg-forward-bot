import sqlprocessing
import config
import vkontakt
import telegram

#   MESSAGE TABLE STRUCTURE
#
#   ID        set NULL
#   FIRST NAME
#   LAST NAME
#   MSG TEXT
#   FORWARD MSG
#   ATTACHMENTS
#   SOURCE
#   CHAT_ID


class worker:
    dataBase = None
    vk_bot = None
    tg_bot = None
    def __init__(self):
        self.dataBase = sqlprocessing.sqlproc(config.db_host, config.db_user, config.db_password, config.db_name)
        self.vk_bot = vkontakt.bot(config.vk_token)
        self.tg_bot = telegram.bot(config.tg_token)
        print("worker working =)")

    def actionExecuting(self, msgObject):
        peer_id = str(msgObject["peer_id"])
        if msgObject["action"]["member_id"] == -177210709:
            self.vk_bot.sendMsg(peer_id, "YOUR CHAT ID TO USE TELEGRAM IS " + peer_id + "IF YOU ALREDY HAVE TG CHAT WITH BOT WRITE /CONNECT TelegramChatId")
            if self.dataBase.is_seen_in_column("chats", "vk_chat_id", peer_id) == 0:
                self.dataBase.add_vk_chat("chats", peer_id)
            else:
                self.vk_bot.sendMsg(peer_id, "WE ALREADY HAVE YOUR CHAT IN DB")
        else:
            name = self.vk_bot.getNameById(msgObject["action"]["member_id"])
            self.dataBase.addMessage("messages", "CHAT", "INFO", "Added new chat member " + name[0] + " " + name[1], None, None, "vk", peer_id)

    def linkTelegramChat(self, msgObject):
        peer_id = str(msgObject["peer_id"])
        chat_id = msgObject["text"][7:].strip(" ")
        response = self.dataBase.link_chats("chats", peer_id, chat_id, 1)
        if response == 0:
            self.vk_bot.sendMsg(peer_id, "Chat " + str(chat_id) + " linked to ur chat")
        elif response == 1:
            self.vk_bot.sendMsg(peer_id, "Chat " + str(chat_id) + " already linked to ur chat or another one")
        else:
            self.vk_bot.sendMsg(peer_id, "Chat " + str(chat_id) + " wanted to link yours but something went wrong, help us fix it sending to us messsage with such ussue")

    def linkVkChat(self, msgObject):
        chat_id = str(msgObject["chat"]["id"])
        peer_id = msgObject["text"][7:].strip(" ")
        response = self.dataBase.link_chats("chats", peer_id, chat_id, 0)
        if response == 0:
            self.tg_bot.send_message(chat_id, "Chat " + str(peer_id) + " linked to ur chat")
        elif response == 1:
            self.vk_bot.sendMsg(chat_id, "Chat " + str(peer_id) + " already linked to ur chat or another one")
        else:
            self.vk_bot.sendMsg(chat_id, "Chat " + str(peer_id) + " wanted to link yours but something went wrong, help us fix it sending to us messsage with such ussue")

    def msgExecuting(self, msgObject):
        peer_id = msgObject["peer_id"]
        from_id = msgObject["from_id"]
        name = []
        name = self.vk_bot.getNameById(from_id)
        if peer_id == from_id():
            print("")
            #maybe do something with it
        text = msgObject["text"]
        attachments = msgObject["attachments"]
        fwd_messages = msgObject["fwd_messages"]
        #   process fwd_message
        self.dataBase.addMessage("messages", name[0], name[1], text, fwd_messages, attachments, "vk", peer_id)

    def vk_event_parse(self, event):
        None


    def tg_processing_event(self, event):
        UPDATE = self.tg_event_parse(event)
        chat_id = UPDATE['update']['chat']['id']
        is_connected = self.dataBase.is_connected("chats", "tg_chat_id", chat_id)
        #Search for new chats_member
        if UPDATE['update']['new_chat_member'] != None:
            if str(UPDATE['update']['new_chat_member']['user']['user']["id"]) == config.tg_chat_id:
                #   ОТПРАВЛЯТЬ В БАЗУ ДАННЫХ И В ГЕНЕРАТОР СООБЩЕНИЙ!!!
                self.tg_bot.send_message(chat_id, "Бот добавлен, ID вашего чата " + chat_id)
                if self.dataBase.is_seen_in_column("chats", "tg_chat_id", chat_id) == 0:
                    self.dataBase.add_tg_chat("chats", chat_id)
            else:
                if is_connected == 1:
                    #   ОТПРАВЛЯТЬ В ГЕНЕРАТОР СООБЩЕНИЙ И СОХРАНЯТЬ В БД
                    None
        elif UPDATE['update']['message']['message']['text'] != None:
            if is_connected == 1:
                #   MESSAGE GENERATOR DB
                None



    def tg_event_parse(self, event):
        #update_id = event["update_id"]
        UPDATE = {}
        message = {'message':None}
        chat = {'chat':None}
        new_chat_member = {'new_chat_member':None}
        #new_chat_members = []
        #is_edited = 0
        if 'message' in event:
            message = {'message':self.tg_message_parse(event["message"])}
        if 'chat' in event:
            chat = {'chat':self.tg_chat_parse(event["chat"])}
        if 'new_chat_member' in event:
            new_chat_member = {'new_chat_member':self.tg_user_parse(event['new_chat_member'])}
#        if 'edited_message' in event:
#            message = self.tg_message_parse(event["edited_message"])
#            is_edited = 1
        UPDATE = {'update':{message, chat, new_chat_member}}
        return UPDATE

    def tg_message_parse(self, messageObj):
        MSG = {'message':None}
        user = {'user':None}
        text = {'text':None}
        if 'from' in messageObj:
            user = {'user':self.tg_user_parse(messageObj["from"])}
        if 'text' in messageObj:
            text = {'text':messageObj["text"]}
        MSG = {'message':{user, text}}
        return MSG

    def tg_user_parse(self, userObj):
        USER = {'user':None}
        id = {'id':None}
        first_name = {'first_name':None}
        last_name = {'last_name':None}
        username = {'username':None}
        if 'id' in userObj:
            id = {'id':userObj["id"]}
        if 'first_name' in userObj:
            first_name = {'first_name':userObj["first_name"]}
        if 'last_name' in userObj:
            last_name = {'last_name':userObj["last_name"]}
        if 'username' in userObj:
            username = {'username':userObj["username"]}
        USER = {'user':{id, first_name, last_name, username}}
        return USER

    def tg_chat_parse(self, chatObj):
        CHAT = {}
        id = {'id':None}
        if 'id' in chatObj:
            id = {'id':chatObj["id"]}
        CHAT = {'chat':{id}}
        return CHAT

