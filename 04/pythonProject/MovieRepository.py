import pandas as pd

def get_movies(page=0):
    return df.iloc[page*page_size:(page+1)*page_size].to_dict('records')

def get_last_page():
    return len(df) // page_size

def get_movie(movie_id):
    return df.loc[df['ID']==movie_id].to_dict('records')[0]

def delete(movie_id):
    global df
    df = df[df['ID'] != movie_id]

def update(values):
    #pos = get_pos(int(values['ID']))
    #for key, value in values.items():
    #    movies[pos][key] = type(movies[pos][key])(value)
    return True


page_size = 10
df = pd.read_csv('data/movies.csv')
df = df.sort_values(by=['Film'])
df['ID'] = range(1, len(df)+1)

movies = df.to_dict(orient='records')
movies = sorted(movies, key=lambda x: x['Film'])
