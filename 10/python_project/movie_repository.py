import io
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def get_movies(page=0):
    return df.iloc[page * PAGE_SIZE:(page + 1) * PAGE_SIZE].to_dict('records')

def get_last_page():
    return len(df) // PAGE_SIZE

def get_movie(movie_id):
    index = df[df['ID'] == int(movie_id)].index
    if index.any():
        return df.loc[index].to_dict('records')[0]
    return None

def delete(movie_id):
    global df
    index = df[df['ID'] == int(movie_id)].index
    if index.any():
        df = df[index]
        return True
    return False

def update(values):
    global df
    index = df[df['ID'] == int(values['ID'])].index
    if index.any():
        for key, value in values.items():
            df.loc[index, key] = pd.Series(value).astype(df[key].dtype).item()
        return True
    return False

def get_movies_by_year_as_png():
    by_years = df.groupby('Year')['Film'].count()
    ax = by_years.plot(kind='bar', stacked=True)
    output = io.BytesIO()
    FigureCanvas(ax.get_figure()).print_png(output)
    return output.getvalue()

PAGE_SIZE = 10
df = pd.read_csv('data/movies.csv')
df = df.sort_values(by=['Film'])
df['ID'] = range(1, len(df) + 1)
