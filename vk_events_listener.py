import vkontakt
import sqlprocessing
import config
import time


vk_bot = vkontakt.bot(config.vk_token, config.vk_server, config.vk_group_id)
db = sqlprocessing.sqlproc(config.db_host, config.db_user, config.db_password, config.db_name)

while True:
    time.sleep(0.5)
    event = vk_bot.waitForEvent()
    print(event)
    db.add_event("events", event, 1)