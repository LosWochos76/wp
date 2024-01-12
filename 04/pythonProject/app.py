import math
from flask import Flask, render_template, request, redirect, url_for, abort
from MovieRepository import MovieRepository

app = Flask(__name__)

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
    else:
        return abort(404)

@app.route("/movies/save", methods=["POST"])
def save_movie():
    if movie_repository.update(request.form):
        return redirect(url_for("movie_list"))
    else:
        abort(404)

@app.route("/movies/delete/<int:movie_id>")
def delete_movie(movie_id):
    if movie_repository.delete(movie_id):
        return redirect(url_for("movie_list"))
    else:
        abort(404)

movie_repository = MovieRepository()

if __name__ == "__main__":
    app.run(port=8000, debug=True)