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
        return result

    def build_attr_dict(self, uid, uname, upassword, fname, lname, followers):
        result = {}
        result['uid'] = uid
        result['uname'] = uname
        result['upassword'] = upassword
        result['fname'] = fname
        result['lname'] = lname
        result['followers'] = followers
        return result

    def addUser(self, uid, json):
        uname = json['uname']
        upassword = json['upassword']
        fname = json['fname']
        lname = json['lname']
        followers = json['followers']
        dao = UserDAO()
        dao.addUser(uid, uname, upassword, fname, lname, followers)
        result = self.build_attr_dict(uid, uname, upassword, fname, lname, followers)
        return jsonify(result), 201

    def retrieveUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            obj = self.build_attr_dict(row)
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
        result = dao.getUserId(uid)
        return jsonify(result)
