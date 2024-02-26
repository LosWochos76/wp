from flask import Flask, make_response, abort, request

app = Flask(__name__)

todos = [
    {'id': 1, 'name': 'git lernen'},
    {'id': 2, 'name': 'Flask lernen'},
    {'id': 3, 'name': 'HTML lernen'}
]

def pos_by_id(id):
    for pos, obj in enumerate(todos):
        if obj['id'] == id:
            return pos
    return -1

@app.route('/todos/', methods=["GET"])
def get_all():
    return make_response(todos, 200,
        {'Content-Type': 'application/json'})

@app.route('/todos/', methods=["POST"])
def add():
    data = request.get_json()
    if "name" not in data.keys():
        abort(500, message="name property missing!")
    obj = { "name": data["name"], "id": len(todos)+1 }
    todos.append(obj)
    return make_response(obj, 200, {'Content-Type': 'application/json'})

@app.route('/todos/<int:id>', methods=["GET"])
def get_single(id):
    pos = pos_by_id(id)
    if pos == -1:
        abort(404)
    return make_response(todos[pos], 200, {'Content-Type': 'application/json'})

@app.route('/todos/<int:id>', methods=["DELETE"])
def delete(id):
    pos = pos_by_id(id)
    if pos == -1:
        abort(404)
    del todos[pos]
    return make_response("", 200, {'Content-Type': 'application/json'})

@app.route('/todos/<int:id>', methods=["PUT"])
def update(id):
    pos = pos_by_id(id)
    if pos == -1:
        abort(404)
    data = request.get_json()
    todos[pos]["name"] = data["name"]
    return make_response(todos[pos], 200, {'Content-Type': 'application/json'})


if __name__ == "__main__":
    app.run(port=5000, debug=True)