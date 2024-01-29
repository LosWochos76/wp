import os
from Shared import db, app
from User import User
import hashlib
from flask import session, g, redirect, url_for
from functools import wraps

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

@app.before_request
def load_user():
    if session.get("user_id") is not None:
        g.user = get_user(session.get("user_id"))
    else:
        g.user = None

def current_user():
    return g.user

def is_logged_in():
    return current_user() is not None

def is_logged_out():
    return current_user() is None

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()

def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login"))
        else:
            return function(*args, **kwargs)

    return wrapper
