import hashlib
import os

def generate_salt():
    return os.urandom(16).hex()

def hash_password(password, salt):
    # kombino password + salt
    combined = password + salt
    return hashlib.sha256(combined.encode()).hexdigest()