from functools import wraps
import hashlib
from flask import session, g, redirect, url_for, Flask
from flask_sqlalchemy import SQLAlchemy
from models import User

class UserRepository:
    def __init__(self, app:Flask, db: SQLAlchemy):
        self.app = app
        self.db = db
        self.__load_data()

    def __load_data(self):
        with self.app.app_context():
            if self.db.session.query(User).count() == 0:
                user = User()
                user.Email = "alexander.stuckenholz@hshl.de"
                user.PasswordHash = self.hash_password("secret")
                self.db.session.add(user)
                self.db.session.commit()

    def by_email_and_password(self, email, password):
        email = email.lower()
        password_hash = self.hash_password(password)
        with self.app.app_context():
            return self.db.session.query(User).filter(User.Email==email, User.PasswordHash==password_hash).first()

    def get_user(self, user_id):
        with self.app.app_context():
            return self.db.session.query(User).filter(User.ID==user_id).first()

    def current_user(self):
        return g.user

    def is_logged_in(self):
        return self.current_user() is not None

    def is_logged_out(self):
        return self.current_user() is None

    def hash_password(self, password):
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        return hash_object.hexdigest()

def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login"))
        return function(*args, **kwargs)

    return wrapper
