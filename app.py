from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.message import BaseMessage

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

if __name__ == '__main__':
    app.run()
