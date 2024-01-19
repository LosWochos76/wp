import os
from Shared import app, db
from flask import request, session, g
import MovieRepository
import MovieRoutes
import UserRepository
import UserRoutes

db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '5432')
db_user = os.environ.get('DB_USER', 'postgres')
db_password = os.environ.get('DB_PASSWORD', 'secret')
db_name = os.environ.get('DB_NAME', 'postgres')
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.secret_key = 'secret_key'
db.init_app(app)

with app.app_context():
    db.create_all()

MovieRepository.init()
UserRepository.init()

@app.before_request
def load_user():
    if session.get("user_id") is not None:
        g.user = UserRepository.get_user(session.get("user_id"))
    else:
        g.user = None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)