from mysql import connector
import config
import logging

log = logging.getLogger(__name__)

# create database
db = connector.connect(
    host=config.db_host,
    user=config.db_user,
    passwd=config.db_password
    )

cursor = db.cursor()

cursor.execute(f'CREATE DATABASE {config.db_name}')

cursor.execute('SHOW DATABASES')

for database in cursor:
    log.debug(database)

cursor.close()
db.close()

# create tables
db = mysql.connector.connect(
    host=config.db_host,
    user=config.db_user,
    passwd=config.db_password,
    database=config.db_name
    )

cursor = db.cursor()

cursor.execute(
    'CREATE TABLE tokens ('
    'ID BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,'
    'token_1 VARCHAR(20),'
    'token_2 VARCHAR(20)'
    'SelfID VARCHAR(20)'
    'DestID VARCHAR(20)'
    'Date '
    'Source BOOL NOT NULL)'
    )

cursor.execute(
    'CREATE TABLE chats ('
    'ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,'
    'TgChatID VARCHAR(20) DEFAULT NULL,'
    'VkChatID VARCHAR(20) DEFAULT NULL,'
    'IsConnected BOOL NOT NULL DEFAULT 0)'
    )

cursor.execute('SHOW TABLES')

for table in cursor:
    log.debug(table)

cursor.close()
db.close()

