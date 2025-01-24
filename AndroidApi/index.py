import json
from flask import Flask, jsonify, request
from database import User, Question
app = Flask(__name__)

##TODO: Add password encryption before storing to DB
##TODO: Add PK pair to UserId and Username

##User Enpoints
#get user by username
@app.route('/user/<string:username>')
def get_user(username):
    #initialize User object and pull from DB via username
    user = User.User()
    user.get_user(username)
    #check if user exists
    if user.userId is None:
        return jsonify({'message': 'User not found'}), 404
    #return user object as JSON
    return user.json()

#insert user
@app.route('/user/add', methods=['POST'])
def add_user():
    #push JSON data from response to User object
    user = User.User(**request.get_json())
    #check if user already exists
    checkUser = User.User()
    checkUser.get_user(user.username)
    if checkUser.userId is not None:
        return jsonify({'message': 'User already exists'}), 400
    #add user to database if they do not exist
    user.add_user(user)
    #return the newly stored user
    storedUser = User.User()
    storedUser.get_user(user.username)
    #check if user was stored
    if storedUser.userId is None:
        return jsonify({'message': 'User not stored'}), 404
    #if all is well, return the new userId
    return jsonify({'userId': storedUser.userId}), 201

#update user
@app.route('/user/update/<int:userId>', methods=['PUT'])
def update_user(userId):
    #push JSON data from response to User object
    user = User.User(**request.get_json())
    #check if user exists
    checkUser = User.User()
    checkUser.get_userById(userId)
    if checkUser.userId is None:
        return jsonify({'message': 'User not found'}), 404
    #update user in database based on the provided userId
    user.update_user(user, checkUser.userId)
    #if all is well, return the new userId
    return jsonify({'userId': user.userId}), 201

#delete user
@app.route('/user/delete/<int:userId>', methods=['POST'])
def delete_user(userId):
    #check if user exists
    checkUser = User.User()
    checkUser.get_userById(userId)
    if checkUser.userId is None:
        return jsonify({'message': 'User not found'}), 404
    #Maybe check password here before we delete to prevent spoofing
    #delete user from database based on the provided userId
    checkUser.delete_user(checkUser.userId)
    #if all is well, return the deleted message
    return jsonify({'message': 'User deleted'}), 201

#disable user account
@app.route('/user/disable/<int:userId>', methods=['PUT'])
def disable_user(userId):
    #check if user exists
    checkUser = User.User()
    checkUser.get_userById(userId)
    if checkUser.userId is None:
        return jsonify({'message': 'User not found'}), 404
    #disable user in database based on the provided userId
    checkUser.disable_user(checkUser.userId)
    #if all is well, return the disabled message
    return jsonify({'message': 'User disbaled'}), 201

#enable user account
@app.route('/user/enable/<int:userId>', methods=['PUT'])
def enable_user(userId):
    #check if user exists
    checkUser = User.User()
    checkUser.get_userById(userId)
    if checkUser.userId is None:
        return jsonify({'message': 'User not found'}), 404
    #enable user in database based on the provided userId
    checkUser.enable_user(checkUser.userId)
    #if all is well, return the enabled message
    return jsonify({'message': 'User enabled'}), 201

#update login time
@app.route('/user/login/<int:userId>', methods=['PUT'])
def update_login(userId):
    #check if user exists
    checkUser = User.User()
    checkUser.get_userById(userId)
    if checkUser.userId is None:
        return jsonify({'message': 'User not found'}), 404
    #update login time in database based on the provided userId
    checkUser.update_login(checkUser.userId)
    #if all is well, return the updated message
    return jsonify({'message': 'Login time updated'}), 201



##Question Endpoints

#get question by questionId
@app.route('/question/<int:questionId>')
def get_question(questionId):
    #initialize Question object and pull from DB via questionId
    question = Question.Question()
    question.get_question(questionId)
    #check if question exists
    if question.questionId is None:
        return jsonify({'message': 'Question not found'}), 404
    #return question object as JSON
    return question.json()

#add question
@app.route('/question/add', methods=['POST'])
def add_question():
    #push JSON data from response to Question object
    question = Question.Question(**request.get_json())
    ##See if we have this question already
    checkQuestion = Question.Question()
    checkQuestion.get_question(question.questionId)
    if checkQuestion.questionId is not None:
        return jsonify({'message': 'Question already exists'}), 400
    #add question to database
    question.add_question(question)
    #return the newly stored question
    return jsonify({'message': "question added"}), 201

#update question
@app.route('/question/update/<int:questionId>', methods=['PUT'])
def update_question(questionId):
    #push JSON data from response to Question object
    question = Question.Question(**request.get_json())
    #check if question exists
    checkQuestion = Question.Question()
    checkQuestion.get_question(questionId)
    if checkQuestion.questionId is None:
        return jsonify({'message': 'Question not found'}), 404
    #update question in database based on the provided questionId
    question.update_question(question, checkQuestion.questionId)
    #if all is well, return the updated message
    return jsonify({'message': 'Question updated'}), 201

#delete question
@app.route('/question/delete/<int:questionId>', methods=['POST'])
def delete_question(questionId):
    #check if question exists
    checkQuestion = Question.Question()
    checkQuestion.get_question(questionId)
    if checkQuestion.questionId is None:
        return jsonify({'message': 'Question not found'}), 404
    #delete question from database based on the provided questionId
    checkQuestion.delete_question(checkQuestion.questionId)
    #if all is well, return the deleted message
    return jsonify({'message': 'Question deleted'}), 201