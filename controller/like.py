from flask import jsonify
from model.like import LikeDAO

class BaseLike:

    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        return result

    def build_attr_dict(self, uid, RegisteredUser):
        result = {}
        result['pid'] = uid
        result['RegisteredUser'] = RegisteredUser
        return result

    def insertLike(self, pid, json):
        RegisteredUser = json['RegisteredUser']
        dao = LikeDAO()
        dao.insertLike(pid, RegisteredUser)
        result = self.build_attr_dict(pid, RegisteredUser)
        return jsonify(result), 201

    def removeLike(self, pid, json):
        RegisteredUser = json['RegisteredUser']
        dao = LikeDAO()
        dao.removeLike(pid, RegisteredUser)
        result = self.build_attr_dict(pid, RegisteredUser)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def getLiked(self, pid):
        dao = LikeDAO()
        users_list = dao.getLiked(pid)
        result_list = []
        for row in users_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("NOT FOUND"), 404

    def insertUnlike(self, pid, json):
        RegisteredUser = json['RegisteredUser']
        dao = LikeDAO()
        dao.insertUnlike(pid, RegisteredUser)
        result = self.build_attr_dict(pid, RegisteredUser)
        return jsonify(result), 201

    def removeUnlike(self, pid, json):
        RegisteredUser = json['RegisteredUser']
        dao = LikeDAO()
        dao.removeUnlike(pid, RegisteredUser)
        result = self.build_attr_dict(pid, RegisteredUser)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

    def getUnliked(self, pid):
        dao = LikeDAO()
        users_list = dao.getUnliked(pid)
        result_list = []
        for row in users_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("NOT FOUND"), 404