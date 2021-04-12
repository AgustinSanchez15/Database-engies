from config.dbconfig import pg_config
import psycopg2

class BlockDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" % (
            pg_config['dbname'], pg_config['user'],
            pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def blockUser(self, RegisteredUser, uid):
        cursor = self.conn.cursor()
        query = "insert into blocks (buid, uid) values (%s,%s)"
        cursor.execute(query, (RegisteredUser, uid))
        self.conn.commit()
        return True

    def getBlocked(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, uname from users natural inner join (select buid from blocks where uid = 1) as buid where buid=uid;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBlocking(self,uid):
        cursor = self.conn.cursor()
        query = "select uid, uname from users natural inner join (select uid from blocks where buid = %s) as uid;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def unblock(self, uid, RegisteredUser):
        cursor = self.conn.cursor()
        query = "delete from blocks where buid=%s and uid=%s"
        cursor.execute(query, (uid, RegisteredUser))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows != 0