from flask import jsonify
from model.followers import FollowersDAO

class BaseFollowers:

    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        return result

    def build_attr_dict(self, uid, fuid):
        result = {}
        result['uid'] = uid
        result['uname'] = fuid
        return result

    def insertFollowers(self, uid, json):
        RegisteredUser = json['RegisteredUser']
        dao = FollowersDAO()
        uid = dao.insertFollowers(RegisteredUser, uid)
        result = self.build_attr_dict(uid, RegisteredUser)
        return jsonify(result), 201


    def getFollowing(self, uid):
        dao = FollowersDAO()
        following_tuple = dao.getFollowing(uid)
        result_list = []
        for row in following_tuple:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("Not Found"), 404


    def getFollowers(self, uid):
        dao = FollowersDAO()
        follower_tuple = dao.getFollowers(uid)
        result_list = []
        for row in follower_tuple:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        if result_list:
            return jsonify(result_list), 200
        else:
            return jsonify("Not Found"), 404


    def insertUnfollowing(self, uid, json):
        RegisteredUser = json['RegisteredUser']
        dao = FollowersDAO()
        dao.insertUnfollowing(uid, RegisteredUser)
        result = self.build_attr_dict(uid, RegisteredUser)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

