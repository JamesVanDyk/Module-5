"""
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
"""

#the user id is in the url so the user can just change the id an send another accounts data in json

"""
@app.route('/account')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
"""

#this doesn't allow the user to just change the user id in the url and now the id can be gained elsewhere like the user associated
#with the current session id