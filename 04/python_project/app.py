from shared import app
import movie_repository
import movie_routes

if __name__ == "__main__":
    app.run(port=8000, debug=True)
