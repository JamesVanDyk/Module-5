"""
@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return 'Password reset'
"""

#This allows an attacker to enter any email that is associated with an account in the database and just allows them to reset the
#password without authorizing first. 

"""
@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    emailMessage = (f'here is a link to reset your password: examplelink.com/reset-password?=user' + <User.query.filter_by(userID = user)>)
    sendEmailLink(user, from = 'This company', subject = 'password reset', message = emailMessage)

    @app.route(f'/reset-password?=user' + <User.query.filter_by(userID = user)>, methods=['POST'])
    def reset_page():
        new_password = request.form['new_password']  
        user.password = new_password
        db.session.commit()
        return 'Password reset'
    return reset_page()
"""

#This sends an reset link to the email the person puts in that way they have to actually get into the email account associated with
#the account. This verifies the user because they would have to also have access to the email account to reset the password.