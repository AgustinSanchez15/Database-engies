from config.dbconfig import pg_config
import psycopg2


class FollowersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-54-224-120-186.compute-1.amazonaws.com'" % (
            pg_config['dbname'], pg_config['user'],
            pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def insertFollowers(self, uid, fuid):
        cursor = self.conn.cursor()
        query= "insert into followers (uid, fuid) values (%s,%s)"
        cursor.execute(query, (uid, fuid))
        self.conn.commit()
        return fuid

    def checkBlock(self, uid, fuid):
        cursor = self.conn.cursor()
        query = "select uid, buid from blocks where uid=%s and buid=%s"
        cursor.execute(query, (uid, fuid))
        uid = cursor.fetchone()
        return uid

    def getFollowing(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, uname from followers natural inner join users where fuid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFollowers(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, uname from users natural inner join(select fuid from followers where uid=%s) as fuid where uid=fuid;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertUnfollowing(self, uid, fuid):
        cursor = self.conn.cursor()
        query = "delete from followers where uid=%s and fuid=%s"
        cursor.execute(query, (uid, fuid))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows != 0