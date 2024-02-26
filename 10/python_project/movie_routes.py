from flask import request, render_template, abort, redirect, url_for, Response
from shared import app
import movie_repository

@app.route("/")
def movie_list():
    page = request.args.get('page', 0, type=int)
    movies = movie_repository.get_movies(page)
    last_page = movie_repository.get_last_page()
    return render_template("movie_list.html", movies=movies, page=page, last_page=last_page)

@app.route("/movies/<int:movie_id>")
def single_movie(movie_id):
    movie = movie_repository.get_movie(movie_id)
    if movie:
        return render_template("movie_edit.html", movie=movie)
    return abort(404)

@app.route("/movies/save", methods=["POST"])
def save_movie():
    if movie_repository.update(request.form):
        return redirect(url_for("movie_list"))
    abort(404)

@app.route("/movies/delete/<int:movie_id>")
def delete_movie(movie_id):
    if movie_repository.delete(movie_id):
        return redirect(url_for("movie_list"))
    abort(404)

@app.route('/movies/by-year-chart.png')
def movies_by_year():
    figure_as_bytes = movie_repository.get_movies_by_year_as_png()
    return Response(figure_as_bytes, mimetype='image/png')

@app.route('/movies/analyze-by-year')
def analyze_by_year():
    return render_template("movies_by_year.html")