from flask import jsonify
from model.user import UserDAO

class BaseUser:

    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['upassword'] = row[2]
        result['fname'] = row[3]
        result['lname'] = row[4]
        result['followers'] = row[5]
        result['visible'] = row[6]
        return result

    def build_attr_dict(self, uid, uname, upassword, fname, lname, followers, visible):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['upassword'] = upassword
        result['fname'] = fname
        result['lname'] = lname
        result['followers'] = followers
        result['visible'] = visible
        return result

    def addUser(self):
        uname = "test"
        upassword = "test"
        fname = "test"
        lname = "test"
        dao = UserDAO()
        uid = dao.addUser(uname, upassword, fname, lname)
        result = self.build_attr_dict(uid, uname, upassword, fname, lname, 0, 1)
        return jsonify(result), 201

    def retrieveUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("NOT FOUND"), 404

    def updateUser(self, uid, json):
        uname = json['uname']
        upassword = json['upassword']
        fname = json['fname']
        lname = json['lname']
        followers = json['followers']
        dao = UserDAO()
        dao.updateUser(uid, uname, upassword, fname, lname, followers)
        result = self.build_attr_dict(uid, uname, upassword, fname, lname, followers)
        return jsonify(result), 201

    def deleteUser(self, uid):
        dao = UserDAO()
        result = dao.deleteUser(uid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def getUserId(self, uid):
        dao = UserDAO()
        tuple = dao.getUserId(uid)
        if not tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(tuple)
            return jsonify(result), 200
