import os
import time

from Shared import app, db
import MovieRepository
import MovieRoutes
import UserRepository
import UserRoutes

def create_app():
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', '5432')
    db_user = os.environ.get('DB_USER', 'postgres')
    db_password = os.environ.get('DB_PASSWORD', 'secret')
    db_name = os.environ.get('DB_NAME', 'postgres')
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.secret_key = os.environ.get('SECRET_KEY', 'nFt9lwYwzU')
    db.init_app(app)

    while True:
        try:
            with app.app_context():
                db.create_all()

            MovieRepository.init()
            UserRepository.init()
            return app
        except Exception as e:
            app.logger.error("Could not connect to DB!")
            time.sleep(0.5)

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)