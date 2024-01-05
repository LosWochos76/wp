from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/order", methods=['get', 'post'])
def order():
    if request.method == 'GET':
        return render_template('order.html')
    else:
        return render_template('deliver.html')

if __name__ == "__main__":
    app.run()