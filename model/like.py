from config.dbconfig import pg_config
import psycopg2

class LikeDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-54-224-120-186.compute-1.amazonaws.com'" % (
            pg_config['dbname'], pg_config['user'],
            pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def insertLike(self, pid, RegisteredUser):
        cursor = self.conn.cursor()
        query = "delete from dislikes where pid=%s and uid=%s"
        cursor.execute(query, (pid, RegisteredUser))
        query = "insert into likes (pid, uid) values (%s,%s)"
        cursor.execute(query, (pid, RegisteredUser))
        self.conn.commit()
        return True

    def removeLike(self, pid, RegisteredUser):
        cursor = self.conn.cursor()
        query = "delete from likes where pid=%s and uid=%s"
        cursor.execute(query, (pid, RegisteredUser))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows != 0

    def getLiked(self, pid):
        cursor = self.conn.cursor()
        query = "select uid, uname from users natural inner join (select uid from likes where pid = %s) as uid;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertUnlike(self, pid, RegisteredUser):
        cursor = self.conn.cursor()
        query = "delete from likes where pid=%s and uid=%s"
        cursor.execute(query, (pid, RegisteredUser))
        query = "insert into dislikes (pid, uid) values (%s,%s)"
        cursor.execute(query, (pid, RegisteredUser))
        self.conn.commit()
        return True

    def removeUnlike(self, pid, RegisteredUser):
        cursor = self.conn.cursor()
        query = "delete from dislikes where pid=%s and uid=%s"
        cursor.execute(query, (pid, RegisteredUser))
        affected_rows = cursor.rowcount
        self.conn.commit()
        return affected_rows != 0

    def getUnliked(self, pid):
        cursor = self.conn.cursor()
        query = "select uid, uname from users natural inner join (select uid from dislikes where pid = %s) as uid;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result