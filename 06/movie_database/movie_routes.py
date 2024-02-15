from flask import render_template, request, redirect, url_for, abort
from shared import app
import user_repository
import movie_repository

@app.route("/")
@user_repository.login_required
def movie_list():
    page = request.args.get('page', 0, type=int)
    movies = movie_repository.get_movies(page)
    last_page = movie_repository.get_last_page()
    return render_template("movie_list.html", movies=movies, page=page, last_page=last_page)

@app.route("/movies/<int:movie_id>")
@user_repository.login_required
def single_movie(movie_id):
    movie = movie_repository.get_movie(movie_id)
    if movie:
        return render_template("movie_edit.html", movie=movie)
    return abort(404)

@app.route("/movies/save", methods=["POST"])
@user_repository.login_required
def save_movie():
    if movie_repository.update(request.form):
        return redirect(url_for("movie_list"))
    abort(404)

@app.route("/movies/delete/<int:movie_id>")
@user_repository.login_required
def delete_movie(movie_id):
    if movie_repository.delete(movie_id):
        return redirect(url_for("movie_list"))
    abort(404)
