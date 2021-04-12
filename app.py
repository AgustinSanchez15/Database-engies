from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.message import BaseMessage, BaseFollowers

app = Flask(__name__)
# apply CORS
CORS(app)

@app.route('/engies/like/<int:pid>', methods=['POST'])
def handleAddLike(pid):
    if request.method == 'POST':
        return BaseMessage().insertLike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/like/remove/<int:pid>', methods=['DELETE'])
def handleRemoveLike(pid):
    if request.method == 'DELETE':
        return BaseMessage().removeLike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/liked/<int:pid>', methods=['GET'])
def handleLiked(pid):
    if request.method == 'GET':
        return BaseMessage().getLiked(pid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unlike/<int:pid>', methods=['POST'])
def handleAddUnlike(pid):
    if request.method == 'POST':
        return BaseMessage().insertUnlike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unlike/remove/<int:pid>', methods=['DELETE'])
def handleRemoveUnlike(pid):
    if request.method == 'DELETE':
        return BaseMessage().removeUnlike(pid, request.json)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/unliked/<int:pid>', methods=['GET'])
def handleUnliked(pid):
    if request.method == 'GET':
        return BaseMessage().getUnliked(pid)
    else:
        return jsonify("Method Not Allowed"), 405

@app.route('/engies/follow/<int:uid>', methods=['POST'])
def handleAddFollower(uid):
    if request.method == 'POST':
        return BaseFollowers().insertFollowers(uid)
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
def handleAddUnfollow(uid, fuid):
    if request.method == 'POST':
        return BaseFollowers().insertUnfollowing(uid, fuid)
    else:
        return jsonify("Method Not Allowed"), 405

if __name__ == '__main__':
    app.run()
