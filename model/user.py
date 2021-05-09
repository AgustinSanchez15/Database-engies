from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='ec2-54-224-120-186.compute-1.amazonaws.com'" % (
            pg_config['dbname'], pg_config['user'],
            pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def addUser(self, uname, upassword, fname, lname):
        cursor = self.conn.cursor()
        query = "insert into users (uname, upassword, fname, lname, followers, visible) values (%s, %s, %s, %s, 0, 1) returning uid;"
        cursor.execute(query, (uname, upassword, fname, lname))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users where visible = 1;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def updateUser(self, uid, uname, upassword, fname, lname, followers):
        cursor = self.conn.cursor()
        query = "update users set uname = %s, upassword=%s, fname=%s, lname=%s, followers=%s where uid=%s;"
        cursor.execute(query, (uname, upassword, fname, lname, followers, uid))
        self.conn.commit()
        return True

    def deleteUser(self, uid):
        cursor = self.conn.cursor()
        query = "update users set visible = 0 where uid=%s"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return True

    def getUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid=%s and visible=1"
        cursor.execute(query, (uid,))
        uid = cursor.fetchone()
        #self.conn.commit()
        return uid