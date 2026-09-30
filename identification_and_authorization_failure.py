"""
if (inputPassword.equals(user.getPassword())):
    // Login success
"""

#Multi-factor authentication should be used to ensure a user's identification. if MFA isn't used then another method such as
#checking if the device is a familiar device.


"""
if (inputPassword == user.getPassword()):
    code = sendAuthCode(user.getKnownEmail())
    if (code = inputCode):
        // Login success
    else:
        // Login fail
"""

#This uses a fuction to generate a verification code to the known user email and when the user inputs a code it will compare what
#was generated to what they input to authenticate them