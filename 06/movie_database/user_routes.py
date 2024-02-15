from flask import render_template, request, redirect, url_for, session
from shared import app
import user_repository

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.values.get('email')
        password = request.values.get('password')
        user = user_repository.by_email_and_password(email, password)
        if user:
            session['user_id'] = user.ID
            return redirect(url_for("movie_list"))
        return render_template("login.html", email=email, error=True)
    return render_template("login.html", error=False)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if session.get("user_id") is not None:
        del session["user_id"]
    return redirect(url_for("login"))
