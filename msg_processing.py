import sqlprocessing
import config
import vkontakt
import telegram


#   MESSAGE TABLE STRUCTURE
#
#0   ID        set NULL
#1   FIRST NAME
#2   LAST NAME
#3   MSG TEXT
#4   FORWARD MSG
#5   ATTACHMENTS
#6   SOURCE
#7   CHAT_ID

dataBase = sqlprocessing.sqlproc(config.db_host, config.db_user, config.db_password, config.db_name)
vk_bot = vkontakt.bot(config.vk_token)
tg_bot = telegram.bot(config.tg_token)

while True:
    messages = dataBase.fetch_all("messages")
    for i in range(len(messages)):
        message = messages[i]
        if message[6] == 0:
            tg_bot.send_message(message[7], message[3])
        else:
            vk_bot.sendMsg(message[7], message[3])

