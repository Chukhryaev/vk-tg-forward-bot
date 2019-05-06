import modules.sqlprocessing as sqlprocessing
import config
import modules.vkontakt as vkontakt
import modules.telegram as telegram


#   MESSAGE TABLE STRUCTURE
#
# 0   ID        set NULL
# 1   FIRST NAME
# 2   LAST NAME
# 3   MSG TEXT
# 4   FORWARD MSG
# 5   ATTACHMENTS
# 6   SOURCE
# 7   CHAT_ID

dataBase = sqlprocessing.SqlProc(config.db_host, config.db_user, config.db_password, config.db_name)
vk_bot = vkontakt.Bot(config.vk_token)
tg_bot = telegram.Bot(config.tg_token)

while True:
    messages = dataBase.fetch_all("messages")
    for message in messages:
        if message[6]:
            tg_bot.send_message(message[7], message[3])
        else:
            vk_bot.send_message(message[7], message[3])
