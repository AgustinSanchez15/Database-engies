from flask import jsonify
from model.followers import FollowersDAO

class BaseFollowers:

    def build_map_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['fuid'] = row[1]
        return result

    def build_attr_dict(self, uid, fuid):
        result = {}
        result['uid'] = uid
        result['fuid'] = fuid
        return result

    def insertFollowers(self, json):
        fuid = json['fuid']
        dao = FollowersDAO()
        uid = dao.insertFollowers(fuid)
        result = self.build_attr_dict(uid, fuid)
        return jsonify(result), 201


    def getFollowing(self, uid):
        dao = FollowersDAO()
        following_tuple = dao.getFollowing(uid)
        if not following_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(following_tuple)
            return jsonify(result), 200


    def getFollowers(self, uid):
        dao = FollowersDAO()
        follower_tuple = dao.getFollower(uid)
        if not follower_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(follower_tuple)
            return jsonify(result), 200


    def insertUnfollowing(self, uid, fuid):
        dao = FollowersDAO()
        result = dao.insertUnfollowing(uid, fuid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404

