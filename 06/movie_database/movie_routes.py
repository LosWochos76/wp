from flask import render_template, request, redirect, url_for, abort, g, Flask
from user_repository import login_required
from movie_repository import MovieRepository

class MovieRoutes:
    def __init__(self, app:Flask, movie_repository:MovieRepository):
        self.app = app
        self.movie_repository = movie_repository
        app.add_url_rule("/", "movie_list", self.movie_list)
        app.add_url_rule("/movies/<int:movie_id>", "movie_details", self.single_movie)
        app.add_url_rule("/movies/save", "movie_save", self.save_movie, methods=["POST"])
        app.add_url_rule("/movies/delete/<int:movie_id>", "movie_delete", self.delete_movie)

    @login_required
    def movie_list(self):
        page = request.args.get('page', 0, type=int)
        movies = self.movie_repository.get_movies(page)
        last_page = self.movie_repository.get_last_page()
        return render_template("movie_list.html", movies=movies, page=page, last_page=last_page)

    @login_required
    def single_movie(self, movie_id):
        movie = self.movie_repository.get_movie(movie_id)
        if movie:
            return render_template("movie_edit.html", movie=movie)
        return abort(404)

    @login_required
    def save_movie(self):
        if self.movie_repository.update(request.form):
            return redirect(url_for("movie_list"))
        abort(404)

    @login_required
    def delete_movie(self, movie_id):
        if self.movie_repository.delete(movie_id):
            return redirect(url_for("movie_list"))
        abort(404)
