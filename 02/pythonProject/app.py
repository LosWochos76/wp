from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello World!</h1>"
@app.route('/username/<username>')
def username(username):
    return f"Your username is {username}"
@app.route("/json")
def json():
    data = {'name': 'alex', 'age': 48}
    return make_response(data, 200, {'Content-Type': 'application/json'})
@app.route("/umleitung")
def umleitung():
    return redirect(url_for("root"))

@app.route("/template")
def tempate():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()