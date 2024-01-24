import UserRepository
from Shared import app
from flask import render_template, request, redirect, url_for, abort
import MovieRepository

@app.route("/")
@UserRepository.login_required
def movie_list():
    page = request.args.get('page', 0, type=int)
    movies = MovieRepository.get_movies(page)
    last_page = MovieRepository.get_last_page()
    return render_template("movie_list.html", movies=movies, page=page, last_page=last_page)

@app.route("/movies/<int:movie_id>")
@UserRepository.login_required
def single_movie(movie_id):
    if UserRepository.is_logged_out():
        return redirect(url_for("login"))
    movie = MovieRepository.get_movie(movie_id)
    if movie:
        return render_template("movie_edit.html", movie=movie)
    else:
        return abort(404)

@app.route("/movies/save", methods=["POST"])
@UserRepository.login_required
def save_movie():
    if UserRepository.is_logged_out():
        return redirect(url_for("login"))
    if MovieRepository.update(request.form):
        return redirect(url_for("movie_list"))
    else:
        abort(404)

@app.route("/movies/delete/<int:movie_id>")
@UserRepository.login_required
def delete_movie(movie_id):
    if MovieRepository.delete(movie_id):
        return redirect(url_for("movie_list"))
    else:
        abort(404)