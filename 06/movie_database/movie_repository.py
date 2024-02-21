import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Movie

class MovieRepository:
    def __init__(self, app: Flask, db: SQLAlchemy):
        self.app = app
        self.db = db
        self.PAGE_SIZE = 10
        self.__load_data()

    def __load_data(self):
        with self.app.app_context():
            if self.db.session.query(Movie).count() == 0:
                data = pd.read_csv('data/movies.csv')
                for movie in data.to_dict(orient='records'):
                    obj = Movie(Film=movie['Film'],
                                Genre=movie['Genre'],
                                LeadStudio=movie['LeadStudio'],
                                AudienceScore=float(movie['AudienceScore']),
                                Profitability=float(movie['Profitability']),
                                RottenTomatoes=float(movie['RottenTomatoes']),
                                WorldwideGross=float(movie['WorldwideGross'][1:]),
                                Year=int(movie['Year']))
                    self.db.session.add(obj)
                    self.db.session.commit()

    def get_movies(self, page=0):
        with self.app.app_context():
            return (self.db.session.query(Movie)
                    .order_by(Movie.Film)
                    .offset(page*self.PAGE_SIZE)
                    .limit(self.PAGE_SIZE).all())

    def get_last_page(self):
        with self.app.app_context():
            count = self.db.session.query(Movie).count()
            return count//self.PAGE_SIZE

    def get_movie(self, movie_id):
        with self.app.app_context():
            return self.db.session.query(Movie).filter(Movie.ID==movie_id).first()

    def delete(self, movie_id):
        with self.app.app_context():
            movie = self.db.session.query(Movie).filter(Movie.ID==movie_id).first()
            if movie:
                self.db.session.delete(movie)
                self.db.session.commit()
                return True
            return False

    def update(self, values):
        with self.app.app_context():
            movie = self.db.session.query(Movie).filter(Movie.ID==int(values['ID'])).first()
            if movie:
                movie.Film = values['Film']
                movie.Genre = values['Genre']
                movie.LeadStudio = values['LeadStudio']
                movie.AudienceScore = float(values['AudienceScore'])
                movie.Profitability = float(values['Profitability'])
                movie.RottenTomatoes = float(values['RottenTomatoes'])
                movie.WorldwideGross = float(values['WorldwideGross'])
                movie.Year = int(values['Year'])
                self.db.session.commit()
                return True
            return False