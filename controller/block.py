from flask import jsonify
from model.block import BlockDAO

class BaseBlock:

    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        return result

    def build_attr_dict(self, uid, RegisteredUser):
        result = {}
        result['uid'] = uid
        result['RegisteredUser'] = RegisteredUser
        return result

    def blockUser(self, uid, json):
        RegisteredUser = json['RegisteredUser']
        dao = BlockDAO()
        dao.blockUser(uid, RegisteredUser)
        result = self.build_attr_dict(uid, RegisteredUser)
        return jsonify(result), 201

    def getBlocked(self, uid):
        dao = BlockDAO()
        users_list = dao.getBlocked(uid)
        result_list = []
        for row in users_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("NOT FOUND"), 404

    def getBlocking(self, uid):
        dao = BlockDAO()
        users_list = dao.getBlocking(uid)
        result_list = []
        for row in users_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("NOT FOUND"), 404

    def unblock(self, uid, json):
        RegisteredUser = json['RegisteredUser']
        dao = BlockDAO()
        dao.unblock(uid, RegisteredUser)
        result = self.build_attr_dict(uid, RegisteredUser)
        if result:
            return jsonify("UNBLOCKED"), 200
        else:
            return jsonify("NOT FOUND"), 404

