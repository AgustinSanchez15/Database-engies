from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.like import BaseLike
from controller.followers import BaseFollowers
from controller.message import BaseMessage
from controller.block import BaseBlock
from controller.user import BaseUser

app = Flask(__name__)
# apply CORS
CORS(app)

@app.route('/engies/like/<int:pid>', methods=['POST'])
def handleAddLike(pid):
    if request.method == 'POST':
        return BaseLike().insertLike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/like/remove/<int:pid>', methods=['DELETE'])
def handleRemoveLike(pid):
    if request.method == 'DELETE':
        return BaseLike().removeLike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/liked/<int:pid>', methods=['GET'])
def handleLiked(pid):
    if request.method == 'GET':
        return BaseLike().getLiked(pid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unlike/<int:pid>', methods=['POST'])
def handleAddUnlike(pid):
    if request.method == 'POST':
        return BaseLike().insertUnlike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unlike/remove/<int:pid>', methods=['DELETE'])
def handleRemoveUnlike(pid):
    if request.method == 'DELETE':
        return BaseLike().removeUnlike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unliked/<int:pid>', methods=['GET'])
def handleUnliked(pid):
    if request.method == 'GET':
        return BaseLike().getUnliked(pid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/block/<int:uid>', methods=['POST'])
def handleBlockUser(uid):
    if request.method == 'POST':
        return BaseBlock().blockUser(uid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/blocking/<int:uid>', methods=['GET'])
def handleBlocking(uid):
    if request.method == 'GET':
        return BaseBlock().getBlocking(uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/blockedby/<int:uid>', methods=['GET'])
def handleBlocked(uid):
    if request.method == 'GET':
        return BaseBlock().getBlocked(uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unblock/<int:uid>', methods=['POST'])
def handleUnblock(uid):
    if request.method == 'POST':
        return BaseBlock().unblock(uid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/follow/<int:uid>', methods=['POST'])
def handleAddFollower(uid):
    if request.method == 'POST':
        return BaseFollowers().insertFollowers(uid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/followedby/<int:uid>', methods=['GET'])
def handleGetFollowing(uid):
    if request.method == 'GET':
        return BaseFollowers().getFollowing(uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/follows/<int:uid>', methods=['GET'])
def handleGetFollower(uid):
    if request.method == 'GET':
        return BaseFollowers().getFollowers(uid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unfollow/<int:uid>', methods=['POST'])
def handleAddUnfollow(uid):
    if request.method == 'POST':
        return BaseFollowers().insertUnfollowing(uid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/posts', methods=['POST'])
def handlePostMessage():
    if request.method == 'POST':
        return BaseMessage().addMessage(request.json)
    else:
        return jsonify("Method Not Allowed"), 405


@app.route('/engies/reply', methods=['POST'])
def handleReplyMessage():
    if request.method == 'POST':
        return BaseMessage().replyMessage(request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/share', methods=['POST'])
def handleShareMessage():
    if request.method == 'POST':
        return BaseMessage().shareMessage(request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/msg/<int:pid>', methods=['GET'])
def handleGetMessageID(pid):
    if request.method == 'GET':
        return BaseMessage().getMessage(pid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/msg', methods=['GET'])
def handleGetAllMessages():
    if request.method == 'GET':
        return BaseMessage().getMessages()
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/users', methods=['GET', 'POST'])
def handleAddUser():
    if request.method == 'GET':
        return BaseUser().retrieveUsers()
    if request.method == 'POST':
        return BaseUser().addUser(request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/users/<int:uid>', methods=['PUT', 'GET', 'DELETE'])
def handlePUTSpecificUser(uid):
    if request.method == 'PUT':
        return BaseUser().updateUser(uid, request.json)
    elif request.method == 'DELETE':
        return BaseUser().deleteUser(uid)
    elif request.method == 'GET':
        return BaseUser().getUserId(uid)
    else:
        return jsonify("Method Not Allowed"), 405

if __name__ == '__main__':
    app.run()
