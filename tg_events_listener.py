import telegram
import sqlprocessing
import config
import time


tg_bot = telegram.bot(config.tg_token)

db = sqlprocessing.sqlproc("localhost", config.db_user, config.db_password, config.db_name)

while True:
    time.sleep(0.5)
    updates = tg_bot.event_listener()
    db.add_event("events", updates, 0)
    print(updates)


