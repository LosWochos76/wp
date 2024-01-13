import pandas as pd
from shared import db, app
from Movie import Movie

class MovieRepository:
    def __init__(self):
        with app.app_context():
            db.create_all()

        self.load_from_csv()
        self.page_size = 10

    def load_from_csv(self):
        with app.app_context():
            if Movie.query.count() > 0:
                return
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

    def get_movies(self, page=0):
        with app.app_context():
            return Movie.query.order_by(Movie.Film).offset(page*self.page_size).limit(self.page_size).all()

    def get_last_page(self):
        with app.app_context():
            count = db.session.query(Movie).count()
            return int(count/self.page_size)

    def get_movie(self, movie_id):
        with app.app_context():
            return Movie.query.filter_by(ID=movie_id).first()

    def delete(self, movie_id):
        with app.app_context():
            movie = Movie.query.filter_by(ID=movie_id).first()
            if movie:
                db.session.delete(movie)
                db.session.commit()
                return True
            else:
                return False

    def update(self, values):
        with app.app_context():
            movie = Movie.query.filter_by(ID=int(values['ID'])).first()
            if movie:
                movie.Film = values['Film']
                movie.Genre = values['Genre']
                movie.LeadStudio = values['LeadStudio']
                movie.AudienceScore = float(values['AudienceScore']),
                movie.Profitability = float(values['Profitability']),
                movie.RottenTomatoes = float(values['RottenTomatoes']),
                movie.WorldwideGross = float(values['WorldwideGross'])
                movie.Year = int(values['Year'])
                db.session.commit()
                return True
            else:
                return False

