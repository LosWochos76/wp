import os
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from movie_repository import MovieRepository
from user_repository import UserRepository
from movie_routes import MovieRoutes
from user_routes import UserRoutes

class WebApp:
    def __init__(self, database_uri = None):
        if database_uri is None:
            db_host = os.environ.get('DB_HOST', 'localhost')
            db_port = os.environ.get('DB_PORT', '5432')
            db_user = os.environ.get('DB_USER', 'postgres')
            db_password = os.environ.get('DB_PASSWORD', 'secret')
            db_name = os.environ.get('DB_NAME', 'postgres')
            self.database_uri = (f"postgresql://{db_user}:"
                                    f"{db_password}@{db_host}:"
                                    f"{db_port}/{db_name}")
        else:
            self.database_uri = database_uri

    def create_app(self):
        self.init_flask()
        self.connect_to_db()
        self.register_routes()
        return self.app

    def init_flask(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self.database_uri
        self.app.secret_key = os.environ.get('SECRET_KEY', 'nFt9lwYwzU')
        self.db = SQLAlchemy(self.app)

    def connect_to_db(self):
        while True:
            try:
                with self.app.app_context():
                    self.db.create_all()
                    break
            except Exception:
                self.app.logger.error("Could not connect to DB!")
                time.sleep(0.5)

    def register_routes(self):
        self.user_repository = UserRepository(self.app, self.db)
        self.movie_repository = MovieRepository(self.app, self.db)
        self.movie_routes = MovieRoutes(self.app, self.movie_repository)
        self.user_routes = UserRoutes(self.app, self.user_repository)

def create_app():
    wa = WebApp()
    return wa.create_app()

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)
