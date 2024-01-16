from sqlalchemy import Column, Integer, String, Numeric
from Shared import db

class Movie(db.Model):
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