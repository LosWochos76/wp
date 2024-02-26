import pandas as pd
from shared import db, app
from models import Movie

def get_movies(page=0):
    with app.app_context():
        return (Movie.query
                .order_by(Movie.Film)
                .offset(page*PAGE_SIZE)
                .limit(PAGE_SIZE).all())

def get_last_page():
    with app.app_context():
        count = db.session.query(Movie).count()
        return count//PAGE_SIZE

def get_movie(movie_id):
    with app.app_context():
        return Movie.query.filter_by(ID=movie_id).first()

def delete(movie_id):
    with app.app_context():
        movie = Movie.query.filter_by(ID=movie_id).first()
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return True
        return False

def update(values):
    with app.app_context():
        movie = Movie.query.filter_by(ID=int(values['ID'])).first()
        if movie:
            movie.Film = values['Film']
            movie.Genre = values['Genre']
            movie.LeadStudio = values['LeadStudio']
            movie.AudienceScore = float(values['AudienceScore'])
            movie.Profitability = float(values['Profitability'])
            movie.RottenTomatoes = float(values['RottenTomatoes'])
            movie.WorldwideGross = float(values['WorldwideGross'])
            movie.Year = int(values['Year'])
            db.session.commit()
            return True
        return False

def init():
    with app.app_context():
        if Movie.query.count() == 0:
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
                db.session.add(obj)
                db.session.commit()

PAGE_SIZE = 10
