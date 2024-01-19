from sqlalchemy import Column, Integer, String, Numeric
from Shared import db

class User(db.Model):
    __tablename__ = 'users'
    ID=Column(Integer, primary_key=True)
    Email=Column('Email', String(100))
    PasswordHash=Column('PasswordHash', String(200))
    Role=Column('Role', Numeric)