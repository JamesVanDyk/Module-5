"""
import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
"""

#This uses sha1 which is no longer the standard. sha256 should be used instead

"""
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
"""

#This uses SHA256 which is the standard for encryption. With sha1, the encryption could have been reversed and the password exposed.