import modules.vkontakt as vkontakt
import modules.sqlprocessing as sqlprocessing
import config
import time


vk_bot = vkontakt.Bot(config.vk_token, config.vk_server, config.vk_group_id)
db = sqlprocessing.SqlProc(config.db_host, config.db_user, config.db_password, config.db_name)

while True:
    time.sleep(0.5)
    event = vk_bot.wait_for_event()
    print(event)
    db.add_event('events', event, 1)
