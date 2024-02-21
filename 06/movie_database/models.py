from sqlalchemy import MetaData, Integer, String, Numeric, Column
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = 'users'
    ID=Column(Integer, primary_key=True)
    Email=Column('Email', String(100))
    PasswordHash=Column('PasswordHash', String(200))
    Role=Column('Role', Numeric)

class Movie(Base):
    __tablename__ = 'movies'
    ID=Column(Integer, primary_key=True)
    Film=Column('Film', String(100))
    Genre=Column('Genre', String(100))
    LeadStudio = Column('LeadStudio', String(100))
    AudienceScore = Column('AudienceScore', Numeric)
    Profitability = Column('Profitability', Numeric)
    RottenTomatoes = Column('RottenTomatoes', Numeric)
    WorldwideGross = Column('WorldwideGross', Numeric)
    Year = Column('Year', Integer)
