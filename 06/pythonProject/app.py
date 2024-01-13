import math
import os
from shared import app, db
from flask import render_template, request, redirect, url_for, abort
from MovieRepository import MovieRepository

db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '5432')
db_user = os.environ.get('DB_USER', 'postgres')
db_password = os.environ.get('DB_PASSWORD', 'secret')
db_name = os.environ.get('DB_NAME', 'postgres')
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db.init_app(app)

movie_repository = MovieRepository()

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)