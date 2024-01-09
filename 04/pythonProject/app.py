from flask import Flask, render_template, request, make_response, redirect, url_for, abort
from MovieRepository import MovieRepository

app = Flask(__name__)

@app.route("/")
def movie_list():
    return render_template("movies_list.html", movies=movies.get_movies())

@app.route("/movies/<int:movie_id>", methods=["GET", "POST"])
def single_movie(movie_id):
    if request.method == "GET":
        movie = movies.get_movie(movie_id)
        if movie:
            return render_template("single_movie.html", movie=movie)
        else:
            return abort(404)
    elif request.method == "POST":
        if movies.update(request.form):
            return redirect(url_for("movie_list"))
        else:
            abort(404)

@app.route("/movies/delete/<int:movie_id>")
def delete_movie(movie_id):
    if movies.delete(movie_id):
        return redirect(url_for("movie_list"))
    else:
        abort(404)

movies = MovieRepository()

if __name__ == "__main__":
    app.run(port=8000, debug=True)