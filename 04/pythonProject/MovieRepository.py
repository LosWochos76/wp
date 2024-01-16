import pandas as pd

def get_movies(page=0):
    return df.iloc[page*page_size:(page+1)*page_size].to_dict('records')

def get_last_page():
    return len(df) // page_size

def get_movie(movie_id):
    return df.loc[df['ID'] == int(movie_id)].to_dict('records')[0]

def delete(movie_id):
    global df
    df = df[df['ID'] != movie_id]
    return True

def update(values):
    global df
    index = df[df['ID'] == int(values['ID'])].index
    for key, value in values.items():
        df.loc[index, key] = pd.Series(value).astype(df[key].dtype).item()
    return True


page_size = 10
df = pd.read_csv('data/movies.csv')
df = df.sort_values(by=['Film'])
df['ID'] = range(1, len(df)+1)
