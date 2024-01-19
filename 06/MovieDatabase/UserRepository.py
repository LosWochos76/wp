import os
from Shared import db, app
from User import User
import hashlib

def by_email_and_password(email, password):
    email = email.lower()
    password_hash = hash_password(password)
    with app.app_context():
        return User.query.filter_by(Email=email, PasswordHash=password_hash).first()

def get_user(user_id):
    with app.app_context():
        return User.query.filter_by(ID=user_id).first()

def init():
    with app.app_context():
        if User.query.count() == 0:
            user = User()
            user.Email = "alexander.stuckenholz@hshl.de"
            user.PasswordHash = hash_password("secret")
            db.session.add(user)
            db.session.commit()

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()