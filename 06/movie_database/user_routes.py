from flask import render_template, request, redirect, url_for, session, g, Flask
from user_repository import UserRepository

class UserRoutes:
    def __init__(self, app:Flask, user_repository:UserRepository):
        self.user_repository = user_repository
        app.add_url_rule("/login", "login", self.login, methods=["GET", "POST"])
        app.add_url_rule("/logout", "logout", self.logout)
        app.before_request(self.load_user)

    def login(self):
        if request.method == 'POST':
            email = request.values.get('email')
            password = request.values.get('password')
            user = self.user_repository.by_email_and_password(email, password)
            if user:
                session['user_id'] = user.ID
                return redirect(url_for("movie_list"))
            return render_template("login.html", email=email, error=True)
        return render_template("login.html", error=False)

    def logout(self):
        if session.get("user_id") is not None:
            del session["user_id"]
        return redirect(url_for("login"))

    def load_user(self):
        global g
        if session.get("user_id") is not None:
            g.user = self.user_repository.get_user(session.get("user_id"))
        else:
            g.user = None