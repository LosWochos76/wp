import pandas as pd
import math

class MovieRepository:
    def __init__(self):
        self.load_from_csv()
        self.generate_ids()
        self.page_size = 10

    def load_from_csv(self):
        data = pd.read_csv('data/movies.csv')
        self.movies = data.to_dict(orient='records')
        self.movies = sorted(self.movies, key=lambda x: x['Film'])

    def generate_ids(self):
        id = 1
        for film in self.movies:
            film['ID'] = id
            id = id + 1

    def get_movies(self, page=0):
        return self.movies[page*self.page_size:(page+1)*self.page_size]

    def get_last_page(self):
        return int(len(self.movies)/self.page_size)

    def get_pos(self, movie_id):
        for i in range(len(self.movies)):
            if self.movies[i]['ID'] == movie_id:
                return i
        return -1

    def get_movie(self, movie_id):
        pos = self.get_pos(movie_id) # Die Funktion get_pos muss man auch realisieren
        if pos > -1:
            return self.movies[pos]
        else:
            return None

    def delete(self, movie_id):
        pos = self.get_pos(movie_id)
        if pos > -1:
            del self.movies[pos]
            return True
        else:
            return False

    def update(self, values):
        pos = self.get_pos(int(values['ID']))
        if pos == -1:
            return False
        for key, value in values.items():
            self.movies[pos][key] = type(self.movies[pos][key])(value)
        return True

