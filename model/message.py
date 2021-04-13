from psycopg2._psycopg import cursor

from config.dbconfig import pg_config
import psycopg2

class MessageDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" % (
            pg_config['dbname'], pg_config['user'],
            pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def addMessage(self, RegisteredUser, Text):
        cursor = self.conn.cursor()
        query = "insert into posts(uid, pdate, content) values(%s, NOW(), %s)"
        cursor.execute(query, (RegisteredUser, Text))
        self.conn.commit()
        return True

    def replyMessage(self, RegisteredUser, Text, replyingto):
        cursor = self.conn.cursor()
        query = "insert into replies (pid, uid, content) values(%s, %s, %s);"
        cursor.execute(query, (replyingto, RegisteredUser, Text))
        self.conn.commit()
        return True

    def shareMessage(self, RegisteredUser, sharing):
        cursor = self.conn.cursor()
        query = "insert into shares (pid, uid) values(%s, %s);"
        cursor.execute(query, (sharing, RegisteredUser))
        self.conn.commit()
        return True

    def getSpecMessage(self, pid):
        cursor = self.conn.cursor()
        query = "select pid, content, uid, pdate from posts where pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessages(self):
        cursor = self.conn.cursor()
        query = "select pid, content, uid, pdate from posts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result