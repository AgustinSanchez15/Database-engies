from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" % (
            pg_config['dbname'], pg_config['user'],
            pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def addUser(self, uname, upassword, fname, lname, followers):
        cursor = self.conn.cursor()
        query = "insert into users (uname, upassword, fname, lname, followers)" \
                "values (%s, %s, %s, %s, %s) returning uid"
        cursor.execute(query, (uname, upassword, fname, lname, followers))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def updateUser(self, uid, uname, upassword, fname, lname, followers):
        cursor = self.conn.cursor()
        query = "update users (uname, upassword, fname, lname, followers) where uid=%s "
        cursor.execute(query, (uname, upassword, fname, lname, followers, uid))
        self.conn.commit()
        return True

    def deleteUser(self, uid):
        cursor = self.conn.cursor()
        query = "delete from users where uid=%s"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return True

    def getUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select from users where uid=%s"
        cursor.execute(query)
        self.conn.commit()
        return True