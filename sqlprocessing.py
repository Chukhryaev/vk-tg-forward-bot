import mysql.connector


class sqlproc:
    database = None
    cursor = None
    host = None
    user = None
    password = None
    database_name = None
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name

    def open_connection(self):
        self.database = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=self.database_name
        )
        self.cursor = self.database.cursor()

    def close_connection(self):
        self.cursor.close()
        self.database.close()

    def fetch_all(self, tableName):
        self.open_connection()
        sql = "SELECT * FROM " + tableName
        self.cursor.execute(sql)
        ans = self.cursor.fetchall()
        self.close_connection()
        return ans

    def add_event(self, table_name, response, source):
        self.open_connection()
        values = []
        values.append(None)
        values.append(str(response))
        values.append(source)
        self.cursor.execute("INSERT INTO " + table_name + " VALUES(%s,%s,%s)", values)
        self.database.commit()
        self.close_connection()

    def add_vk_chat(self, table_name, chat_id):
        self.open_connection()
        values = ["NULL", "NULL", str(chat_id)]
        self.cursor.execute("INSERT INTO " + table_name + " VALUES (%s,%s,%s)" , values)
        self.database.commit()
        self.close_connection()

    def add_tg_chat(self, table_name, chat_id):
        self.open_connection()
        values = ["NULL", str(chat_id), "NULL"]
        self.cursor.execute("INSERT INTO " + table_name + " VALUES (%s,%s,%s);", values)
        self.database.commit()
        self.close_connection()

    def is_seen_in_column(self, table_name, column, chat_id):
        self.open_connection()
        sql = "SELECT * FROM " + table_name + " WHERE " + str(column) + " = " + str(chat_id)
        self.cursor.execute(sql)
        ans_len = len(self.cursor.fetchall())
        self.close_connection()
        return ans_len

    def delete_row_by_id(self, table_name, id):
        self.open_connection()
        sql = "DELETE FROM " + table_name + " WHERE id = " + str(id)
        self.cursor.execute(sql)
        self.database.commit()
        self.close_connection()

    def link_chats(self, table_name, source_chat_id, chat_id, source):
        self.open_connection()
        if source == 0:
            sql = "SELECT * FROM " + table_name + " WHERE " + "vk_chat_id" + " = " + str(chat_id) + " AND tg_chat_id = NULL"
            self.cursor.execute(sql)
            fetch = self.cursor.fetchall()
            if len(fetch) == 1:
                sql = "UPDATE " + table_name + " SET vk_chat_id = " + str(chat_id) + " WHERE tg_chat_id = " + str(source_chat_id)
                self.cursor.execute(sql)
                self.database.commit()
                self.delete_row_by_id(table_name, fetch[0])
                self.close_connection()
                return 0
            else:
                self.close_connection()
                return 1

        elif source == 1:
            sql = "SELECT * FROM " + table_name + " WHERE " + "vk_chat_id = NULL" + " AND tg_chat_id = " + str(chat_id)
            self.cursor.execute(sql)
            fetch = self.cursor.fetchall()
            if len(fetch) == 1:
                sql = "UPDATE " + table_name + " SET tg_chat_id = " + str(chat_id) + " WHERE vk_chat_id = " + str(source_chat_id)
                self.cursor.execute(sql)
                self.database.commit()
                self.delete_row_by_id(table_name, fetch[0])
                self.close_connection()
                return 0
            else:
                self.close_connection()
                return 1
        self.close_connection()
        return 2

    def addMessage(self, table_name, first_name, last_name, msg_text, forward_msg, attachments, source, chat_id):
        self.open_connection()
        values = [0, str(first_name), str(last_name), str(msg_text), str(forward_msg), str(attachments), str(source), str(chat_id)]
        self.cursor.execute("INSERT INTO " + table_name + " VALUES (%s,%s,%s,%s,%s,%s,%s,%s);", values)
        self.database.commit()
        self.close_connection()

    def is_connected(self, table_name, column, chat_id):
        self.is_seen_in_column()







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