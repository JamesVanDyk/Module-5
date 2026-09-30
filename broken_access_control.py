"""
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
"""
#The first line goes through a directory that has all the user accounts in it. this can likely lead to a horizontal privilage
#escalation