from functools import wraps
import jwt
from flask import Flask, make_response, abort, request, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 's9d78f6s9d8fhksahdfkj'

db = [
    {
        'id': 1,
        'firstname': 'Alexander',
        'lastname': 'Stuckenholz',
        'email': 'alexander.stuckenholz@hshl.de',
        'isAdmin': True,
        'passwordHash': 'password'
    },
    {
        'id': 2,
        'firstname': 'Elvira',
        'lastname': 'Spiess',
        'email': 'elvira.spiess@gmail.com',
        'isAdmin': False,
        'passwordHash': 'password'
    }
]


def pos_by_id(id):
    for pos, obj in enumerate(db):
        if obj['id'] == id:
            return pos
    return -1


def pos_by_email(email):
    email = email.lower()
    for pos, obj in enumerate(db):
        if obj['email'].lower() == email:
            return pos
    return -1

def decode_token(request):
    if "Authorization" not in request.headers:
        abort(401, "Authorization Token is missing!")
    token = request.headers["Authorization"]
    try:
        data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        pos = pos_by_id(data['user_id'])
        if pos == -1:
            abort(401, "User not found!")
        current_user = db[pos]
    except Exception as e:
        abort(500, "Semething went wrong!")
    return current_user

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_user = decode_token(request)
        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/users/login', methods=["POST"])
def login():
    data = request.json
    if "email" not in data.keys() or "passwordHash" not in data.keys():
        abort(500, message="Required data missing!")
    pos = pos_by_email(data['email'])
    if pos == -1:
        abort(400, "User not found!")
    user = db[pos]
    if user['passwordHash'] != data['passwordHash']:
        abort(401, "Password incorrect!")
    token = jwt.encode({"user_id": user["id"]}, app.config["SECRET_KEY"], algorithm="HS256")
    return make_response(token, 200, {'Content-Type': 'application/json'})


@app.route('/users/', methods=["GET"])
def get_all():
    current_user = decode_token(request)
    if current_user['isAdmin'] == False:
        abort(401, "User not allowed!")
    return make_response(db, 200,
        {'Content-Type': 'application/json'})


@app.route('/users/', methods=["POST"])
@token_required
def add(current_user):
    if current_user['isAdmin'] == False:
        abort(401, "User not allowed!")
    data = request.get_json()
    if "name" not in data.keys():
        abort(500, message="name property missing!")
    obj = { "name": data["name"], "id": len(db)+1 }
    db.append(obj)
    return make_response(obj, 200, {'Content-Type': 'application/json'})


@app.route('/users/<int:id>', methods=["GET"])
@token_required
def get_single(current_user, id):
    if current_user['isAdmin'] == False:
        abort(401, "User not allowed!")
    pos = pos_by_id(id)
    if pos == -1:
        abort(404)
    return make_response(db[pos], 200, {'Content-Type': 'application/json'})


@app.route('/users/<int:id>', methods=["DELETE"])
@token_required
def delete(current_user, id):
    if current_user['isAdmin'] == False:
        abort(401, "User not allowed!")
    pos = pos_by_id(id)
    if pos == -1:
        abort(404)
    del db[pos]
    return make_response("", 200, {'Content-Type': 'application/json'})


@app.route('/users/<int:id>', methods=["PUT"])
@token_required
def update(current_user, id):
    if current_user['isAdmin'] == False:
        abort(401, "User not allowed!")
    pos = pos_by_id(id)
    if pos == -1:
        abort(404)
    data = request.get_json()
    db[pos]["name"] = data["name"]
    return make_response(db[pos], 200, {'Content-Type': 'application/json'})


if __name__ == "__main__":
    app.run(port=5000, debug=True)