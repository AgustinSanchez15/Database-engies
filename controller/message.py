from flask import jsonify
from model.message import MessageDAO

class BaseMessage:

    def build_map_dict(self, row):
        result = {}
        result['ID'] = row[0]
        result['Text'] = row[1]
        result['RegisteredUser'] = row[2]
        result['Date'] = row[3]
        return result

    def build_attr_dict(self, RegisteredUser, Text):
        result = {}
        result['RegisteredUser'] = RegisteredUser
        result['Text'] = Text
        return result

    def build_attr_dictrep(self, RegisteredUser, Text, replyingto):
        result = {}
        result['RegisteredUser'] = RegisteredUser
        result['Text'] = Text
        result['replyingto'] = replyingto
        return result

    def build_attr_dictshare(self, RegisteredUser, sharing):
        result = {}
        result['RegisteredUser'] = RegisteredUser
        result['sharing'] = sharing
        return result

    def addMessage(self, json):
        RegisteredUser = json['RegisteredUser']
        Text = json['Text']
        dao = MessageDAO()
        dao.addMessage(RegisteredUser, Text)
        result = self.build_attr_dict(RegisteredUser, Text)
        return jsonify(result), 201

    def replyMessage(self, json):
        RegisteredUser = json['RegisteredUser']
        Text = json['Text']
        replyingto = json['replyingto']
        dao = MessageDAO()
        dao.replyMessage(RegisteredUser, Text, replyingto)
        result = self.build_attr_dictrep(RegisteredUser, Text, replyingto)
        return jsonify(result), 201

    def shareMessage(self, json):
        RegisteredUser = json['RegisteredUser']
        sharing = json['sharing']
        dao = MessageDAO()
        dao.shareMessage(RegisteredUser, sharing)
        result = self.build_attr_dictshare(RegisteredUser, sharing)
        return jsonify(result), 201

    def getMessage(self, pid):
        dao = MessageDAO()
        message = dao.getSpecMessage(pid)
        result = []
        for row in message:
            obj = self.build_map_dict(row)
            result.append(obj)
        if result:
            return jsonify(result), 200
        else:
            return jsonify("NOT FOUND"), 404

    def getMessages(self):
        dao = MessageDAO()
        message = dao.getMessages()
        result = []
        for row in message:
            obj = self.build_map_dict(row)
            result.append(obj)
        if result:
            return jsonify(result), 200
        else:
            return jsonify("NOT FOUND"), 404