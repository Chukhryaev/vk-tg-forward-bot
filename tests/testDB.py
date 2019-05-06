import mysql.connector
import config
import logging

log = logging.getLogger(__name__)

db = mysql.connector.connect(
    host=config.db_host,
    user=config.db_user,
    passwd=config.db_password,
    database=config.db_name
)

cursor = db.cursor()
cursor.execute('SHOW TABLES')
for table in cursor:
    log.debug(table)

cursor.close()
db.close()
